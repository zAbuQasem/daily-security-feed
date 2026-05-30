"""
notify_discord.py

Sends a Discord embed notification after the pipeline runs.

Usage:
    # Success
    python pipeline/notify_discord.py success

    # Failure
    python pipeline/notify_discord.py failure --step "Step 2 — Classify with Copilot"

Environment variables:
    DISCORD_WEBHOOK_URL   Discord webhook URL, or comma/newline-separated list for fan-out (repo secret)
    RUN_URL               GitHub Actions run URL (set in workflow)
    RUN_DATE              ISO date string (optional, defaults to today UTC)
    NOTIFY_CHANNELS       Notification targets: discord, slack, both, or comma-separated list
    PAGES_URL             GitHub Pages site URL (optional, for "Browse feed" link)
"""

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

from common import (
    channel_enabled,
    load_articles,
    pages_url,
    run_date,
    run_url,
    truncate,
)
from config import USER_AGENT

COLOR_SUCCESS = 0x57F287  # green
COLOR_FAILURE = 0xED4245  # red

MAX_TITLE_LEN = 80


def build_feed_embed(articles: list[dict]) -> dict:
    """Build a single embed with all research articles sorted by priority."""
    title = f"📡  Today's Feed  ·  {run_date()}"
    pages = pages_url()

    sorted_articles = sorted(articles, key=lambda a: a.get("priority") or 3)

    if not sorted_articles:
        embed = {
            "title": title,
            "description": "No new content today.",
            "color": 0x99AAB5,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        if pages:
            embed["url"] = pages
        return embed

    lines = []
    for i, a in enumerate(sorted_articles, 1):
        t = truncate(a.get("title", "Untitled"), MAX_TITLE_LEN)
        url = a.get("url", "")
        lines.append(f"{i}. [{t}]({url})" if url else f"{i}. {t}")

    if pages:
        lines.append(f"\n[Browse feed →]({pages})")

    description = "\n".join(lines)
    if len(description) > 4096:
        description = description[:4093] + "…"

    embed = {
        "title": title,
        "description": description,
        "color": COLOR_SUCCESS,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    if pages:
        embed["url"] = pages
    return embed


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

    pages = pages_url()
    if pages:
        embed["fields"].append(
            {"name": "Feed", "value": f"[Browse feed →]({pages})", "inline": False}
        )

    return embed


def _parse_webhook_urls(raw: str) -> list[str]:
    # Split on comma or newline so secrets can hold multiple URLs.
    return [u.strip() for u in raw.replace("\n", ",").split(",") if u.strip()]


def send(embeds: list[dict]) -> None:
    if not channel_enabled("discord"):
        print("Discord notifications disabled by NOTIFY_CHANNELS")
        return

    webhook_urls = _parse_webhook_urls(os.environ.get("DISCORD_WEBHOOK_URL", ""))
    if not webhook_urls:
        print("DISCORD_WEBHOOK_URL not set — skipping notification")
        return

    # Discord allows up to 10 embeds per message
    payload = json.dumps({"embeds": embeds[:10]}).encode()
    failures = 0
    for i, webhook_url in enumerate(webhook_urls, 1):
        label = f"[{i}/{len(webhook_urls)}]" if len(webhook_urls) > 1 else ""
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
                    print(f"Discord notification sent {label}".rstrip())
                else:
                    print(
                        f"Discord responded with {resp.status} {label}".rstrip(),
                        file=sys.stderr,
                    )
        except urllib.error.HTTPError as e:
            failures += 1
            print(
                f"Discord webhook error {label}: {e.code} {e.reason}".rstrip(),
                file=sys.stderr,
            )

    if failures:
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
        send([build_feed_embed(articles)])
    else:
        send([build_failure_embed(args.step)])


if __name__ == "__main__":
    main()
