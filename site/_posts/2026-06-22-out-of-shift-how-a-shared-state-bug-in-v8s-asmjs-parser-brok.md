---
layout: post
title: "Out of Shift: How a Shared State Bug in V8’s AsmJS Parser Broke the Ubercage"
date: 2026-06-22 15:59:57 +0300
categories: [RSS]
tags: [v8, parser, asmjs, wasm, sandbox-escape]
toc: true
---

A shared state management bug in V8's AsmJS parser (CVE-2026-3542) corrupts the WebAssembly opcode stream when processing heap access expressions. The vulnerability occurs in AsmJsParser::ShiftExpression() during heap validation, where the current WebAssembly stream position is not properly tracked when the parser replaces shift operations (e.g., `HEAP32[n >> 2]`) with bitwise AND expressions. This state corruption allows an attacker to inject malformed WebAssembly opcodes into the module, potentially breaking V8's sandbox (Ubercage) when the corrupted stream is decoded. The bug was patched in Chrome on March 3, 2026.

[Read original article](https://blog.exodusintel.com/2026/06/22/out-of-shift-how-a-shared-state-bug-in-v8s-asmjs-parser-broke-the-ubercage/){: .btn .btn-primary }
