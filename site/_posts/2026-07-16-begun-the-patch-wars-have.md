---
layout: post
title: "Begun, the Patch Wars have"
date: 2026-07-16 18:00:50 +0300
categories: [RSS]
tags: [malware, supply-chain, c2, evasion, threat-intel]
toc: true
---

Cisco Talos disclosed UAT-11795, a Russian-speaking financially motivated threat actor distributing trojanized installers of popular tools (Webex, Zoom, MobaXterm) containing Starland RAT and a custom in-memory PowerShell C2 agent (WLDR) since June 2025. The campaign targets users in the US and Europe, using AMSI/ETW evasion and blockchain-anchored C2 fallback mechanisms to maintain persistence while deploying secondary payloads (CastleStealer, Remcos RAT) for credential and cryptocurrency theft. Defenders should monitor for mshta.exe execution and suspicious in-memory PowerShell activity with unexpected scheduled task creation.

[Read original article](https://blog.talosintelligence.com/begun-the-patch-wars-have/){: .btn .btn-primary }
