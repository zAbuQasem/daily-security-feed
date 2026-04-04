import json
import os
from datetime import datetime, timezone
from pathlib import Path

from config import (
    CLASSIFIED_FILE,
    DEFAULT_NOTIFY_CHANNELS,
    GITHUB_HANDLE,
    LINKEDIN_HANDLE,
    NOTIFY_CHANNELS_ENV,
)


def channel_enabled(channel: str) -> bool:
    raw = os.environ.get(NOTIFY_CHANNELS_ENV, DEFAULT_NOTIFY_CHANNELS).strip().lower()
    return not raw or raw == "both" or channel in [c.strip() for c in raw.split(",")]


def run_date() -> str:
    return os.environ.get("RUN_DATE") or datetime.now(timezone.utc).strftime("%Y-%m-%d")


def run_url() -> str:
    return os.environ.get("RUN_URL", "")


def pages_url() -> str:
    return os.environ.get("PAGES_URL", "").strip()


def creator_tags() -> list[str]:
    return [
        f"github-{GITHUB_HANDLE.lower()}",
        f"linkedin-{LINKEDIN_HANDLE}",
    ]


def truncate(text: str, length: int) -> str:
    return text[: length - 1] + "\u2026" if len(text) > length else text


def read_json_file(path: Path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text())
    except Exception:
        return default


def load_articles() -> list[dict]:
    return read_json_file(CLASSIFIED_FILE, [])
