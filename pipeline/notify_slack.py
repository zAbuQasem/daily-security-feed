"""
notify_slack.py

Sends Slack webhook notifications after the pipeline runs.

Usage:
    python scripts/notify_slack.py success
    python scripts/notify_slack.py failure --step "Step 2 — Classify with Copilot"

Environment variables:
    SLACK_WEBHOOK_URL     Slack incoming webhook URL (repo secret)
    RUN_URL               GitHub Actions run URL (set in workflow)
    RUN_DATE              ISO date string (optional)
    NOTIFY_CHANNELS       Notification targets: discord, slack, both, or comma-separated list
"""

import argparse
import json
import os
import sys
import urllib.request
from common import channel_enabled, creator_line, load_articles, run_date, run_url
from config import USER_AGENT


def send(text: str) -> None:
    if not channel_enabled("slack"):
        print("Slack notifications disabled by NOTIFY_CHANNELS")
        return

    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("SLACK_WEBHOOK_URL not set — skipping notification")
        return

    payload = json.dumps({"text": text}).encode()
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
            if 200 <= resp.status < 300:
                print("Slack notification sent")
            else:
                print(f"Slack responded with {resp.status}", file=sys.stderr)
                sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"Slack webhook error: {e.code} {e.reason}", file=sys.stderr)
        sys.exit(1)


def build_success_message(articles: list[dict]) -> list[str]:
    lines = [f":satellite_antenna: Daily Security Content Feed {run_date()}"]

    if not articles:
        lines.append("No new content today.")
    else:
        sorted_articles = sorted(articles, key=lambda a: (a.get("priority") or 3))
        for i, article in enumerate(sorted_articles[:50], 1):
            title = article.get("title", "Untitled")
            url = article.get("url", "")
            priority = article.get("priority", 3)
            tags = article.get("tags", [])
            tag_str = " [" + ", ".join(tags[:3]) + "]" if tags else ""
            if url:
                lines.append(f"{i}. [P{priority}] {title}{tag_str} - {url}")
            else:
                lines.append(f"{i}. [P{priority}] {title}{tag_str}")

    url = run_url()
    if url:
        lines.append(f"Run: {url}")
    lines.append(creator_line())
    return lines


def build_failure_message(step: str) -> str:
    lines = [
        f":x: Security Feed failed on {run_date()}",
        f"Failed step: {step}",
    ]
    url = run_url()
    if url:
        lines.append(f"Run: {url}")
    lines.append(creator_line())
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["success", "failure"])
    parser.add_argument(
        "--step", default="unknown step", help="Name of the failed step"
    )
    args = parser.parse_args()

    if args.mode == "success":
        send("\n".join(build_success_message(load_articles())))
        return

    send(build_failure_message(args.step))


if __name__ == "__main__":
    main()
