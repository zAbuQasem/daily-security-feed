"""
notify_slack.py

Sends Slack webhook notifications after the pipeline runs.
Uses Slack Block Kit for rich formatting.

Usage:
    python pipeline/notify_slack.py success
    python pipeline/notify_slack.py failure --step "Step 2 — Classify with Copilot"

Environment variables:
    SLACK_WEBHOOK_URL     Slack incoming webhook URL (repo secret)
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
from common import channel_enabled, load_articles, run_date, run_url, truncate
from config import USER_AGENT

PRIORITY_EMOJI = {
    1: ":red_circle:",
    2: ":large_orange_circle:",
    3: ":large_blue_circle:",
}
PRIORITY_LABEL = {1: "Critical", 2: "Solid", 3: "Low"}


def _pages_url() -> str:
    return os.environ.get("PAGES_URL", "").strip()


def send(payload: dict) -> None:
    if not channel_enabled("slack"):
        print("Slack notifications disabled by NOTIFY_CHANNELS")
        return

    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("SLACK_WEBHOOK_URL not set \u2014 skipping notification")
        return

    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        webhook_url,
        data=data,
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


def _build_article_line(article: dict) -> str:
    title = truncate(article.get("title", "Untitled"), 72)
    url = article.get("url", "")
    priority = article.get("priority", 3)
    emoji = PRIORITY_EMOJI.get(priority, ":white_circle:")

    if url:
        return f"{emoji}  <{url}|{title}>"
    return f"{emoji}  {title}"


def build_success_payload(articles: list[dict]) -> dict:
    date = run_date()

    # -- Header --
    blocks: list[dict] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"\U0001f4e1  Security Feed  \u00b7  {date}",
            },
        },
    ]

    if not articles:
        blocks.append(
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": "_No new research articles today._"},
            }
        )
    else:
        sorted_articles = sorted(articles, key=lambda a: a.get("priority") or 3)

        # -- Stats line --
        total = len(sorted_articles)
        p1 = sum(1 for a in sorted_articles if a.get("priority") == 1)
        p2 = sum(1 for a in sorted_articles if a.get("priority") == 2)
        p3 = total - p1 - p2

        stats_parts = [f"*{total}* article{'s' if total != 1 else ''}"]
        if p1:
            stats_parts.append(f":red_circle: {p1} critical")
        if p2:
            stats_parts.append(f":large_orange_circle: {p2} solid")
        if p3:
            stats_parts.append(f":large_blue_circle: {p3} low")

        blocks.append(
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": "  \u2022  ".join(stats_parts)}
                ],
            }
        )

        blocks.append({"type": "divider"})

        # -- Group by priority --
        for prio in (1, 2, 3):
            prio_articles = [a for a in sorted_articles if a.get("priority") == prio]
            if not prio_articles:
                continue

            label = PRIORITY_LABEL.get(prio, "Other")
            emoji = PRIORITY_EMOJI.get(prio, ":white_circle:")
            lines = [_build_article_line(a) for a in prio_articles[:25]]

            blocks.append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*{emoji} {label}*\n" + "\n".join(lines),
                    },
                }
            )

    blocks.append({"type": "divider"})

    # -- Footer actions --
    footer_parts = []
    url = run_url()
    pages = _pages_url()
    if pages:
        footer_parts.append(f"<{pages}|:globe_with_meridians: Browse feed>")
    if url:
        footer_parts.append(f"<{url}|:gear: View run>")

    if footer_parts:
        blocks.append(
            {
                "type": "context",
                "elements": [{"type": "mrkdwn", "text": "  │  ".join(footer_parts)}],
            }
        )
    footer_parts.append(f"<{LINKEDIN_URL}|:briefcase: LinkedIn>")

    blocks.append(
        {
            "type": "context",
            "elements": [{"type": "mrkdwn", "text": "  \u2502  ".join(footer_parts)}],
        }
    )

    # Fallback text for notifications/previews
    fallback = f"\U0001f4e1 Security Feed {date} \u2014 {len(articles)} article{'s' if len(articles) != 1 else ''}"

    return {"text": fallback, "blocks": blocks}


def build_failure_payload(step: str) -> dict:
    date = run_date()
    url = run_url()

    blocks: list[dict] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"\u274c  Pipeline Failed  \u00b7  {date}",
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Failed step:*  `{step}`",
            },
        },
    ]

    if url:
        blocks.append(
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": ":mag: View Logs"},
                        "url": url,
                        "style": "danger",
                    },
                ],
            }
        )

    return {
        "text": f"\u274c Security Feed failed on {date} at: {step}",
        "blocks": blocks,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["success", "failure"])
    parser.add_argument(
        "--step", default="unknown step", help="Name of the failed step"
    )
    args = parser.parse_args()

    if args.mode == "success":
        send(build_success_payload(load_articles()))
    else:
        send(build_failure_payload(args.step))


if __name__ == "__main__":
    main()
