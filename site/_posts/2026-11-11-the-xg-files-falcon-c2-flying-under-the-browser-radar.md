---
layout: post
title: "The XG Files: Falcon C2 Flying Under The (Browser) Radar"
date: 2026-11-11 15:00:23 +0300
categories: [RSS]
tags: [c2, malware, browser, javascript, credential-theft]
toc: true
---

Unit 42 identified Falcon, a sophisticated browser-based C2 framework that compromises webmail portals and government web applications through injected malicious JavaScript. The framework operates entirely within the browser, using XOR-obfuscated JavaScript with RSA-encrypted session keys, and employs OPSEC mechanisms including F9-triggered hidden login panels and Tetris/Snake game overlays to evade detection. Attackers use Falcon to sideload malicious Chrome extensions and steal credentials, emails, session cookies, and communications, while delivering a secondary implant called Antino that uses Microsoft OneDrive as a C2 channel. The framework shares extensive technical overlap with PeckBirdy, including identical URL structures, payload delivery sequences, and Baidu-mimicking session ID naming conventions (Hm_lvt_ prefix), indicating they represent variants of the same core framework. Active campaigns between March-May 2026 targeted government ministries (foreign affairs, defense, interior) and law enforcement agencies across Southeast Asia and the Middle East, suggesting strategic intelligence collection operations.

[Read original article](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/){: .btn .btn-primary }
