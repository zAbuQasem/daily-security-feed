"""
classify.py

Step 2 of the pipeline:
- Reads state/staged_articles.json from fetch_feeds.py
- Classifies each article using Copilot CLI or Claude API (configurable via CLASSIFIER_BACKEND)
- Writes state/classified_articles.json for downstream notification and state persistence
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

from config import CLASSIFIED_FILE, PROMPTS_DIR, STAGING_FILE
from injection_scanner import scan_for_injection

COPILOT_TIMEOUT = 120
CLAUDE_TIMEOUT = 120
CLAUDE_MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-4-20250514")
CLASSIFIER_BACKEND = os.environ.get("CLASSIFIER_BACKEND", "copilot").lower()


def _load_prompt() -> str:
    path = PROMPTS_DIR / "classify.md"
    text = path.read_text(encoding="utf-8")
    # Strip the H1 title line (first non-empty line starting with #) — it's for humans, not the model
    lines = text.splitlines()
    body_lines = [
        line for i, line in enumerate(lines) if not (i == 0 and line.startswith("#"))
    ]
    return "\n".join(body_lines).lstrip("\n")


_cached_prompt: str | None = None


def _get_prompt() -> str:
    global _cached_prompt
    if _cached_prompt is None:
        _cached_prompt = _load_prompt()
    return _cached_prompt


def _sanitize_field(value: str) -> str:
    """Strip newlines and control characters from a field before prompt interpolation."""
    return re.sub(r"[\r\n\t]", " ", value).strip()


def _build_article_text(article: dict) -> str:
    """Build the article portion of the prompt (shared across backends)."""
    published_at = _sanitize_field(article.get("published_at") or "unknown")
    return (
        f"Title: {article['title']}\n"
        f"URL: {article['url']}\n"
        f"Feed: {article['feed']}\n"
        f"Published: {published_at}\n\n"
        f"{article['content']}"
    )


def _extract_json(text: str) -> dict | None:
    """Extract a JSON object from text that may contain preamble."""
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        print("  → no JSON object found in output", file=sys.stderr)
        print(f"  → text: {text[:300]!r}", file=sys.stderr)
        return None
    try:
        return json.loads(text[start : end + 1])
    except json.JSONDecodeError as e:
        print(f"  → JSON parse error: {e}", file=sys.stderr)
        return None


def _classify_with_copilot(article: dict) -> dict | None:
    prompt = f"{_get_prompt()}\n\n---\n\n{_build_article_text(article)}"
    env = {
        **os.environ,
        "COPILOT_GITHUB_TOKEN": os.environ.get("COPILOT_GITHUB_TOKEN", ""),
    }

    try:
        result = subprocess.run(
            ["copilot", "--prompt", prompt],
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
            timeout=COPILOT_TIMEOUT,
            env=env,
        )
        if result.returncode != 0:
            print(
                f"  → CLI error (exit {result.returncode}): {result.stderr[:200]}",
                file=sys.stderr,
            )
            return None
        return _extract_json(result.stdout)
    except subprocess.TimeoutExpired:
        print("  → timeout", file=sys.stderr)
        return None
    except FileNotFoundError:
        print(
            "  → 'copilot' CLI not found — install with: npm i -g @github/copilot",
            file=sys.stderr,
        )
        sys.exit(1)
    except Exception as e:
        print(f"  → Error: {e}", file=sys.stderr)
        return None


def _classify_with_claude(article: dict) -> dict | None:
    try:
        import anthropic
    except ImportError:
        print(
            "  → 'anthropic' package not found — install with: uv add anthropic",
            file=sys.stderr,
        )
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        print("  → ANTHROPIC_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    article_text = _build_article_text(article)

    try:
        message = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=512,
            messages=[
                {
                    "role": "user",
                    "content": f"{_get_prompt()}\n\n---\n\n{article_text}",
                }
            ],
        )
        response_text = message.content[0].text
        return _extract_json(response_text)
    except anthropic.APITimeoutError:
        print("  → Claude API timeout", file=sys.stderr)
        return None
    except anthropic.APIError as e:
        print(f"  → Claude API error: {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  → Error: {e}", file=sys.stderr)
        return None


def classify_article(article: dict) -> dict | None:
    if CLASSIFIER_BACKEND == "claude":
        return _classify_with_claude(article)
    return _classify_with_copilot(article)


def main() -> None:
    if not STAGING_FILE.exists():
        print("No staged articles found — run fetch_feeds.py first")
        sys.exit(0)

    articles = json.loads(STAGING_FILE.read_text())
    if not articles:
        print("Staging file is empty — nothing to classify")
        sys.exit(0)

    skip_classify = os.environ.get("SKIP_CLASSIFY", "").strip().lower() in (
        "1",
        "true",
        "yes",
    )

    classified: list[dict] = []
    counts: dict[str, int] = {}

    for i, article in enumerate(articles, 1):
        print(f"[{i}/{len(articles)}] {article['title'][:70]}")

        if skip_classify:
            print("  → research (classification skipped)")
            classified.append(
                {
                    "url": article["url"],
                    "title": article["title"],
                    "feed": article["feed"],
                    "published_at": article.get("published_at"),
                    "fetched_at": article["fetched_at"],
                    "classified_at": datetime.now(timezone.utc).isoformat(),
                    "category": "research",
                    "priority": 2,
                    "tags": [],
                    "summary": "",
                }
            )
            counts["research"] = counts.get("research", 0) + 1
            continue

        # --- Prompt-injection pre-filter (scan all fields interpolated into the prompt) ---
        injection_hits: list[str] = []
        for field_name in ("content", "title", "url", "feed", "published_at"):
            value = article.get(field_name, "") or ""
            hits = [f"[{field_name}] {h}" for h in scan_for_injection(value)]
            injection_hits.extend(hits)
        injection_hits = list(dict.fromkeys(injection_hits))
        if injection_hits:
            print(
                f"  ⚠ Prompt-injection detected — {len(injection_hits)} pattern(s) matched, "
                "skipping AI call",
                file=sys.stderr,
            )
            for h in injection_hits:
                print(f"    ↳ {h}", file=sys.stderr)
            classified.append(
                {
                    "url": article["url"],
                    "title": article["title"],
                    "feed": article["feed"],
                    "published_at": article.get("published_at"),
                    "fetched_at": article["fetched_at"],
                    "classified_at": datetime.now(timezone.utc).isoformat(),
                    "category": "noise",
                    "priority": 3,
                    "tags": ["prompt-injection"],
                    "summary": "Article quarantined: content matched prompt-injection heuristics.",
                }
            )
            counts["noise-injection"] = counts.get("noise-injection", 0) + 1
            continue

        result = classify_article(article)
        if result is None:
            continue

        category = result.get("category", "noise")
        counts[category] = counts.get(category, 0) + 1
        print(f"  → {category}")
        classified.append(
            {
                "url": article["url"],
                "title": article["title"],
                "feed": article["feed"],
                "published_at": article.get("published_at"),
                "fetched_at": article["fetched_at"],
                "classified_at": datetime.now(timezone.utc).isoformat(),
                "category": category,
                "priority": min(3, max(1, int(result.get("priority") or 3))),
                "tags": result.get("tags") or [],
                "summary": (result.get("summary") or "").strip(),
            }
        )

    CLASSIFIED_FILE.write_text(json.dumps(classified, indent=2))
    print(f"\nClassification complete: {counts}")
    print(f"Results written to {CLASSIFIED_FILE}")


if __name__ == "__main__":
    main()
