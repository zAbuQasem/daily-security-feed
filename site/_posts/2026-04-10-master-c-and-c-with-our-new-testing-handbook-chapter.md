---
layout: post
title: "Master C and C++ with our new Testing Handbook chapter"
date: 2026-04-10 03:12:57 +0300
categories: [RSS]
tags: [c-cpp, memory-safety, windows-kernel, seccomp, code-review]
toc: true
---

Trail of Bits published a comprehensive C/C++ security testing checklist covering five areas: general bug classes (memory safety, integer errors, type confusion, compiler-introduced bugs), Linux usermode libc gotchas, Linux kernel driver/module review, Windows usermode (DLL planting, unquoted path, WorstFit Unicode bypass), and Windows kernel driver issues. Notable findings include seccomp/BPF sandbox bypasses via io_uring syscalls that bypass BPF filters, CLONE_UNTRACED disabling seccomp enforcement, and ptrace race conditions. The post includes two live CTF-style challenges: a C ping program with two libc bugs enabling trivial exploitation (inet_ntoa static buffer reuse clobbering the SSRF check, plus a shell injection vector), and a Windows WDF driver using RTL_QUERY_REGISTRY_DIRECT without a type constraint — allowing an attacker to supply a REG_BINARY value that overwrites adjacent stack memory including a HandlerCallback function pointer, leading to kernel code execution.

[Read original article](https://blog.trailofbits.com/2026/04/09/master-c-and-c-with-our-new-testing-handbook-chapter/){: .btn .btn-primary }
