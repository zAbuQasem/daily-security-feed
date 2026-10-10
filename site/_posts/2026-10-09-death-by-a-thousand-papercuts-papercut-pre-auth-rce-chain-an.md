---
layout: post
title: "Death By A Thousand PaperCuts (PaperCut Pre-Auth RCE Chain and Patch Bypasses WT-2026-0141-0144/CVE-2026-82077/CVE-2026-82078/CVE-2026-81578)"
date: 2026-10-09 17:31:14 +0300
categories: [RSS]
tags: [rce, auth-bypass, 0-day, patch-bypass, infrastructure]
toc: true
---

WatchTowr Labs disclosed a pre-auth RCE chain in PaperCut NG (v26.0.3) actively exploited in the wild, combining CVE-2026-81578 (authentication bypass) with CVE-2026-82078 (post-auth RCE). Post-patch analysis uncovered four additional patch-bypass vulnerabilities (WT-2026-0141-0144), including CVE-2026-82077, a second independent post-auth RCE discovered in 26.0.4-PO build 76508. The vulnerability affects print management infrastructure deployed across schools, universities, healthcare, and government agencies. Three patching rounds (v26.0.4, 26.0.4-PO build 76508, v26.0.5) were required to remediate all bypasses, demonstrating the persistence of complex exploitation paths under rapid remediation cycles.

[Read original article](https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/){: .btn .btn-primary }
