---
layout: post
title: "The Good, the Bad and the Ugly in Cybersecurity – Week 22"
date: 2026-05-29 14:38:21 +0300
categories: [RSS]
tags: [supply-chain, malware, credential-theft, npm, ci-cd]
toc: true
---

TrapDoor is a coordinated supply chain campaign that deployed 34+ malicious packages across npm, PyPI, and Crates.io targeting crypto, DeFi, Solana, and AI developer communities starting May 22, 2026. Each registry uses tailored attack vectors: npm uses postinstall hooks to deploy JS payloads that validate stolen AWS/GitHub tokens and attempt SSH lateral movement; Rust crates use build scripts with XOR-encrypted exfiltration to GitHub Gists; Python packages auto-execute on import to pull remote JS payloads from attacker-controlled domains. The campaign harvests SSH keys, cloud credentials, and crypto wallets, establishes persistence via cron/systemd/Git hooks, and notably targets AI coding assistants by poisoning files with hidden instructions to coerce AI tools into executing malicious scans and exfiltrating secrets. Threat actors are also submitting PRs with these poisoned files to major open-source AI projects, extending the blast radius beyond package registries.

[Read original article](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-22-7/){: .btn .btn-primary }
