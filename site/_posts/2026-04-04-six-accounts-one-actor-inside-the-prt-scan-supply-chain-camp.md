---
layout: post
title: "Six Accounts, One Actor: Inside the prt-scan Supply Chain Campaign"
source_url: https://www.wiz.io/blog/six-accounts-one-actor-inside-the-prt-scan-supply-chain-campaign
date: 2026-04-04
priority: 1
tags: [supply-chain, ci-cd, github-actions, pull_request_target, npm, github-zabuqasem, linkedin-zeyad-abulaban]
feed: https://www.wiz.io/feed/rss.xml
---

Wiz traces a multi-account supply chain campaign ('prt-scan') exploiting the GitHub Actions `pull_request_target` trigger — a dangerous workflow event that runs with write permissions and secrets access even when triggered from a fork. The actor operated six GitHub accounts, mirroring the earlier 'hackerbot-claw' campaign, confirming that AI-assisted abuse of this trigger is an emerging, repeatable threat pattern. Wiz's investigation attributes activity back three weeks before public detection, suggesting defenders are consistently behind on these campaign timelines. The `pull_request_target` primitive is dangerous because it allows attacker-controlled code in a fork to execute in the context of the base repository's privileged CI environment, enabling token theft, secrets exfiltration, and downstream supply chain compromise.
