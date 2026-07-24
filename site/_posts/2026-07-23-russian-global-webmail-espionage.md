---
layout: post
title: "Russian Global Webmail Espionage"
date: 2026-07-23 14:10:53 +0300
categories: [RSS]
tags: [phishing, webmail, cve, espionage, zero-click]
toc: true
---

Unit 42 documents CL-STA-1114, a Russian state-sponsored espionage campaign exploiting CVE-2025-66376 in Zimbra Collaboration Suite via zero-click phishing emails. The attack delivers obfuscated, Base64-encoded JavaScript within HTML attachments or message bodies; an invisible SVG element automatically decodes and injects the payload without user interaction. Once executed, the JavaScript exfiltrates CSRF tokens, login credentials, 2FA scratch codes, system details, and 90 days of email and search history to hardcoded C2 servers. The campaign, active since July 2025, targets government, defense, transportation, and financial organizations across NATO member states, Ukraine, CIS countries, and Africa; Unit 42 identifies 9+ C2 IPs and domains averaging 35 days active each, with comprehensive IoCs provided for detection.

[Read original article](https://unit42.paloaltonetworks.com/russian-webmail-espionage/){: .btn .btn-primary }
