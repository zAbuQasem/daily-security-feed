---
layout: post
title: "Edge Infrastructure Under Siege: What Two Independent Datasets Reveal About Who’s Exploiting Your Perimeter"
date: 2026-08-26 12:59:22 +0300
categories: [RSS]
tags: [cve, threat-intelligence, infrastructure, remediation]
toc: true
---

A joint Tenable-SentinelOne analysis of 93 CVEs reveals that state-sponsored actors (China, Russia, DPRK, Iran) and ransomware operators structurally converge on the same edge infrastructure vulnerabilities, with 79% vendor-level overlap despite minimal CVE-level correlation. Twelve CVEs show confirmed multi-nexus attribution (e.g., CVE-2023-42793 exploited by both APT29 and Lazarus; CVE-2024-3400 by China-nexus and ransomware groups). F5 products show highest exposure at 54% of customers running exploited CVEs; Citrix exhibits slowest remediation at 461-day median time to patch. High-priority CVEs face a statistically significant 24-day remediation delay—driven by edge device complexity: firmware-level updates requiring manual validation, lack of endpoint agents, and change management overhead. The finding emphasizes that patching current CVEs does not remove the persistent vendor attack surface, and that defending against one actor category requires defending against all because the exploitation target is shared.

[Read original article](https://www.sentinelone.com/blog/what-two-independent-datasets-reveal-about-whos-exploiting-your-perimeter/){: .btn .btn-primary }
