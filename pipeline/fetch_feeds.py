"""
fetch_feeds.py

Step 1 of the pipeline:
- Parse feeds.yaml for the list of RSS URLs
- Fetch each feed with feedparser (up to ENTRIES_PER_FEED recent entries)
- Skip URLs already in state/processed_urls.json
- Run defuddle on new article URLs to extract clean markdown content
- Write state/staged_articles.json for classify.py to consume
- Update state/processed_urls.json (all seen URLs, including failed extractions)
"""

import calendar
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone

import feedparser
import yaml

from config import FEEDS_FILE, PROCESSED_URLS_FILE, STAGING_FILE, URL_LOG_FILE

MAX_ARTICLES = int(os.environ.get("MAX_ARTICLES", 100))
ENTRIES_PER_FEED = int(os.environ.get("ENTRIES_PER_FEED", 5))
MAX_ARTICLE_AGE_DAYS = int(os.environ.get("MAX_ARTICLE_AGE_DAYS", 7))
FEED_FETCH_WORKERS = 30
DEFUDDLE_TIMEOUT = 30
MIN_CONTENT_LENGTH = 200
MAX_CONTENT_LENGTH = 8000


def load_state() -> dict:
    if not PROCESSED_URLS_FILE.exists():
        return {"processed_urls": {}, "last_updated": None}
    data = json.loads(PROCESSED_URLS_FILE.read_text())
    urls = data.get("processed_urls", {})
    # Migrate from old list format
    if isinstance(urls, list):
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        urls = {url: today for url in urls}
    data["processed_urls"] = urls
    return data


def save_state(state: dict) -> None:
    PROCESSED_URLS_FILE.write_text(json.dumps(state, indent=2))


def load_feed_urls() -> list[str]:
    data = yaml.safe_load(FEEDS_FILE.read_text())
    return [
        url
        for url in data.get("feeds", [])
        if isinstance(url, str) and url.startswith("http")
    ]


def _parse_entry_date(entry) -> datetime | None:
    """Extract published/updated date from a feedparser entry."""
    for attr in ("published_parsed", "updated_parsed"):
        parsed = getattr(entry, attr, None)
        if parsed:
            try:
                return datetime.fromtimestamp(calendar.timegm(parsed), tz=timezone.utc)
            except (ValueError, OverflowError, OSError):
                continue
    return None


def fetch_feed(feed_url: str, cutoff: datetime) -> list[dict]:
    try:
        d = feedparser.parse(
            feed_url,
            request_headers={"User-Agent": "Mozilla/5.0 (security-feed-bot)"},
        )
        entries = []
        for entry in d.entries:
            link = entry.get("link", "").strip()
            title = entry.get("title", "").strip()
            if not (link and title and link.startswith("http")):
                continue
            published_at = _parse_entry_date(entry)
            if published_at and published_at < cutoff:
                continue
            entries.append(
                {
                    "url": link,
                    "title": title,
                    "feed": feed_url,
                    "published_at": published_at.isoformat() if published_at else None,
                }
            )
            if len(entries) >= ENTRIES_PER_FEED:
                break
        return entries
    except Exception as e:
        print(f"  [feed error] {feed_url}: {e}", file=sys.stderr)
        return []


def extract_with_defuddle(url: str) -> str:
    try:
        result = subprocess.run(
            ["defuddle", "parse", "--json", "--md", url],
            capture_output=True,
            text=True,
            timeout=DEFUDDLE_TIMEOUT,
        )
        if result.returncode != 0:
            return ""
        data = json.loads(result.stdout)
        # defuddle --json returns {content, title, description, ...}
        return data.get("content", "") or data.get("markdown", "")
    except (subprocess.TimeoutExpired, json.JSONDecodeError, FileNotFoundError):
        return ""
    except Exception as e:
        print(f"  [defuddle error] {url}: {e}", file=sys.stderr)
        return ""


def main() -> None:
    state = load_state()
    seen_urls: dict[str, str] = state["processed_urls"]  # {url: date_seen}
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    feed_urls = load_feed_urls()

    print(f"Loaded {len(feed_urls)} feeds | {len(seen_urls)} already-seen URLs")

    # --- Step 1: Fetch all feeds concurrently ---
    cutoff = datetime.now(timezone.utc) - timedelta(days=MAX_ARTICLE_AGE_DAYS)
    candidates: list[dict] = []
    with ThreadPoolExecutor(max_workers=FEED_FETCH_WORKERS) as executor:
        futures = {executor.submit(fetch_feed, url, cutoff): url for url in feed_urls}
        for i, future in enumerate(as_completed(futures), 1):
            entries = future.result()
            for entry in entries:
                if entry["url"] not in seen_urls:
                    candidates.append(entry)
                    seen_urls[entry["url"]] = today  # prevent duplicates across feeds

    print(f"Found {len(candidates)} new candidate articles (cap: {MAX_ARTICLES})")
    candidates = candidates[:MAX_ARTICLES]

    # --- Step 2: Extract content via defuddle ---
    articles: list[dict] = []
    for i, candidate in enumerate(candidates, 1):
        print(f"[{i}/{len(candidates)}] {candidate['title'][:70]}")
        content = extract_with_defuddle(candidate["url"])

        # Always mark as seen to avoid retry loops on dead URLs
        seen_urls.setdefault(candidate["url"], today)

        if len(content) >= MIN_CONTENT_LENGTH:
            articles.append(
                {
                    "url": candidate["url"],
                    "title": candidate["title"],
                    "feed": candidate["feed"],
                    "published_at": candidate.get("published_at"),
                    "content": content[:MAX_CONTENT_LENGTH],
                    "fetched_at": datetime.now(timezone.utc).isoformat(),
                }
            )
            print(f"  ✓ {len(content)} chars extracted")
        else:
            print(f"  ✗ content too short ({len(content)} chars), skipping")

    # --- Step 3: Append processed URLs to log file ---
    if articles:
        URL_LOG_FILE.parent.mkdir(exist_ok=True)
        with URL_LOG_FILE.open("a") as f:
            for article in articles:
                f.write(f"[{today}] {article['url']}\n")

    # --- Step 4: Write staging file ---
    STAGING_FILE.write_text(json.dumps(articles, indent=2))

    # --- Step 5: Persist updated state ---
    state["processed_urls"] = seen_urls
    state["last_updated"] = datetime.now(timezone.utc).isoformat()
    save_state(state)

    print(f"\nDone — {len(articles)} articles staged for classification")


if __name__ == "__main__":
    main()
