---
layout: post
title: "Blinder Tunnel Campaign Targets Iraqi Infrastructure"
date: 2026-10-06 10:00:33 +0300
categories: [RSS]
tags: [malware, evasion, c2, supply-chain, threat-intel]
toc: true
---

Iranian state-aligned threat actors (CL-STA-1178) launched the Blinder Tunnel campaign targeting Iraqi critical infrastructure beginning March 2026, using social engineering lures impersonating Dubai Airports recruitment to deliver trojanized coding challenges. The attack chain exploits legitimate Windows native.csproj files to trigger AppDomainManager hijacking, followed by DLL sideloading to execute ShelbyLoader V2 malware. C2 communication is established via GitHub API infrastructure misuse—leveraging repositories to fetch decryption keys, download payloads, and using GitHub issues as a resilient fallback—combined with the Chisel tunneling utility. The campaign demonstrates AppDomainManager hijacking as an emerging evasion technique adopted by Iranian threat groups, with operational security failures linking it to a separate May-June 2026 credential harvesting operation targeting Israeli entities.

[Read original article](https://unit42.paloaltonetworks.com/blinder-tunnel-targets-critical-infrastructure/){: .btn .btn-primary }
