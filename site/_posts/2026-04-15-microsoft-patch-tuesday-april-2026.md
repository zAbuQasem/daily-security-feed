---
layout: post
title: "Microsoft Patch Tuesday – April 2026"
date: 2026-04-15 03:12:18 +0300
categories: [RSS]
tags: [windows, patch-tuesday, rce, sharepoint, active-directory]
toc: true
---

This Patch Tuesday roundup covers 165 Microsoft fixes for April 2026, with emphasis on one actively exploited issue, one publicly disclosed issue, and several critical remote code execution bugs in core Windows infrastructure. The most actionable items called out are CVE-2026-32201, an unauthenticated SharePoint Server spoofing flaw seen exploited in the wild, and CVE-2026-33825, a publicly disclosed Microsoft Defender elevation-of-privilege bug that requires enterprises on managed update channels to confirm engine version 4.18.26030.3011 or later. It also highlights CVE-2026-33824, a double-free in the Windows IKE Extension enabling unauthenticated network RCE, CVE-2026-33826, an Active Directory input-validation bug that can yield adjacent-network code execution for an authenticated attacker, and CVE-2026-33827, a Windows TCP/IP race condition reachable via crafted IPv6 traffic when IPsec is enabled. The practical value is patch prioritization for organizations running on-prem SharePoint, Defender-managed fleets, and identity or IPsec-heavy Windows environments, although the post is a high-level triage summary rather than a root-cause exploit analysis.

[Read original article](https://outpost24.com/blog/microsoft-patch-tuesday-april-2026/){: .btn .btn-primary }
