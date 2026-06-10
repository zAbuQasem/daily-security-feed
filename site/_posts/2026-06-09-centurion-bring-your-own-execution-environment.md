---
layout: post
title: "Centurion: Bring Your Own Execution Environment"
date: 2026-06-09 19:14:27 +0300
categories: [RSS]
tags: [evasion, vm, malware, redteam]
toc: true
---

Centurion is a virtualized loader that compiles malicious code to RISC-V bytecode executed within a lightweight VM interpreter, enabling red team payloads to evade modern EDR detection. The technique addresses EDR's capability to scan memory for decompressed malware by never materializing native code in recognizable form—instead proxying Win32 API calls and maintaining execution within a bytecode context. The article traces the evolution from traditional packers through VM-based virtualization projects (RISC-Y Business, Firebeam, Fox-IT) and demonstrates how LLMs accelerated prototype development from a planned 3–6 month effort to one week, shifting the engineering constraint from technical feasibility to implementation labor.

[Read original article](https://www.praetorian.com/blog/virtualized-loader-centurion/){: .btn .btn-primary }
