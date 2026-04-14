---
layout: post
title: "JitterDropper"
date: 2026-04-14 03:12:06 +0300
categories: [RSS]
tags: [malware, dropper, rust, windows, shellcode]
toc: true
---

OpenAnalysis documents an actively developed Rust/MSVC Windows malware family dubbed JitterDropper, with two variant lines that either decrypt an embedded payload from .rdata or fetch a 122-byte encrypted shellcode stager from pixeldrain. Across nine builds, the samples share a distinctive anti-analysis pattern: paired CheckRemoteDebuggerPresent/IsDebuggerPresent checks, a fake GUI window, repeated EnumWindows padding, and GetTickCount-backed sleep gates implemented through Rust's thread::sleep path (CreateWaitableTimerExW/SetWaitableTimer) to detect sandbox time skipping. Variant I uses a three-stage decryptor combining a byte-wise XOR chain, 8-10 rounds of SSE permutation with XMM constant tables, and a final repeating-key XOR to recover a Donut/sRDI reflective loader and an encrypted inner PE, while Variant II uses a 32-byte SSE repeating XOR key and, in one fork, wraps the payload with AES-256-GCM via BCryptDecrypt using ChainingModeGCM. The analysis also highlights a strong clustering fingerprint based on stable per-API jitter budgets before calls like InternetOpenA, CoGetObject, and VirtualProtect, and traces feature evolution including explorer.exe CreateRemoteThread injection, %APPDATA% persistence, and a later regression from W^X to direct RWX allocation.

[Read original article](https://research.openanalysis.net/jitterdropper/dropper/rust/srdi/donut/pixeldrain/2026/04/13/jitterdropper.html){: .btn .btn-primary }
