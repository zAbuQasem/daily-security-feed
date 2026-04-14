---
layout: post
title: "Binary Ninja 5.3 (Jotunheim)"
date: 2026-04-14 03:12:10 +0300
categories: [RSS]
tags: [reverse-engineering, binary-ninja, decompiler, ghidra, debugger]
toc: true
---

Binary Ninja 5.3 is a technically substantive tooling release centered on reverse-engineering workflows, adding new architecture APIs for standalone function-level lifting so plugins can analyze stateful or VM-style architectures that cannot be cleanly recovered one basic block at a time. The release also expands platform coverage with NDS32 support and AArch64 ILP32 ABI handling, including recognizer updates for ILP32 PLT entries and a fix for address-size calculation bugs that affect correct analysis. On the interoperability side, it adds Ghidra export and improves IDB import, which matters for analysts moving projects between disassemblers and preserving recovered analysis. Additional debugger work, hardware and conditional breakpoint support, and UI improvements for Mach-O slice selection make the release useful for practitioners, but it is primarily an incremental tooling upgrade rather than a new security finding.

[Read original article](https://binary.ninja/2026/04/13/binary-ninja-5.3-jotunheim.html){: .btn .btn-primary }
