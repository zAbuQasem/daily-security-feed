---
layout: post
title: "Enter the WasmForge: Compiling Sliver into WebAssembly"
date: 2026-06-04 13:30:00 +0300
categories: [RSS]
tags: [evasion, c2, wasm, detection-evasion]
toc: true
---

WasmForge is a loader that compiles Go-based offensive tools (specifically Sliver C2) to WebAssembly to evade EDR and static analysis. The pipeline converts the Go standard library to target WASM with WASI shims that transparently bridge OS APIs (net.Dial, syscalls, file I/O), compiles the tool to a .wasm module, and embeds it in an outer Go binary containing a custom Wazero runtime plus ~80 host shim functions for Windows/macOS APIs. The core evasion advantage is that defensive tooling for WASM analysis is far less mature than for native PE binaries—most heuristic engines fail to recognize malicious code in unfamiliar WASM instruction sets. This allows red teamers to deploy hardened implants with zero source modifications and minimal additional evasion work. The approach combines WASM's portability, weak analysis landscape, and automated polymorphism/renaming to create operational security-safe implants without touching the original tool source.

[Read original article](https://www.praetorian.com/blog/wasmforge-sliver-webassembly/){: .btn .btn-primary }
