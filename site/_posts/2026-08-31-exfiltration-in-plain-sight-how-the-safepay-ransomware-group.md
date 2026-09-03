---
layout: post
title: "Exfiltration in Plain Sight: How the SafePay Ransomware Group Abused OneDrive to Steal Data"
date: 2026-08-31 11:43:07 +0300
categories: [RSS]
tags: [ransomware, cloud, data-exfiltration, living-off-the-land, detection]
toc: true
---

SafePay ransomware operators evaded data exfiltration detection by installing the legitimate, Microsoft-signed OneDrive client on a compromised server and syncing staged RAR archives to an attacker-controlled Microsoft 365 tenant over standard HTTPS. After initial FTP exfiltration was blocked, this pivot leveraged trusted cloud infrastructure to bypass traditional controls that evaluate individual signals (destination, protocol, executable) rather than behavioral context. The incident began via FortiGate SSL VPN exploitation combined with a weak, unauthenticated administrative account, followed by domain admin escalation, lateral movement using native tools, and strategic targeting of backup infrastructure (Veeam). Detection requires correlating multiple evidence sources—browser history, ShellBag artifacts, network telemetry, and OneDrive sync folder behavior—to identify when a trusted service appears on unexpected hosts with unusual tenants and volumes, illustrating a critical shift in ransomware defense from signature-based controls to behavioral anomaly detection.

[Read original article](https://www.sygnia.co/blog/how-the-safepay-ransomware-group-abused-onedrive-to-steal-data/){: .btn .btn-primary }
