---
layout: post
title: "GhostPack Necromancy: Reforging C# Tools with WasmForge"
date: 2026-06-19 01:55:33 +0300
categories: [RSS]
tags: [edr-evasion, c#, wasm, amsi, malware]
toc: true
---

Praetorian's WasmForge toolchain compiles heavily-signatured GhostPack C# tools (Rubeus, Seatbelt) to WebAssembly via .NET's NativeAOT-WASI, evading YARA signatures, AMSI hooks, and ETW tracing by running entirely outside the .NET runtime. The build pipeline combines source patching, C bridges for calling conventions, and BCL backfills; the resulting WASM modules are wrapped in signed PE binaries for C2 delivery. This eliminates the detection surface of CLR loading and IL bytecode analysis, addressing the most heavily-signatured tools in offensive security toolkits.

[Read original article](https://www.praetorian.com/blog/wasmforge-csharp-ghostpack-edr-evasion/){: .btn .btn-primary }
