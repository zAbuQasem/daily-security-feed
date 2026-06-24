---
layout: post
title: "OpenClaw’s Skill Marketplace and the Emerging AI Supply Chain Threat"
date: 2026-06-23 22:00:51 +0300
categories: [RSS]
tags: [supply-chain, ai-agent, malware, c2, evasion]
toc: true
---

Unit 42 researchers identified five unblocked malicious skills on ClawHub, OpenClaw's AI agent skill marketplace, despite VirusTotal and ClawScan screening. Malicious skills exploit semantic instruction hijacking to bypass technical constraints, leveraging agents' native access to filesystems, shells, and credential managers without requiring conventional exploits. The five skills represent three threat categories: infostealers connecting to C2 infrastructure, an evasion skill with inflated file size to defeat scanners, and novel agentic threats (affiliate injection and front-running) used for financial gain. Early findings from February 2026 showed ~17% of skills carried malicious payloads, with dropper infrastructure using Base64-encoded curl-pipe-bash, platform-specific delivery via paste sites, cron persistence, and Telegram exfiltration channels. The underlying threat model differs fundamentally from traditional package registries like npm/PyPI due to lack of isolation between skill logic and agent authority, enabling complete compromise of the agent's authenticated sessions.

[Read original article](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/){: .btn .btn-primary }
