---
layout: post
title: "HP One Agent: local privilege escalation through race condition [CVE-2026-5064]"
date: 2026-09-08 07:05:53 +0300
categories: [RSS]
tags: [lpe, race-condition, dll-sideloading, windows, cve]
toc: true
---

HP One Agent prior to version 1.3.214.7339 is vulnerable to local privilege escalation through a race condition in signature verification combined with DLL sideloading. The service runs as SYSTEM and loads plugin DLLs from a user-writable directory (`C:\ProgramData\HP\telemetry\collectors`), checking signatures via `WinVerifyTrust` and `FindFirstFile`/`FindNextFile` enumeration. However, DLLs added to the folder after enumeration completes bypass verification but can still be loaded as dependencies. The researcher exploited this by dropping large signed DLLs to slow verification, detecting the race window via file handle contention, dropping a malicious DLL that proxies legitimate exports with an added payload (e.g., adding a local admin). This escalates execution to SYSTEM privileges with minimal user interaction.

[Read original article](https://blog.scrt.ch/2026/09/08/hp-one-agent-local-privilege-escalation-through-race-condition-cve-2026-5064/){: .btn .btn-primary }
