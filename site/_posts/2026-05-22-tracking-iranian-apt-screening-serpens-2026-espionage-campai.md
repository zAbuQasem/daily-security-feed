---
layout: post
title: "Tracking Iranian APT Screening Serpens’ 2026 Espionage Campaigns"
date: 2026-05-22 13:00:42 +0300
categories: [RSS]
tags: [apt, iran, rat, phishing, .net]
toc: true
---

Unit 42 tracks an Iran-linked Screening Serpens espionage campaign that used tailored job-recruitment phishing lures against aerospace, defense, telecom, and technology targets in the U.S., Israel, the UAE, and other Middle Eastern organizations during February-April 2026. The report identifies six new RAT variants across two malware families, MiniUpdate and MiniJunk V2, delivered through infection chains that rely on DLL sideloading and per-target command-and-control domain sets, many hosted on Azure, to improve operational resilience and reduce cross-contamination between campaigns. A key technical evolution is the use of AppDomainManager hijacking in .NET applications, where a legitimate configuration file is abused during application initialization to disable built-in security controls before the malware loads. The research is useful because it documents both the actor’s malware-development cadence and a concrete tradecraft upgrade that defenders can hunt for in phishing-driven .NET execution chains.

[Read original article](https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/){: .btn .btn-primary }
