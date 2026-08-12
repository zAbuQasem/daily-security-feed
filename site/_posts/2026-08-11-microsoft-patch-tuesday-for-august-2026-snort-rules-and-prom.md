---
layout: post
title: "Microsoft Patch Tuesday for August 2026 — Snort rules and prominent vulnerabilities"
date: 2026-08-11 22:21:02 +0300
categories: [RSS]
tags: [rce, windows, azure, cve, patch-tuesday]
toc: true
---

Microsoft's August 2026 Patch Tuesday addresses 421 vulnerabilities including 62 critical, with at least one already exploited in the wild. High-impact RCEs include CVE-2026-62893 (Windows DHCP Server heap overflow, CVSS 9.8), CVE-2026-65665 (SharePoint deserialization, CVSS 8.8), and CVE-2026-62823 (DHCP Server heap overflow, CVSS 8.8). Additionally, two Azure service vulnerabilities with CVSS 9.4–9.9 affect AKS and SRE Agent. Nine Office RCEs involve buffer overflows and integer overflows across Excel, Word, and Graphics Component. Infrastructure operators and Office users should prioritize patching network-facing services (DHCP, TFTP, SharePoint) and Azure deployments.

[Read original article](https://blog.talosintelligence.com/microsoft-patch-tuesday-for-august-2026/){: .btn .btn-primary }
