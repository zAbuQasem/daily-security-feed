"""
remind_rotate.py

Sends a monthly secret rotation reminder to Discord and Slack.

Environment variables:
    DISCORD_WEBHOOK_URL   Discord webhook URL
    SLACK_WEBHOOK_URL     Slack incoming webhook URL
    RUN_URL               GitHub Actions run URL (set in workflow)
    NOTIFY_CHANNELS       Notification targets: discord, slack, both, or comma-separated list
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

from common import channel_enabled
from config import USER_AGENT

COLOR_WARNING = 0xFEE75C  # yellow

SECRETS = [
    {
        "name": "`COPILOT_TOKEN`",
        "description": (
            "Fine-grained PAT for Copilot CLI authentication\n"
            "**Permission:** `Copilot Requests: Read`\n"
            "**Rotate at:** GitHub → Settings → Developer settings → Fine-grained personal access tokens"
        ),
    },
]


def build_embed() -> dict:
    now = datetime.now(timezone.utc)
    fields = [
        {
            "name": s["name"],
            "value": s["description"],
            "inline": False,
        }
        for s in SECRETS
    ]
    fields.append(
        {
            "name": "Security warning",
            "value": (
                "Treat feed content as untrusted input. An article can contain indirect prompt-injection "
                "instructions aimed at the AI classifier. Keep PATs and webhooks in Actions secrets only, "
                "never expose broader repo or org credentials, and rotate them monthly to reduce exfiltration impact."
            ),
            "inline": False,
        }
    )
    fields.append(
        {
            "name": "After rotating",
            "value": (
                "Update each value in **Repo → Settings → Secrets → Actions**\n"
                "then re-run the pipeline to verify."
            ),
            "inline": False,
        }
    )

    embed = {
        "title": "🔑  Monthly Secret Rotation Reminder",
        "description": "Time to rotate credentials and verify they still work.",
        "color": COLOR_WARNING,
        "fields": fields,
        "footer": {"text": "Runs on the 1st of every month  ·  RSS pipeline"},
        "timestamp": now.isoformat(),
    }

    run_url = os.environ.get("RUN_URL", "")
    if run_url:
        embed["url"] = run_url

    return embed


def send(embed: dict) -> None:
    if not channel_enabled("discord"):
        print("Discord reminders disabled by NOTIFY_CHANNELS")
        return

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("DISCORD_WEBHOOK_URL not set — skipping notification")
        return

    payload = json.dumps({"embeds": [embed]}).encode()
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
                print("Rotation reminder sent to Discord")
            else:
                print(f"Discord responded with {resp.status}", file=sys.stderr)
                sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"Discord webhook error: {e.code} {e.reason}", file=sys.stderr)
        sys.exit(1)


def build_slack_payload() -> dict:
    run_url = os.environ.get("RUN_URL", "").strip()
    lines = [
        ":warning: Monthly secret rotation reminder for the RSS pipeline.",
        "Rotate these secrets now and verify the workflow still succeeds:",
        "- COPILOT_TOKEN: fine-grained PAT with Copilot Requests: Read",
        "Security warning: feed articles are untrusted input. Indirect prompt injection can try to coerce the classifier into secret exfiltration. Use least-privilege secrets and rotate them monthly.",
    ]
    if run_url:
        lines.append(f"Workflow run: {run_url}")
    return {"text": "\n".join(lines)}


def send_slack(payload: dict) -> None:
    if not channel_enabled("slack"):
        print("Slack reminders disabled by NOTIFY_CHANNELS")
        return

    webhook_url = os.environ.get("SLACK_WEBHOOK_URL", "").strip()
    if not webhook_url:
        print("SLACK_WEBHOOK_URL not set — skipping notification")
        return

    req = urllib.request.Request(
        webhook_url,
        data=json.dumps(payload).encode(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if 200 <= resp.status < 300:
                print("Rotation reminder sent to Slack")
            else:
                print(f"Slack responded with {resp.status}", file=sys.stderr)
                sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"Slack webhook error: {e.code} {e.reason}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    send(build_embed())
    send_slack(build_slack_payload())
