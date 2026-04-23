---
layout: post
title: "IR Trends Q1 2026: Phishing reemerges as top initial access vector, as attacks targeting public administration persist"
date: 2026-04-23 03:12:31 +0300
categories: [RSS]
tags: [phishing, github, azure, supply-chain, ransomware]
toc: true
---

Cisco Talos' Q1 2026 IR report highlights phishing as the top initial access vector again, including a case where attackers used Softr's AI-driven app builder to generate credential-harvesting pages for Microsoft Exchange and Outlook Web Access and route captured data to external stores such as Google Sheets without writing code. The strongest technical case study covers a GitHub Personal Access Token exposed on a public website; attackers then used TruffleHog to enumerate secrets across thousands of repositories, pivoted into Azure cloud storage via discovered client secrets and Microsoft Graph API calls, and attempted to seed repositories with code that would exfiltrate newly committed secrets, showing a practical dev-environment and supply-chain intrusion path. Talos also describes a pre-Rhysida intrusion that used Gootloader-associated tooling and likely MeowBackConn proxy DLLs, with exposed WinRM, over-privileged service accounts, logging gaps, and RDP-based lateral movement enabling the operation. While the article is a trends report rather than a single deep exploit write-up, it provides concrete attacker tradecraft around AI-assisted phishing, PAT leakage, cloud API abuse, and pre-ransomware activity that is useful for defenders.

[Read original article](https://blog.talosintelligence.com/ir-trends-q1-2026/){: .btn .btn-primary }
