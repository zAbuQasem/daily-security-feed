---
layout: post
title: "Atomic macOS (AMOS) Stealer Activity"
date: 2026-09-16 10:00:06 +0300
categories: [RSS]
tags: [malware, macos, infostealer, indicators, persistence]
toc: true
---

AMOS stealer is an active macOS information stealer distributed via fake toolkit installation pages using copy/paste terminal commands. The infection chain involves chained Zsh scripts with Base64/GZIP-encoded payloads that drop Mach-O binaries into Library/Application Support directories, establishing persistence through shell scripts and plist files. The malware exfiltrates browser credentials, cryptocurrency wallet data (Binance, TonKeeper), cloud configurations (AWS, Docker, gcloud), and session history via HTTP POST to C2 infrastructure. Analysis of an August 2026 sample provides specific IOCs including malicious domains, file hashes, and C2 IP addresses (161.35.146.120).

[Read original article](https://unit42.paloaltonetworks.com/atomic-macos-amos-stealer-activity/){: .btn .btn-primary }
