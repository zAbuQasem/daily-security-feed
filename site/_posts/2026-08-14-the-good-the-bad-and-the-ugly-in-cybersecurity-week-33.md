---
layout: post
title: "The Good, the Bad and the Ugly in Cybersecurity – Week 33"
date: 2026-08-14 15:21:37 +0300
categories: [RSS]
tags: [ransomware, 0-day, critical-infrastructure, privilege-escalation, threat-intelligence]
toc: true
---

A SentinelOne weekly digest covering three threat landscapes. Gunra ransomware, derived from leaked Conti source code, actively targets critical infrastructure (public health, finance, government) in Australia and East Asia, exploiting CVE-2024-55591 and CVE-2025-24472 in FortiOS/FortiProxy to establish initial access, deploying double-extortion via RaaS program "Golden Community" with lateral movement via Impacket and Salsa20/ChaCha20 encryption; notably, the Linux variant contains a cryptographic flaw enabling recovery without ransom payment. ShieldBreak, a zero-day Microsoft Defender bypass released by researcher 'Nightmare Eclipse', chains user-mode callback hooks and Object Manager symbolic links to hijack cloud-hydration scans, achieving 100% privilege escalation to SYSTEM on fully patched Windows 11 25H2 and Windows Server 2025 by planting a malicious DLL during cloud filter operations. Both threats represent active, high-impact exploitation against hardened systems.

[Read original article](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-33-8/){: .btn .btn-primary }
