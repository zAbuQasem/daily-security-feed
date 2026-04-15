# Daily Security Feed

AI-curated security research feed — auto-updated daily, deployed to GitHub Pages.

Fork this repo, add your feeds, and get your own daily security feed at `https://<you>.github.io/daily-security-feed/` with optional Discord/Slack notifications.

## Quick start

1. **Fork** this repository.
2. Delete `state/processed_urls.json` — it contains the upstream's seen URLs and will prevent your fork from fetching articles that were already processed here.
3. Enable **GitHub Pages** in your fork: `Settings → Pages → Source → GitHub Actions`.
4. Edit `feeds/feeds.yaml` with the RSS/Atom feeds you want to follow.
5. Add the required [secrets and variables](#setup).
6. Create a Copilot PAT by following [Copilot token setup](#copilot-token-setup).
7. Open **Actions** and run `daily-security-feed-bot` manually to seed the first batch.
8. Your site will be live at `https://<you>.github.io/daily-security-feed/` after the first run.

## How it works

```mermaid
flowchart TD
    A["⏰ Cronjob — Daily at 05:00 Asia/Amman · UTC+3"]:::trigger
    B["Fetch & scrape new articles from RSS feeds"]:::fetch
    C["Filter & classify with AI keep research, assign priority"]:::classify
    D["Write markdown posts to site/_posts/"]:::write
    E["Commit & push → Jekyll rebuilds GitHub Pages"]:::persist
    F["Post digest to Discord"]:::notify
    G["Post digest to Slack"]:::notify
    H(["⚠ On failure — send error alert to Discord + Slack"]):::failure
    I(["📅 Monthly — remind to rotate secrets"]):::monthly

    A --> B --> C --> D --> E
    E --> F & G
    E -.-> H
    A -.-> I

    classDef trigger  fill:#1f3a5f,stroke:#3b82f6,color:#e2e8f0
    classDef fetch    fill:#1a3a2a,stroke:#22c55e,color:#e2e8f0
    classDef classify fill:#2a1a3a,stroke:#a855f7,color:#e2e8f0
    classDef write    fill:#3a2a1a,stroke:#f97316,color:#e2e8f0
    classDef persist  fill:#1a2a3a,stroke:#38bdf8,color:#e2e8f0
    classDef notify   fill:#3a1a1a,stroke:#ef4444,color:#e2e8f0
    classDef failure  fill:#1a1a1a,stroke:#f87171,color:#f87171,stroke-dasharray:4 4
    classDef monthly  fill:#1a1a1a,stroke:#fbbf24,color:#fbbf24,stroke-dasharray:4 4
```

## Setup

**Secrets** (`Settings → Secrets and variables → Actions → Secrets`):

| Secret | Required | Description |
| --- | --- | --- |
| `COPILOT_TOKEN` | Yes | Fine-grained PAT with **Copilot Requests: Read** permission |
| `DISCORD_WEBHOOK_URL` | No | Discord channel webhook for notifications |
| `SLACK_WEBHOOK_URL` | No | Slack incoming webhook for notifications |

**Variables** (`Settings → Secrets and variables → Actions → Variables`):

| Variable | Example | Description |
| --- | --- | --- |
| `AI_MODEL` | `claude-sonnet-4-6` | AI model used by the Copilot classifier |
| `NOTIFY_CHANNELS` | `both`, `discord`, or `slack` | Where to send notifications (default: `both`) |
| `SKIP_CLASSIFY` | `true` or `false` | Skip AI classification — publish all fetched articles (default: `false`) |
| `PAGES_URL` | `https://you.github.io/daily-security-feed/` | GitHub Pages site URL — included as a "Browse feed" link in Discord and Slack notifications |

> [!NOTE]
> Requires an active GitHub Copilot Pro subscription on the repo owner's account.

## Copilot token setup

Create `COPILOT_TOKEN` as a fine-grained personal access token:

1. Go to GitHub `Settings` → `Developer settings` → `Fine-grained personal access tokens`.
2. Create a token for the account that owns the Copilot entitlement used by this pipeline.
3. Grant the minimum permission required: `Copilot Requests: Read`.
4. Set a short expiration date and store the token only in `Repo → Settings → Secrets and variables → Actions` as `COPILOT_TOKEN`.
5. Re-run the workflow after adding it to verify classification works.

Do not use a classic PAT here. Keep the token scoped only for Copilot requests.

## Customization

| What | Where |
| --- | --- |
| Feed list | `feeds/feeds.yaml` — add/remove RSS/Atom URLs |
| Articles per run | `MAX_ARTICLES` env var (workflow default: 30) |
| Entries per feed | `ENTRIES_PER_FEED` env var (default: 5) |
| AI system prompt | `prompts/classify.md` |
| Site theme | `site/_config.yml` and `site/_layouts/` |

## Security warning

Feed content is untrusted input. A malicious article can include indirect prompt-injection text that tries to coerce the classifier into revealing secrets or following attacker instructions.

1. Keep `COPILOT_TOKEN`, `DISCORD_WEBHOOK_URL`, and `SLACK_WEBHOOK_URL` only in GitHub Actions secrets.
2. Use least-privilege credentials only. Do not reuse repo-admin, org-admin, or broadly scoped API tokens.
3. Rotate the Copilot PAT and notification webhooks every month.
4. Re-run the pipeline after rotation to verify the new secrets work.

## Security disclaimer

This project processes untrusted RSS/Atom content and passes it to an AI classifier. We implement multiple layers of defense against indirect prompt injection:

- **Pre-classifier scanning** (`pipeline/injection_scanner.py`) — a heuristic engine that normalises text through 8 layers (HTML entities, URL encoding, Unicode NFKD, zero-width characters, homoglyphs, leetspeak, base64 decoding) and matches against injection patterns in 14 languages before content ever reaches the AI. Articles that match are quarantined and never sent to Copilot.
- **In-prompt defenses** (`prompts/classify.md`) — explicit instructions telling the AI to treat all article content as data, never as instructions.
- **Output validation** — JSON extraction ignores non-JSON output from the classifier.
- **Least-privilege credentials** — the Copilot PAT is scoped to `Copilot Requests: Read` only.

> [!CAUTION]
> These defenses reduce risk but **do not guarantee complete protection**. Prompt injection is an open research problem with no known universal solution. By using this project, you acknowledge that:
>
> - No heuristic scanner can catch every possible injection technique. Adversaries may find bypasses.
> - AI models can behave unpredictably when processing adversarial input regardless of system prompt hardening.
> - The maintainers of this project provide these security measures on a best-effort basis and **accept no liability** for any damage, data exposure, credential leakage, or other harm arising from the use of this software.
> - You are responsible for securing your own secrets, tokens, and infrastructure.
>
> Use at your own risk. Review the code, scope your credentials tightly, rotate secrets regularly, and monitor your pipeline runs.

## Author & credits

Built and maintained by **Zeyad AbuLaban** ([@zAbuQasem](https://github.com/zAbuQasem) · [LinkedIn](https://www.linkedin.com/in/zeyad-abulaban/)).

If you fork or adapt this project, a link back is appreciated but not required.
