---
layout: post
title: "CL-STA-1062 Targets Southeast Asian Governments and Critical Infrastructure"
date: 2026-06-25 22:00:52 +0300
categories: [RSS]
tags: [malware, backdoor, critical-infrastructure, apt, threat-intelligence]
toc: true
---

Palo Alto Networks Unit 42 reports on CL-STA-1062 (also tracked as UAT-7237), a Chinese-speaking threat actor group targeting Southeast Asian government entities and critical energy infrastructure since at least March 2022. The group's attack chain begins with ASPX web shell deployment via web application exploitation, followed by system enumeration and reconnaissance conducted through curl and PowerShell commands. Beyond open-source tools (SoftEther VPN, Mimikatz, yuze, VNT), the attackers introduced TinyRCT, a previously undocumented custom backdoor supporting arbitrary command execution, file enumeration and exfiltration, screen capture, and a self-destruct mechanism. Between October and December 2025, the group compromised at least ten organizations across Southeast Asia, with focused campaigns on critical energy infrastructure entities where they scanned for vulnerabilities and deployed malicious payloads—often disguising tunneling tools as legitimate binaries like vmtools.exe.

[Read original article](https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/){: .btn .btn-primary }
