---
layout: post
title: "Microsoft Windows NCSI Cross-Context Proxy Authentication Coercion - ZDI-26-708 - Part 2"
date: 2026-09-28 07:00:00 +0300
categories: [RSS]
tags: [privesc, windows, event-log, proxy, authentication]
toc: true
---

A Windows privilege escalation (ZDI-26-708) allows unprivileged users to coerce the NETWORK SERVICE account into using attacker-controlled proxy settings through the Windows Event Log channel `Microsoft-Windows-WinINet-Config`. NCSI subscribes to Event ID 5600 and extracts proxy configuration fields (fAutoDetect, pwszAutoConfigUrl, pwszProxy, pwszProxyBypass) without validating the source user context, storing them for use by NETWORK SERVICE's WinHTTP probe operations. An attacker can inject a malicious proxy to intercept credentials or perform MITM attacks on connectivity checks. The vulnerability chains Event Log subscriptions via `EvtSubscribe`/`EvtRender`, proxy state storage in netprofm, and downstream WinHTTP session configuration without proper authorization checks. This represents a novel cross-context proxy authentication coercion technique with broad applicability across Windows systems.

[Read original article](https://pgj11.com/posts/Windows-NCSI-Proxy-Auth-Coercion-Part-2/){: .btn .btn-primary }
