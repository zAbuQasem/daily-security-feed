---
layout: post
title: "OptinMonster supply chain attack hits 1.2 million sites"
date: 2026-06-13 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, wordpress, rce, backdoor, malware]
toc: true
---

Sansec discovered an active supply-chain attack injecting malicious JavaScript into Awesome Motive's CDN-served plugin files (OptinMonster, TrustPulse, PushEngage), affecting 1.2+ million WordPress sites. The payload detects logged-in admins via WordPress cookies and context detection, then creates backdoor admin accounts using four fallback methods (form submission, AJAX, REST API, hidden iframe) while exfiltrating credentials via XOR encryption to a C2 domain (tidio.cc). The attacker silently installs a self-hiding plugin disguised as system tools ("Database Optimizer", "Content Delivery Helper") that exposes unauthenticated code execution endpoints: a file manager shell and an eval endpoint running attacker-supplied base64 code. The malware remains active on PushEngage as of June 13, 2026, with indicators including the XOR key (jX9kM2nP4qR6sT8v), rogue accounts (developer_api1, dev_* variants), and hidden plugin artifacts on disk.

[Read original article](https://sansec.io/research/optinmonster-supply-chain-attack){: .btn .btn-primary }
