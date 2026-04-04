from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
STATE_DIR = REPO_ROOT / "state"

CLASSIFIED_FILE = STATE_DIR / "classified_articles.json"
STAGING_FILE = STATE_DIR / "staged_articles.json"
PROCESSED_URLS_FILE = STATE_DIR / "processed_urls.json"
URL_LOG_FILE = REPO_ROOT / "logs" / "urls.txt"
FEEDS_FILE = REPO_ROOT / "feeds" / "feeds.yaml"
VAULT_DIR = REPO_ROOT / "site" / "_posts"
PROMPTS_DIR = REPO_ROOT / "prompts"

NOTIFY_CHANNELS_ENV = "NOTIFY_CHANNELS"
DEFAULT_NOTIFY_CHANNELS = "both"
GITHUB_HANDLE = "zAbuQasem"
LINKEDIN_URL = "https://www.linkedin.com/in/zeyad-abulaban/"
LINKEDIN_HANDLE = "zeyad-abulaban"
USER_AGENT = "rss-pipeline/1.0"
