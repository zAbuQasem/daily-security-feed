---
layout: post
title: "No Manners Here: The Ruthless Rise of The Gentlemen Ransomware"
date: 2026-07-10 22:00:39 +0300
categories: [RSS]
tags: [ransomware, raas, malware, threat-intelligence, edr-evasion]
toc: true
---

The Gentlemen is a Ransomware-as-a-Service operation (tracked as Storm-2697 by Microsoft) active since July 2025, likely evolved from ArmCorp affiliate activity under Qilin. The group operates ~20 operators and has rapidly become the second most active RaaS program in 2026, with 580 claimed victims across 77 countries and 6x growth in victim count. They deploy polyglot encryptors written in C and Go, use custom Go-based backdoors, employ the GentleKiller EDR-killer framework, and leverage suspected 0-day exploits for defense evasion. Initial access vectors include exploitation of CVE-2024-55591 (FortiOS/FortiProxy), edge device brute force, stolen credentials, and IAB collaboration; lateral movement relies on SMB propagation and internal reconnaissance tools like Advanced IP Scanner. The unusually high 90% affiliate payout structure (vs. typical 70–80% RaaS rates) has accelerated their recruitment and operational scaling, with June 2026 recording 117 claimed victims—their highest monthly total.

[Read original article](https://unit42.paloaltonetworks.com/the-gentlemen-ransomware/){: .btn .btn-primary }
