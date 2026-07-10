---
layout: post
title: "WolfSSL, GeoVision, VTK vulnerabilities"
date: 2026-07-09 18:52:29 +0300
categories: [RSS]
tags: [memory-corruption, buffer-overflow, command-injection, privilege-escalation, cve]
toc: true
---

Cisco Talos disclosed 18 vulnerabilities across three products: three in WolfSSL (improper input validation, integer underflow), 14 advisories covering 37 CVEs in GeoVision surveillance and access control systems (including buffer overflows, command injection, privilege escalation, and XSS), and one heap-based buffer overflow in VTK-DICOM for medical imaging. The GeoVision vulnerabilities span critical attack vectors including OS command injection, stack/buffer overflows, privilege escalation, guessable session cookies, and insufficient encryption affecting security cameras and access control systems. All vulnerabilities have been patched and Snort detection rules are available.

[Read original article](https://blog.talosintelligence.com/wolfssl-vulnerabilities/){: .btn .btn-primary }
