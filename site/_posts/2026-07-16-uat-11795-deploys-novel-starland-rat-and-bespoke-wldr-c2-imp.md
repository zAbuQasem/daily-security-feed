---
layout: post
title: "UAT-11795 deploys novel Starland RAT and bespoke WLDR C2 implant in financially motivated campaign"
date: 2026-07-16 10:00:01 +0300
categories: [RSS]
tags: [malware, rat, c2, stealer, threat-intel]
toc: true
---

Cisco Talos disclosed UAT-11795, a Russian-speaking financially motivated threat actor conducting a campaign since June 2025 targeting users in the U.S. and Europe with trojanized installers (MobaXterm, WebEx, Zoom, DBeaverCE, FACEIT) delivered via ClickFix and HTA downloader. The actor deploys two novel implants: Starland RAT (Python-based, in-memory loader) and WLDR agent (PowerShell C2 with encrypted beaconing, task queuing, Runspace engine), supplemented by CastleStealer and Remcos RAT. The malware performs system reconnaissance, steals browser data and cryptocurrency wallets, and uses hardcoded C2 URLs with Polygon Ethereum smart contract fallback for C2 resilience, enabling hardware-bound victim tracking via drive volume serial number. The infrastructure spans trojanized staging domains, Telegram bot C&C, and parallel C2 domains with recovered Telegram channel "stuk komanda" active since June 2025.

[Read original article](https://blog.talosintelligence.com/uat-11795-deploys-novel-starland-rat-and-bespoke-wldr-c2-implant-in-financially-motivated-campaign/){: .btn .btn-primary }
