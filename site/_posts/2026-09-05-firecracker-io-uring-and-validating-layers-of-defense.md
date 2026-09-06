---
layout: post
title: "Firecracker, io_uring and validating layers of defense"
date: 2026-09-05 00:00:00 +0300
categories: [RSS]
tags: [toctou, privilege-escalation, seccomp, io_uring, container-security]
toc: true
---

Firecracker's jailer process (aarch64 only) contained a TOCTOU vulnerability where privileged WRITE and CHOWN operations on cache info files followed symlinks without path verification, enabling privilege escalation inside the VM isolation boundary. While the vulnerability was patched, the article explores a critical defense-in-depth failure: the seccomp policy designed to block post-exploitation syscalls allows io_uring, which attackers can abuse to multiplex blocked system calls (e.g., symlinkat, renameat) by encoding them as io_uring opcodes, effectively bypassing the seccomp-bpf filter. The analysis demonstrates that measuring seccomp strength by syscall count is misleading—allowing io_uring negates the entire filtering strategy against TOCTOU-class breakouts.

[Read original article](https://www.antitree.com/2026/09/firecracker-io_uring-and-validating-layers-of-defense/){: .btn .btn-primary }
