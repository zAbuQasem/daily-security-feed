# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Commands

```bash
# Install dependencies (Python + Node)
uv sync
npm install -g defuddle
npm install -g @github/copilot   # required by classify.py

# Run the pipeline step by step
MAX_ARTICLES=5 uv run python pipeline/fetch_feeds.py
COPILOT_GITHUB_TOKEN=<fine-grained-pat> uv run python pipeline/classify.py
uv run python pipeline/write_vault.py
uv run python pipeline/persist_state.py
```

There are no tests. The staging files (`state/staged_articles.json`, `state/classified_articles.json`) are the main debugging surface — run steps individually and inspect them between runs.

## Architecture

Pipeline code lives in `pipeline/`, Jekyll site files in `site/`. The pipeline runs as sequential Python modules, each writing a file consumed by the next:

```text
fetch_feeds.py      →  state/staged_articles.json
classify.py         →  state/classified_articles.json
write_vault.py      →  site/_posts/YYYY-MM-DD-slug.md  (Jekyll posts)
persist_state.py    →  git push (state/processed_urls.json + logs/urls.txt + site/_posts)
                        → triggers pages.yml → Jekyll rebuilds GitHub Pages
notify_discord.py   →  Discord webhooks
notify_slack.py     →  Slack webhooks
```

**fetch_feeds.py** parses `feeds/feeds.yaml`, fetches up to `ENTRIES_PER_FEED` recent entries per feed via `feedparser` using 30 concurrent workers, skips URLs already in `state/processed_urls.json`, then calls `defuddle parse --json --md <url>` as a subprocess for each new article. It can filter by publication age with `FEED_MAX_AGE_DAYS` (default 1, set to 0 to disable). All candidate URLs are marked seen during scanning, so `processed_urls.json` grows even for capped/failed fetches. Articles shorter than 200 chars are discarded but still marked seen. Content is capped at 8000 chars. Caps at `MAX_ARTICLES` (default 100 in code; workflow default is 15). Appends processed URLs to `logs/urls.txt` with `[YYYY-MM-DD]` prefix.

**classify.py** calls the `@github/copilot` npm CLI as a subprocess (`copilot --prompt "..." --allow-all-tools --allow-all-paths`), one process per article with a 120s timeout. Auth is via `COPILOT_GITHUB_TOKEN` env var — must be a **fine-grained PAT with Copilot Requests: Read permission** (classic `ghp_` PATs are rejected). Prompt text is loaded from `prompts/classify.md`. The classifier returns structured JSON with `category`, `tags`, `priority`, and `summary`. Only `research` articles are persisted to `state/classified_articles.json`. JSON is extracted by finding the first `{` and last `}` in stdout (Copilot CLI emits preamble before the JSON). When `SKIP_CLASSIFY=true`, AI classification is bypassed entirely — all fetched articles are published as research with priority 2, no tags, and no summary. This removes the Copilot dependency for users who just want an unfiltered feed.

**write_vault.py** reads `state/classified_articles.json` and writes Jekyll-compatible markdown posts to `site/_posts/` with frontmatter (`layout`, `title`, `source_url`, `date`, `priority`, `tags`, `feed`) and the AI summary body. Files are named `YYYY-MM-DD-slug.md`. Creator tags are always appended. Note: the frontmatter key is `source_url` (not `url`) to avoid collision with Jekyll's reserved `page.url` which holds the post permalink.

**persist_state.py** commits `state/processed_urls.json`, `logs/urls.txt`, and `site/_posts/` in a single commit by `github-actions[bot]`.

**notify_discord.py** sends one daily feed embed on success (research only), sorted by priority, including creator info. On failure, it sends a red embed with failed step and run link.

**notify_slack.py** sends a Slack webhook message using Block Kit on success or failure. Success groups research items by priority (critical/solid/low) with colored emoji indicators, stats summary, and footer links to the Pages site and GitHub Actions run. Failure shows the failed step with a "View Logs" button. Both include creator links.

**remind_rotate.py** sends a monthly Discord/Slack reminder to rotate `COPILOT_TOKEN`, plus a warning that untrusted feed content can attempt indirect prompt injection and secret exfiltration.

## Priority Field

Classifier assigns `priority` 1–3 to each research article:

- **1** — High-signal: cloud/CI-CD attacks, supply chain, PortSwigger/Project Zero posts, novel techniques
- **2** — Mid-signal: CVE write-ups, parser bugs, less-known researchers
- **3** — Low urgency: useful but less immediately actionable research

Priority controls sort order within each section in the Discord feed embed.

## Workflows

| Workflow | Schedule | Purpose |
| --- | --- | --- |
| `security_feed.yml` (`daily-security-feed-bot`) | 05:00 Amman daily | Main pipeline (fetch → classify → write vault → persist state → Discord/Slack notify) |
| `pages.yml` (`deploy-github-pages`) | on push to main | Build Jekyll site and deploy to GitHub Pages |
| `secret_rotation_reminder.yml` (`daily-security-feed-bot-secret-rotation-reminder`) | 1st of month, 09:00 Amman | Discord/Slack reminder to rotate `COPILOT_TOKEN` |

## Configuration

| What | Where |
| --- | --- |
| Feed list | `feeds/feeds.yaml` — add/remove URLs freely |
| Articles per run cap | `MAX_ARTICLES` env var (code default: 100; workflow default: 15) |
| Feed entries per source | `ENTRIES_PER_FEED` env var (code default: 5) |
| Feed freshness filter | `FEED_MAX_AGE_DAYS` env var (default: 1, set `0` to disable) |
| Seen URLs | `state/processed_urls.json` — committed after every run; delete entries to reprocess |
| URL audit log | `logs/urls.txt` — append-only, grep by `[YYYY-MM-DD]` to filter by date |
| Prompt template | `prompts/classify.md` |
| Copilot auth | `COPILOT_TOKEN` secret — fine-grained PAT with **Copilot Requests: Read** permission |
| Discord webhook | `DISCORD_WEBHOOK_URL` secret |
| Slack webhook | `SLACK_WEBHOOK_URL` secret |
| AI model | `AI_MODEL` repo variable (e.g. `claude-sonnet-4-6`) |
| Skip classification | `SKIP_CLASSIFY` repo variable (`true` to bypass AI and publish all articles unfiltered) |
| Notification channels | `NOTIFY_CHANNELS` repo variable (`both`, `discord`, or `slack`) |
| Pages URL | `PAGES_URL` env var (optional, used by Slack "Browse feed" link) |
| Creator branding | Hardcoded in `pipeline/config.py` (`GITHUB_HANDLE`, `LINKEDIN_URL`) |

## Security Guidance

Requires an active GitHub Copilot Pro subscription on the repository owner's account (not needed when `SKIP_CLASSIFY=true`).

Create `COPILOT_TOKEN` as a fine-grained PAT with only `Copilot Requests: Read`. Store it only in GitHub Actions secrets and rotate it monthly.

This repo treats feed content as untrusted input. A malicious RSS item can contain indirect prompt-injection content aimed at coercing the AI into leaking tokens or webhook URLs. Keep secrets least-privileged, avoid broader PAT scopes, and rotate all related secrets each month.
