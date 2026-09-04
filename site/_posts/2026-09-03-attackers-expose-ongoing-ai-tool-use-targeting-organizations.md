---
layout: post
title: "Attackers Expose Ongoing AI Tool Use Targeting Organizations in Latin America"
date: 2026-09-03 10:00:58 +0300
categories: [RSS]
tags: [threat-intel, latam, infrastructure, ai, rat]
toc: true
---

Palo Alto Networks Unit 42 describes two ongoing multi-stage campaigns targeting Mexican government/transportation and Brazilian financial sectors (CL-CRI-1131 and CL-CRI-1163). The Mexican campaign uses living-off-the-land techniques, iterative batch scripts, and volume shadow copy manipulation to exfiltrate SAM/NTDS.dit files, with infrastructure exposed via Let's Encrypt certificate rotation timelines and dynamic DNS domains. Both campaigns demonstrate a critical emerging pattern: threat actors independently integrating commercial LLMs (Claude, GPT-4.1) to orchestrate operations, troubleshoot execution failures, and generate tooling—including Go-based SOCKS5 proxies with AI-generated filenames. Overlapping SOCKS5 relay infrastructure and operational techniques signal a broader regional shift toward AI-augmented attack orchestration beyond isolated incidents.

[Read original article](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/){: .btn .btn-primary }
