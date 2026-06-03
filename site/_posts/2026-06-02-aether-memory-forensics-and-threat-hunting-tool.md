---
layout: post
title: "Aether: memory forensics and threat hunting tool"
date: 2026-06-02 11:39:43 +0300
categories: [RSS]
tags: [memory-forensics, threat-hunting, detection, malware, tool-release]
toc: true
---

Aether is a memory forensics tool written in Zig that addresses false positive challenges in detecting code injection and memory tampering. The tool uses a five-layer filter pipeline (L1-L5) to distinguish legitimate runtime modifications from malicious code injection: L1 filters for executable pages only, L2 grades modification ratios, L3 requires corroboration from independent signals, L4 suppresses .NET JIT noise while scanning other modules, and L5 performs byte-level disk comparison to confirm tampering. The approach reduces false positives by over 80% compared to naive modified-code detection by requiring multi-signal correlation before flagging findings, while maintaining coverage through hook prologue pattern matching and thread start address validation.

[Read original article](https://0xsp.com/security%20research%20%20development%20srd/aether-memory-forensics-and-threat-hunting-tool/?utm_source=rss&utm_medium=rss&utm_campaign=aether-memory-forensics-and-threat-hunting-tool){: .btn .btn-primary }
