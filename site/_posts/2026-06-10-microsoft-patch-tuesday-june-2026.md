---
layout: post
title: "Microsoft Patch Tuesday – June 2026"
date: 2026-06-10 02:07:54 +0300
categories: [RSS]
tags: [patch-tuesday, windows, rce, critical, kernel]
toc: true
---

Microsoft's June 2026 Patch Tuesday addresses 206 CVEs, including four critical remote code execution flaws affecting core Windows infrastructure. CVE-2026-45657 allows kernel-level RCE via malformed TCP/IP packets without authentication; CVE-2026-47291 enables HTTP-based RCE in specific configurations; CVE-2026-44815 exploits the DhcpGetOriginalSubnetMask API to trigger RCE from a network-local DHCP server; CVE-2026-47281 grants SYSTEM privileges when users open malicious .code-workspace files in Visual Studio Code. None are currently under active exploitation, providing a critical window for immediate patching.

[Read original article](https://outpost24.com/blog/microsoft-patch-tuesday-june-2026/){: .btn .btn-primary }
