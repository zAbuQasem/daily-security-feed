---
layout: post
title: "Is Cyber missing the Marque?"
date: 2026-08-20 18:00:18 +0300
categories: [RSS]
tags: [malware, rootkit, ai, edr-bypass, threat-actor]
toc: true
---

Talos discovered UAT-10147, a Chinese-speaking cybercrime group integrating agentic AI into post-compromise operations to automate exploit generation, reconnaissance, and custom malware development. The group deploys SPECTRE, a cross-platform implant featuring a custom Linux kernel rootkit and Bring Your Own Vulnerable Driver (BYOVD) capabilities designed to completely evade endpoint detection and response (EDR) solutions. UAT-10147 exploits one-day vulnerabilities in internet-facing applications (Zimbra, Nacos, Telerik UI) and leverages stolen ASP.NET MachineKeys to perform ViewState deserialization attacks, using HTTP 500 errors to silently validate exploit paths. The use of agentic AI to scale complex attacks with dynamic troubleshooting and kernel-level evasion techniques represents a significant escalation in offensive capabilities. Defenders must prioritize patching one-days, blocking vulnerable drivers, and monitoring for anomalous HTTP 500 errors to counter this threat.

[Read original article](https://blog.talosintelligence.com/is-cyber-missing-the-marque/){: .btn .btn-primary }
