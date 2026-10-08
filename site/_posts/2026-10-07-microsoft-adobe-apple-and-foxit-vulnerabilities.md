---
layout: post
title: "Microsoft, Adobe, Apple, and Foxit vulnerabilities"
date: 2026-10-07 19:27:08 +0300
categories: [RSS]
tags: [cve, rce, privilege-escalation, kernel, pdf]
toc: true
---

Cisco Talos disclosed seven patched vulnerabilities across major vendors. Windows Cloud Files Mini Filter Driver contains use-after-free and type confusion flaws (CVE-2026-58613, CVE-2026-80093) enabling privilege escalation via malicious Cloud Filter API sequences. Foxit Reader has critical JavaScript-related PDF vulnerabilities: code execution in checkbox widget processing (CVE-2026-57256) and use-after-free in Array handling (CVE-2026-91799) allowing arbitrary code execution. Microsoft kernel drivers (NETIO.sys, tcpip.sys) contain out-of-bounds pointer/read vulnerabilities enabling information disclosure, Adobe Photoshop Setup has privilege escalation through file replacement, and macOS CoreWLAN has information disclosure via API abuse. All patches available from vendors.

[Read original article](https://blog.talosintelligence.com/microsoft-adobe-apple-and-foxit-vulnerabilities/){: .btn .btn-primary }
