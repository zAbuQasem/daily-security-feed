"""
write_vault.py

Step 3 of the pipeline:
- Reads state/classified_articles.json
- For each research article, writes a Jekyll post to site/_posts/
- Posts include YAML frontmatter and the AI-generated summary
- Skips articles that already have a note (idempotent)
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from common import creator_tags
from config import CLASSIFIED_FILE, VAULT_DIR


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:60].strip("-")


_DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")


def _article_date(article: dict) -> str:
    """Return the best date string for an article: published_at if valid, else fetched_at."""
    for field in ("published_at", "fetched_at"):
        value = article.get(field) or ""
        if _DATE_RE.match(value):
            return value
    return datetime.now(timezone.utc).isoformat()


def note_path(article: dict) -> Path:
    date = _article_date(article)[:10]
    slug = slugify(article.get("title", "untitled")) or "untitled"
    path = VAULT_DIR / f"{date}-{slug}.md"
    if not path.resolve().is_relative_to(VAULT_DIR.resolve()):
        raise ValueError(f"Resolved path escapes VAULT_DIR: {path}")
    return path


def build_note(article: dict) -> str:
    title = article.get("title", "Untitled")
    url = article.get("url", "")
    tags = [
        t
        for t in (article.get("tags") or []) + creator_tags()
        if not t.startswith("github-") and not t.startswith("linkedin-")
    ]
    date = _article_date(article)[:19]  # YYYY-MM-DDTHH:MM:SS
    if len(date) == 10:
        date += " 00:00:00"
    else:
        date = date.replace("T", " ")
    summary = article.get("summary", "").strip()

    unique_tags = list(dict.fromkeys(tags))
    tag_yaml = "[" + ", ".join(unique_tags) + "]" if unique_tags else "[]"

    cat_yaml = "[RSS]"

    # Escape title for YAML
    safe_title = title.replace('"', '\\"').replace("\n", " ").replace("\r", " ")

    frontmatter = (
        "---\n"
        "layout: post\n"
        f'title: "{safe_title}"\n'
        f"date: {date} +0300\n"
        f"categories: {cat_yaml}\n"
        f"tags: {tag_yaml}\n"
        "toc: true\n"
        "---\n"
    )

    body_parts = []
    if summary:
        body_parts.append(summary)
    else:
        body_parts.append("_No summary available._")

    if url:
        body_parts.append(f"\n[Read original article]({url}){{: .btn .btn-primary }}")

    return frontmatter + "\n" + "\n".join(body_parts) + "\n"


def main() -> None:
    if not CLASSIFIED_FILE.exists():
        print("No classified articles found — run classify.py first")
        sys.exit(0)

    articles = json.loads(CLASSIFIED_FILE.read_text())
    research = [a for a in articles if a.get("category") == "research"]

    if not research:
        print("No research articles to write to vault")
        sys.exit(0)

    VAULT_DIR.mkdir(parents=True, exist_ok=True)

    written = 0
    skipped = 0
    for article in research:
        path = note_path(article)
        if path.exists():
            skipped += 1
            continue
        path.write_text(build_note(article), encoding="utf-8")
        print(f"  ✓ {path.name}")
        written += 1

    print(f"\nVault: {written} note(s) written, {skipped} already existed")


if __name__ == "__main__":
    main()
