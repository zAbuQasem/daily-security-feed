---
layout: post
title: "Microsoft Patch Tuesday for July 2026 — Snort rules and prominent vulnerabilities"
date: 2026-07-14 20:27:33 +0300
categories: [RSS]
tags: [patch-tuesday, rce, windows, critical, exploitation]
toc: true
---

Microsoft's July 2026 Patch Tuesday addresses 622 vulnerabilities, including 57 critical issues (48 RCEs, 7 EoPs, 1 spoofing, 1 bypass). Two vulnerabilities are already exploited in the wild. The 11 RCEs rated "more likely" to exploit include heap buffer overflows in Windows DHCP Server (CVE-2026-50370, CVE-2026-50518), a use-after-free in DHCP client (CVE-2026-54128), buffer overflows in Media Foundation and MSMQ, a race condition in Windows Server Network driver (CVE-2026-56188), and deserialization vulnerabilities in SharePoint (CVE-2026-50522, CVE-2026-58644) and Dynamics NAV/365 (CVE-2026-55944). Additional critical RCEs affect Active Directory, SQL Server, Office applications, Remote Desktop, DirectX, and others, many triggered by opening crafted documents or network requests.

[Read original article](https://blog.talosintelligence.com/microsoft-patch-tuesday-july-2026/){: .btn .btn-primary }
