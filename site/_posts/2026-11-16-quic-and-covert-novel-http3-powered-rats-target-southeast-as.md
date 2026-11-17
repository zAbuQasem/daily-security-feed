---
layout: post
title: "QUIC and Covert: Novel HTTP/3-Powered RATs Target Southeast Asian Governments"
date: 2026-11-16 23:00:55 +0300
categories: [RSS]
tags: [rat, c2, cyberespionage, malware, http3]
toc: true
---

Unit 42 reveals a multi-stage cyberespionage campaign (TGR-STA-0049) targeting Southeast Asian governments since July 2025, deploying two previously undocumented custom RATs: PerfectPioneer and its modular successor KUKURAT. PerfectPioneer features an early adoption of HTTP/3 over UDP for C2 communications—bypassing traditional TCP-optimized deep packet inspection—and an isDangerousCommand validation engine that blocks operators from executing noisy or destructive commands that could trigger alerts. KUKURAT adds a custom spoofing engine that generates synthetic benign network, registry, and file activity to obscure indicators of compromise within artificial noise. The campaign demonstrates high operational stealth through rapid iterative development, infrastructure leveraging web shells (ASPXSpy, Godzilla, Suo5), and credential harvesting with exfiltration methodologies refined over nine months.

[Read original article](https://unit42.paloaltonetworks.com/custom-rats-target-southeast-asia-governments/){: .btn .btn-primary }
