import json
import os
from datetime import datetime, timezone
from pathlib import Path

from config import (
    CLASSIFIED_FILE,
    DEFAULT_NOTIFY_CHANNELS,
    GITHUB_HANDLE,
    LINKEDIN_HANDLE,
    LINKEDIN_URL,
    NOTIFY_CHANNELS_ENV,
    STAGING_FILE,
)


def channel_enabled(channel: str) -> bool:
    raw = os.environ.get(NOTIFY_CHANNELS_ENV, DEFAULT_NOTIFY_CHANNELS).strip().lower()
    return not raw or raw in ("both", channel)


def run_date() -> str:
    return os.environ.get("RUN_DATE") or datetime.now(timezone.utc).strftime("%Y-%m-%d")


def run_url() -> str:
    return os.environ.get("RUN_URL", "")


def creator_tags() -> list[str]:
    return [
        f"github-{GITHUB_HANDLE.lower()}",
        f"linkedin-{LINKEDIN_HANDLE}",
    ]


def creator_line() -> str:
    return (
        f"GitHub: @{GITHUB_HANDLE}\n"
        f"LinkedIn: {LINKEDIN_URL}"
    )


def read_json_file(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def load_articles() -> list[dict]:
    return read_json_file(CLASSIFIED_FILE, [])


def load_staged_count() -> int:
    return len(read_json_file(STAGING_FILE, []))
