---
layout: post
title: "Identity, browsers, and node.js: Everything you missed in the Threat Detection Report miniseries"
date: 2026-04-16 03:12:35 +0300
categories: [RSS]
tags: [identity, browser, nodejs, lolbins, detection]
toc: true
---

Red Canary's recap distills several operational trends from its Threat Detection Report, emphasizing that attackers are increasingly targeting identity material such as credentials, OAuth consent grants, and browser session tokens because they provide direct access to SaaS data without needing full endpoint compromise. The post also highlights browsers as a primary attack surface and recommends controls like extension version pinning and ad-blocker hygiene to reduce exposure to malicious extensions and session theft. On the endpoint side, it calls out growing abuse of Node.js, Python, and Deno as alternative execution layers that blend into legitimate developer activity more easily than heavily monitored tools like PowerShell, especially when packaged as standalone executables. The article also reinforces evergreen evasion techniques such as DLL sideloading and LOLBin abuse, and pairs them with practical defensive measures including procedure-level purple-team testing, changing script file handlers to open in Notepad, and baselining trusted processes that execute from abnormal user-controlled paths.

[Read original article](https://redcanary.com/blog/security-operations/tdr-secops-recap/){: .btn .btn-primary }
