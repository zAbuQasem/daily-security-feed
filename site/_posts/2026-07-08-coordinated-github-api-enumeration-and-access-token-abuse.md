---
layout: post
title: "Coordinated GitHub API enumeration and access token abuse"
date: 2026-07-08 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, token-abuse, detection, api-abuse]
toc: true
---

Datadog Security Research has identified sustained, coordinated campaigns systematically enumerating GitHub organizations and repositories via the GitHub API, using dormant "ghost" accounts reactivated years later alongside compromised OAuth tokens and personal access tokens (PATs). Attackers leverage public GraphQL endpoints and REST routes to map organization structures, members, and project relationships without generating authentication failures, then escalate to cloning private repositories using exfiltrated credentials. Detection requires monitoring GitHub audit logs for suspicious user agents (e.g., 'GitHub-Scraper-Tool', 'repo-dumper'), programmatic access types, and successful API actions (`api.request`, `git.clone`) against private repositories. The post provides defensive queries and indicators for hunting this activity, which has been active since October 2025 across multiple organizations with confirmed private data exfiltration.

[Read original article](https://securitylabs.datadoghq.com/articles/coordinated-github-api-enumeration/){: .btn .btn-primary }
