---
layout: post
title: "Game of Hide and Seek: Detecting Dynamic API Resolution at Runtime With Aether"
date: 2026-06-24 14:23:13 +0300
categories: [RSS]
tags: [malware, detection, evasion, c2, windows]
toc: true
---

Deep-dive technical analysis of how modern malware loaders conceal malicious capabilities by dynamically resolving Windows APIs at runtime rather than exposing them in the static Import Address Table (IAT). The article covers three primary evasion techniques: PEB traversal to locate DLL base addresses without calling `GetModuleHandle`, API hashing (using algorithms like Djb2) to match function names without storing plaintext strings, and direct system calls to bypass user-land EDR hooks. Using the Adaptix C2 agent as a case study, the author demonstrates how these techniques combined allow malware to execute from legitimate mapped memory with low entropy and normal execution flows, evading traditional structural malware scanners. The Aether v0.9 detection tool is then shown to identify these evasions by analyzing heap-allocated function pointer tables and the mechanics of dynamic resolution rather than relying solely on private memory or IAT signatures.

[Read original article](https://0xsp.com/research/game-of-hide-and-seek-detecting-dynamic-api-resolution-at-runtime-with-aether/?utm_source=rss&utm_medium=rss&utm_campaign=game-of-hide-and-seek-detecting-dynamic-api-resolution-at-runtime-with-aether){: .btn .btn-primary }
