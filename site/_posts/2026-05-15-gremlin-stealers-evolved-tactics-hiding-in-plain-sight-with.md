---
layout: post
title: "Gremlin Stealer's Evolved Tactics: Hiding in Plain Sight With Resource Files"
date: 2026-05-15 10:00:52 +0300
categories: [RSS]
tags: [malware, infostealer, dotnet, obfuscation, threat-intel]
toc: true
---

Unit 42 analyzes a newer Gremlin Stealer variant that hides its second-stage payload inside the .NET Resource section, XOR-encodes the embedded data, and in some samples adds commercial packer protection with instruction virtualization that runs the logic through a private VM. Decrypting the resource blob with a single-byte XOR key reveals hard-coded C2 and exfiltration paths, while the updated loader only decrypts and maps key functions into memory on demand, making static inspection far less useful than dynamic debugging. The stealer collects browser cookies, session tokens, clipboard data, cryptocurrency wallet material, and FTP/VPN credentials, packages the loot into a ZIP named after the victim's public IP, and uploads it to a newly observed operator site at 194.87.92.109. Compared with older Gremlin builds, this version also broadens collection with Discord token theft and crypto-clipper behavior, showing a shift from straightforward credential harvesting toward a more modular and anti-analysis-focused infostealer.

[Read original article](https://unit42.paloaltonetworks.com/gremlin-stealer-evolution/){: .btn .btn-primary }
