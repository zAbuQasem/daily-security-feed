---
layout: post
title: "Striga: Lifting x86 to LLVM IR with Python"
date: 2026-05-21 11:00:00 +0300
categories: [RSS]
tags: [reverse-engineering, llvm, binary-analysis, x86, deobfuscation]
toc: true
---

The post introduces Striga, a Python-based x86_64 lifter that translates machine instructions into LLVM IR to make binary analysis and transformation easier than working directly on assembly. Its core design models CPU state as an in-memory `State` struct containing general-purpose registers and individual flag bytes, then emits LLVM `load`/`store` operations against that struct so standard optimization passes like `mem2reg` can recover SSA form automatically. Memory accesses are separated from register state by using an opaque `memory` pointer in lifted functions of the form `void lifted(State* state, void* memory)`, which lets the lifter distinguish CPU RAM reads like `mov rax, [rbx+42]` from internal state manipulation. The article walks through concrete IR emitted for register moves and memory dereferences, and explains how each x86 instruction maps to its own basic block with explicit successor branches, making the output suitable for later brightening, recompilation, and devirtualization workflows.

[Read original article](https://secret.club/2026/05/21/striga.html){: .btn .btn-primary }
