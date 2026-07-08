---
layout: post
title: "Vidar Stealer Unmasked: Code Signing Abuse, Go Loaders and File Inflation"
date: 2026-07-07 22:00:21 +0300
categories: [RSS]
tags: [malware, supply-chain, code-signing, evasion, credential-theft]
toc: true
---

Unit 42 analyzed a financially motivated April 2026 campaign distributing Vidar stealer and XMRig miner via malvertising targeting cracked software downloads. The 43 loader samples leverage the Factory-v3 MaaS builder framework and employ multiple evasion techniques: forged Authenticode certificates impersonating JustWatch GmbH, DLL search-order hijacking by mimicking MpClient.dll exports, and file-size inflation to 491 MB to bypass sandbox enforcement limits. Malware analysis reveals the loaders use custom Go 1.25.9 with anti-forensics measures (zeroed PE timestamps, obfuscated type names, kernel32-only imports) and come in clusters including x64/x86 variants, with the same Factory-v3 infrastructure also supporting concurrent Lumma stealer operations. The campaign targets U.S. and EU consumers and SMBs, with infected systems losing browser credentials, cookies, crypto wallets, and CPU resources to Monero mining.

[Read original article](https://unit42.paloaltonetworks.com/vidar-stealer-xmrig-miner-campaign-analysis/){: .btn .btn-primary }
