---
layout: post
title: "Dialing for Data: Inside the Com’s High-Profile Heists"
date: 2026-11-20 22:00:25 +0300
categories: [RSS]
tags: [threat-intel, vishing, aitm, extortion, cloud]
toc: true
---

Unit 42 tracks multiple Com-affiliated threat actors—including newly identified clusters Vortex (CL-CRI-1264) and Cinder (CL-CRI-1274)—conducting coordinated vishing attacks against healthcare, financial services, and legal organizations. Attackers establish initial access via voice social engineering, deploy adversary-in-the-middle (AiTM) proxies to intercept credentials and MFA approvals in real time, then automate data exfiltration from Microsoft 365 using Python scripts (targeting mailbox, OneDrive, SharePoint). Key tactics include immediate MFA device enrollment for persistence, session token replay to bypass Duo MFA re-prompting, and extortion via compromised internal channels (Teams, email) directing victims to Tor-hosted negotiation sites. The report attributes activity to multiple named actors (Bling Libra/ShinyHunters, Redact, Pink, Falcon, Helix) with overlaps to Google-tracked UNC6671, includes infrastructure observables and file hashes, and details a malicious browser extension used in related campaigns.

[Read original article](https://unit42.paloaltonetworks.com/com-affiliate-vishing-attacks/){: .btn .btn-primary }
