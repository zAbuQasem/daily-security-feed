---
layout: post
title: "Microsoft Patch Tuesday – May 2026"
date: 2026-05-13 00:48:36 +0300
categories: [RSS]
tags: [windows, patch-tuesday, rce, privilege-escalation, hyper-v]
toc: true
---

Outpost24's May 2026 Patch Tuesday roundup highlights 137 Microsoft fixes, including 30 Critical issues, and calls out several bugs with strong enterprise impact even though none are confirmed zero-days. The most urgent items include CVE-2026-41089, a stack-based buffer overflow in Windows Netlogon enabling unauthenticated RCE on domain controllers, and CVE-2026-41096, a heap-based buffer overflow in the Windows DNS client that can be triggered via malicious DNS responses. The post also flags a Hyper-V guest-to-host escape via use-after-free (CVE-2026-40402), authenticated server-side code-execution flaws in Dynamics 365 on-prem and SharePoint Server, and two likely-exploitable Microsoft Word RCEs caused by use-after-free and type confusion when opening or previewing crafted documents. It is primarily a prioritization-focused patch analysis rather than original exploitation research, but it provides useful triage signal on which Windows and on-prem Microsoft components defenders should patch first.

[Read original article](https://outpost24.com/blog/microsoft-patch-tuesday-may-2026/){: .btn .btn-primary }
