"""
persist_state.py

Step 4 of the pipeline:
- Commits and pushes updated state files needed for future deduplication
- Also commits new Jekyll posts written by write_vault.py to site/_posts/
"""

import os
import subprocess
import sys
from datetime import datetime, timezone

from config import PROCESSED_URLS_FILE, REPO_ROOT, URL_LOG_FILE, VAULT_DIR

TRACKED_PATHS = [
    str(PROCESSED_URLS_FILE.relative_to(REPO_ROOT)),
    str(URL_LOG_FILE.relative_to(REPO_ROOT)),
]


def git_commit() -> None:
    git_env = {
        **os.environ,
        "GIT_AUTHOR_NAME": "github-actions[bot]",
        "GIT_AUTHOR_EMAIL": "41898282+github-actions[bot]@users.noreply.github.com",
        "GIT_COMMITTER_NAME": "github-actions[bot]",
        "GIT_COMMITTER_EMAIL": "41898282+github-actions[bot]@users.noreply.github.com",
    }

    for rel_path in TRACKED_PATHS:
        subprocess.run(["git", "add", rel_path], cwd=REPO_ROOT, check=True)

    # Stage any new vault notes (directory may not exist if no research was found)
    if VAULT_DIR.exists():
        subprocess.run(
            ["git", "add", str(VAULT_DIR.relative_to(REPO_ROOT))],
            cwd=REPO_ROOT,
            check=True,
        )

    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO_ROOT)
    if diff.returncode == 0:
        print("No state changes to commit")
        return

    date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    msg = f"chore: update feed state [{date_str}]"
    subprocess.run(["git", "commit", "-m", msg], cwd=REPO_ROOT, check=True, env=git_env)
    subprocess.run(["git", "push"], cwd=REPO_ROOT, check=True)
    print("Committed and pushed feed state")


def main() -> None:
    missing = [
        rel_path for rel_path in TRACKED_PATHS if not (REPO_ROOT / rel_path).exists()
    ]
    if missing:
        print(f"Missing required state files: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    git_commit()


if __name__ == "__main__":
    main()
