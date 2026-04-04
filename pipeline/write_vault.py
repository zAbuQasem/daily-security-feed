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

from common import creator_tags
from config import CLASSIFIED_FILE, VAULT_DIR


def slugify(title: str) -> str:
    slug = title.lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    return slug[:60].strip("-")


def note_path(article: dict):
    date = (article.get("fetched_at") or datetime.now(timezone.utc).isoformat())[:10]
    slug = slugify(article.get("title", "untitled"))
    return VAULT_DIR / f"{date}-{slug}.md"


def build_note(article: dict) -> str:
    title = article.get("title", "Untitled")
    url = article.get("url", "")
    tags = (article.get("tags") or []) + creator_tags()
    priority = article.get("priority", 3)
    date = (article.get("fetched_at") or "")[:10]
    feed = article.get("feed", "")
    summary = article.get("summary", "").strip()

    unique_tags = list(dict.fromkeys(tags))
    tag_yaml = "[" + ", ".join(unique_tags) + "]" if unique_tags else "[]"

    frontmatter = (
        "---\n"
        "layout: post\n"
        f'title: "{title.replace(chr(34), chr(39))}"\n'
        f"url: {url}\n"
        f"date: {date}\n"
        f"priority: {priority}\n"
        f"tags: {tag_yaml}\n"
        f"feed: {feed}\n"
        "---\n"
    )

    body = summary if summary else "_No summary available._"
    return frontmatter + "\n" + body + "\n"


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
