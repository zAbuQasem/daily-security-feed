---
layout: post
title: "UAT-12643: Suspected North Korea-aligned actor blends blockchain resilience with targeted infostealing"
date: 2026-11-18 11:00:00 +0300
categories: [RSS]
tags: [malware, rat, infostealer, blockchain, threat-intelligence]
toc: true
---

Cisco Talos tracked UAT-12643, a financially motivated threat actor (potentially North Korea-aligned) operating a modular Go-based Overlord RAT, a Python infostealer called "Good Game," and a clipboard hijacker targeting cryptocurrency, gaming, and VoIP users primarily in Europe. The Overlord RAT variant implements a Solana blockchain C2 resilience technique by embedding encrypted server URLs in transaction memos, refining a method previously observed with Lazarus Group. Initial access uses weaponized Windows shortcuts (abusing MpCmdRun.exe and certutil for payload download), HTA droppers with MSXML2.ServerXMLHTTP, and MSBuild LOLBin with spoofed BITS User-Agent. Infrastructure analysis revealed an exposed Flask server hosting payloads, multiple C2 ports for different services, and exfiltration via Discord webhooks and gofile.io, indicating significant operational security failures that exposed the actor's full toolkit.

[Read original article](https://blog.talosintelligence.com/uat-12643-suspected-north-korea-aligned-actor-blends-blockchain-resilience-with-targeted-infostealing/){: .btn .btn-primary }
