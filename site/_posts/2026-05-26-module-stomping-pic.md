---
layout: post
title: "Module Stomping PIC"
date: 2026-05-26 17:30:32 +0300
categories: [RSS]
tags: [malware, defense-evasion, dll-hollowing, pic, windows]
toc: true
---

This article explores applying module stomping (DLL hollowing) to Position-Independent Code (PIC) and PIC Objects (PICOs) within the Crystal Palace framework. The classic technique loads a legitimate signed DLL via NtCreateSection/NtMapViewOfSection, zeroes its headers/sections, then overwrites them with malicious code — making it appear backed by a trusted on-disk module rather than residing in anonymous private memory. The author extends this to PICOs by stomping the .text and .data sections of a loaded DLL instead of using VirtualAlloc, and further adapts it for Crystal Palace PIC blobs by placing executable code in the DLL's .text section while reusing its RW .data section for BSS storage. Testing with Moneta showed no additional IOCs beyond those already expected for standard module stomping (modified .text sections, missing PEB entry, erased headers), confirming this is an incremental refinement rather than a novel evasion breakthrough.

[Read original article](https://rastamouse.me/module-stomping-pic/){: .btn .btn-primary }
