---
layout: post
title: "The Good, the Bad and the Ugly in Cybersecurity – Week 18"
date: 2026-05-01 13:00:13 +0300
categories: [RSS]
tags: [supply-chain, npm, sap, oidc, malware]
toc: true
---

This weekly roundup is mostly news-oriented, but its strongest technical section covers the 'Mini Shai-Hulud' supply-chain attack against SAP-related npm packages such as `@cap-js/attachments`, `@cap-js/openapi`, `@cap-js/sqlite`, and `cds-dk`. According to the cited reporting, the attackers abused a gap in npm OIDC trusted publishing to mint a publish-capable token, push poisoned package versions, and execute a `preinstall` bootstrapper that downloads a platform-specific Bun binary. The payload steals developer credentials, GitHub and npm tokens, GitHub Actions secrets, cloud secrets, and browser-stored passwords, then attempts persistence by planting malicious files into Claude Code and VS Code-related settings so the malware re-executes when repositories are opened. The article also notes AES-256-GCM encryption for exfiltrated data, use of GitHub repositories on the victim's own account as exfil/C2 infrastructure, and a Russia-locale kill switch that may link the campaign to TeamPCP.

[Read original article](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-18-7/){: .btn .btn-primary }
