"""
classify.py

Step 2 of the pipeline:
- Reads state/staged_articles.json from fetch_feeds.py
- Sends each article to the Copilot CLI with a structured classification prompt
- Writes state/classified_articles.json for downstream notification and state persistence
"""

import json
import os
import subprocess
import sys
from datetime import datetime, timezone

from config import CLASSIFIED_FILE, PROMPTS_DIR, STAGING_FILE

COPILOT_TIMEOUT = 120


def _load_prompt() -> str:
        path = PROMPTS_DIR / "classify.md"
        text = path.read_text(encoding="utf-8")
        # Strip the H1 title line (first non-empty line starting with #) — it's for humans, not the model
        lines = text.splitlines()
        body_lines = [l for i, l in enumerate(lines) if not (i == 0 and l.startswith("#"))]
        return "\n".join(body_lines).lstrip("\n")


SYSTEM_PROMPT = _load_prompt()


def classify_article(article: dict) -> dict | None:
    prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"---\n\n"
        f"Title: {article['title']}\n"
        f"URL: {article['url']}\n"
        f"Feed: {article['feed']}\n\n"
        f"{article['content']}"
    )

    env = {
        **os.environ,
        "COPILOT_GITHUB_TOKEN": os.environ.get("COPILOT_GITHUB_TOKEN", ""),
    }

    try:
        result = subprocess.run(
            ["copilot", "--prompt", prompt, "--allow-all-tools", "--allow-all-paths"],
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

        # The CLI may emit a preamble before the JSON fence — extract the JSON object directly
        text = result.stdout
        start = text.find("{")
        end = text.rfind("}")
        if start == -1 or end == -1:
            print("  → no JSON object found in output", file=sys.stderr)
            print(f"  → stdout: {text[:300]!r}", file=sys.stderr)
            return None

        parsed = json.loads(text[start : end + 1])
        return parsed
    except subprocess.TimeoutExpired:
        print("  → timeout", file=sys.stderr)
        return None
    except json.JSONDecodeError as e:
        print(f"  → JSON parse error: {e}", file=sys.stderr)
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


def main() -> None:
    if not STAGING_FILE.exists():
        print("No staged articles found — run fetch_feeds.py first")
        sys.exit(0)

    articles = json.loads(STAGING_FILE.read_text())
    if not articles:
        print("Staging file is empty — nothing to classify")
        sys.exit(0)

    classified: list[dict] = []
    counts: dict[str, int] = {}

    for i, article in enumerate(articles, 1):
        print(f"[{i}/{len(articles)}] {article['title'][:70]}")
        result = classify_article(article)
        if result is None:
            continue

        category = result.get("category", "noise")
        counts[category] = counts.get(category, 0) + 1
        print(f"  → {category}")
        if category != "research":
            continue
        classified.append(
            {
                "url": article["url"],
                "title": article["title"],
                "feed": article["feed"],
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
