"""
notify_discord.py

Sends a Discord embed notification after the pipeline runs.

Usage:
    # Success
    python scripts/notify_discord.py success

    # Failure
    python scripts/notify_discord.py failure --step "Step 2 — Classify with Copilot"

Environment variables:
    DISCORD_WEBHOOK_URL   Discord webhook URL (repo secret)
    RUN_URL               GitHub Actions run URL (set in workflow)
    RUN_DATE              ISO date string (set in workflow)
    NOTIFY_CHANNELS       Notification targets: discord, slack, both, or comma-separated list
"""

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

from common import channel_enabled, creator_line, load_articles, run_date, run_url
from config import USER_AGENT

COLOR_SUCCESS = 0x57F287  # green
COLOR_FAILURE = 0xED4245  # red


def _build_category_embed(
    articles: list[dict],
    categories: list[tuple[str, str, int]],
    title: str,
    color: int,
) -> dict | None:
    MAX_TITLE_LEN = 80

    by_category: dict[str, list[dict]] = {}
    for a in articles:
        cat = a.get("category", "noise")
        by_category.setdefault(cat, []).append(a)

    sections = []
    for cat_key, cat_label, limit in categories:
        cat_articles = sorted(
            by_category.get(cat_key, []),
            key=lambda a: (a.get("priority") or 3),
        )[:limit]
        if not cat_articles:
            continue
        lines = [f"**{cat_label}**"] if cat_label else []
        for i, a in enumerate(cat_articles, 1):
            t = a.get("title", "Untitled")
            if len(t) > MAX_TITLE_LEN:
                t = t[: MAX_TITLE_LEN - 1] + "…"
            url = a.get("url", "")
            tags = a.get("tags", [])
            tag_str = "  " + " ".join(f"`{tag}`" for tag in tags[:3]) if tags else ""
            lines.append(f"{i}. [{t}]({url}){tag_str}" if url else f"{i}. {t}{tag_str}")
        sections.append("\n".join(lines))

    if not sections:
        return None

    description = "\n\n".join(sections)
    if len(description) > 4096:
        description = description[:4093] + "…"

    return {
        "title": title,
        "description": description,
        "color": color,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


def build_feed_embed(articles: list[dict]) -> dict | None:
    """All articles: Research first, then Security Feed, sorted by priority."""
    embed = _build_category_embed(
        articles,
        categories=[
            ("research", "", 100),
        ],
        title=f"📡  Today's Feed  ·  {run_date()}",
        color=COLOR_SUCCESS,
    )
    if embed is not None:
        embed["fields"] = [
            {
                "name": "Creator",
                "value": creator_line().replace("Creator: ", ""),
                "inline": False,
            }
        ]
        return embed

    fallback = {
        "title": f"📡  Today's Feed  ·  {run_date()}",
        "description": "No new content today.",
        "color": 0x99AAB5,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    url = run_url()
    if url:
        fallback["url"] = url
    fallback["fields"] = [
        {
            "name": "Creator",
            "value": creator_line().replace("Creator: ", ""),
            "inline": False,
        }
    ]
    return fallback


def build_failure_embed(step: str) -> dict:
    embed = {
        "title": f"❌  Pipeline Failed  ·  {run_date()}",
        "color": COLOR_FAILURE,
        "fields": [
            {"name": "Failed at", "value": f"`{step}`", "inline": False},
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    url = run_url()
    if url:
        embed["url"] = url
        embed["fields"].append(
            {"name": "Logs", "value": f"[View run →]({url})", "inline": False}
        )

    embed["fields"].append(
        {
            "name": "Creator",
            "value": creator_line().replace("Creator: ", ""),
            "inline": False,
        }
    )

    return embed


def send(embeds: list[dict]) -> None:
    if not channel_enabled("discord"):
        print("Discord notifications disabled by NOTIFY_CHANNELS")
        return

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("DISCORD_WEBHOOK_URL not set — skipping notification")
        return

    # Discord allows up to 10 embeds per message
    payload = json.dumps({"embeds": embeds[:10]}).encode()
    req = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status == 204:
                print("Discord notification sent")
            else:
                print(f"Discord responded with {resp.status}", file=sys.stderr)
    except urllib.error.HTTPError as e:
        print(f"Discord webhook error: {e.code} {e.reason}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["success", "failure"])
    parser.add_argument(
        "--step", default="unknown step", help="Name of the failed step"
    )
    args = parser.parse_args()

    if args.mode == "success":
        articles = load_articles()
        feed = build_feed_embed(articles)
        if feed:
            send([feed])
    else:
        send([build_failure_embed(args.step)])


if __name__ == "__main__":
    main()
