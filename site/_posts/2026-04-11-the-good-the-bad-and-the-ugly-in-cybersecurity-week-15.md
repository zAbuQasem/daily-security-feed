---
layout: post
title: "The Good, the Bad and the Ugly in Cybersecurity – Week 15"
date: 2026-04-11 03:10:14 +0300
categories: [RSS]
tags: [dns-hijacking, macos, infostealer, ics, apt]
toc: true
---

This weekly roundup collects three technically relevant stories: a DOJ/FBI disruption of APT28 infrastructure that had compromised TP-Link routers, rewritten DNS settings, and returned forged records to insert adversary-controlled systems into targeted encrypted sessions; a new macOS ClickFix variant that abuses the `appplescript://` URL scheme to open Script Editor with pre-populated AppleScript and deliver AMOS/Atomic Stealer without the usual Terminal paste flow; and a joint advisory on Iranian actors targeting exposed Rockwell CompactLogix and Micro850 PLCs. The router operation is notable because the GRU campaign used stolen admin access and DNS resolver hijacking to selectively intercept credentials, tokens, email, and other traffic of intelligence value, and the FBI reportedly tested command sets against matching firmware before remotely restoring legitimate DNS behavior. The macOS campaign shows attackers adapting quickly to Apple’s Terminal paste warnings by shifting execution into Script Editor, while the payload still performs classic infostealer collection against browser data, wallet material, and password stores via hardcoded C2. The OT portion highlights hands-on exploitation of internet-facing PLCs over ports such as `44818`, `2222`, `102`, and `502`, with operators using tools like Studio 5000, deploying Dropbear SSH for persistence, extracting `.ACD` project files, and altering HMI/SCADA-visible process data to create operational disruption.

[Read original article](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-15-7/){: .btn .btn-primary }
