---
layout: post
title: "The Good, the Bad and the Ugly in Cybersecurity – Week 21"
date: 2026-05-22 15:08:13 +0300
categories: [RSS]
tags: [macos, infostealer, windows, privilege-escalation, defender]
toc: true
---

This weekly roundup combines several security items, but the most technically useful sections cover a new SHub "Reaper" macOS stealer variant and two actively exploited Microsoft Defender zero-days. The macOS malware uses fake WeChat and Miro installers on typosquatted domains, anti-analysis checks, and the `applescript://` URL scheme to launch Script Editor, pad malicious code with ASCII art, prompt for a user password to access Keychain data, steal browser and iCloud credentials, and exfiltrate files in 70MB ZIP chunks; it also hijacks crypto apps by replacing `app.asar`, clearing quarantine attributes, and applying ad hoc signing to bypass Gatekeeper. The Windows section summarizes CVE-2026-41091, a link-following flaw in the Microsoft Malware Protection Engine that can yield SYSTEM privileges, and CVE-2026-45498, a Defender Antimalware Platform bug that can force denial-of-service conditions on unpatched systems. The law-enforcement coverage on Operation Ramz, an infostealer operator case, and Europol's takedown of the "First VPN" service adds context on current cybercrime disruption, but the article is primarily a curated digest rather than a deep original technical write-up.

[Read original article](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-21-7/){: .btn .btn-primary }
