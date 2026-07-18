---
layout: post
title: "Three Steps to the Terminal: A Siemens ROX II Zero-Day Trilogy"
date: 2026-07-17 10:00:24 +0300
categories: [RSS]
tags: [zero-day, ot-security, privilege-escalation, rce, critical-infrastructure]
toc: true
---

Palo Alto Networks Unit 42 discovered three chained zero-day vulnerabilities in Siemens ROX II operational technology switches (CVE-2025-40948, CVE-2025-40947, CVE-2025-40949) that achieve full privilege escalation and persistent root access. CVE-2025-40948 exploits an insecure xz utility configuration to disclose arbitrary files including password hashes and cryptographic keys; CVE-2025-40947 leverages unsanitized input in the feature key validation function to inject commands executed with root privilege; CVE-2025-40949 allows authenticated attackers to inject malicious commands into the system's root cron table for persistence across reboots. The exploit chain transforms these critical network appliances—core to industrial control system connectivity—into platforms for sustained malicious activity. Siemens released firmware patches (V2.17.1) and corresponding security advisories; CVSS scores range from 6.8 to 9.1.

[Read original article](https://unit42.paloaltonetworks.com/siemens-rox-ii-zero-day-vulnerabilities/){: .btn .btn-primary }
