---
layout: post
title: "COFF Mixing - Hiding in Plain Sight"
date: 2026-07-28 14:27:46 +0300
categories: [RSS]
tags: [evasion, coff, obfuscation, windows, malware-delivery]
toc: true
---

COFF mixing is an evasion technique that combines malicious capabilities (COFF/BOF payloads) with benign code at link-time to create legitimate-looking Windows PE executables. Unlike memory-injected content, which generates indicators of compromise (unbacked RX memory, call stack anomalies, memory allocation patterns), COFF-mixed payloads reside in image-backed memory with normal call stacks and symbol tables. The technique uses specification files and the `cpl` utility to merge capability objects into PE-ready COFF files with proper stack unwinding (.xdata/.pdata sections), then employs symbol stripping and code shuffling (+disco) to obfuscate payload execution within benign functions. This approach trades flexibility for reduced forensic artifacts and improved evasion against EDR/memory analysis.

[Read original article](https://rastamouse.me/coff-mixing/){: .btn .btn-primary }
