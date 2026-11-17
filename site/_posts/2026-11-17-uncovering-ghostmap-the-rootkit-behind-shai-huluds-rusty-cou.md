---
layout: post
title: "Uncovering GhostMap: The Rootkit Behind Shai-Hulud’s Rusty Cousin"
date: 2026-11-17 13:40:31 +0300
categories: [RSS]
tags: [supply-chain, malware, linux, ebpf, rootkit]
toc: true
---

GhostMap is a Linux eBPF rootkit deployed by the IronWorm malware implant (a Rust-based supply chain attack delivered via compromised npm packages like weavedb-sdk@0.45.3) and reused across the Atomic Arch AUR campaign. The rootkit hides processes, files, and network sockets by manipulating kernel data in real-time—specifically, it hooks getdents64 to intercept directory listings and modifies the d_reclen field in /proc entries to skip hidden processes, while using inode-based filtering to conceal listeners from /proc/net/tcp. Crucially, the research demonstrates that while concealment succeeds against standard enumeration tools (ps, ls), it fails against some inspection methods (e.g., ss exposes sockets the rootkit hides from /proc/net/tcp) and is completely transparent to runtime monitors like Tracee, which detect the eBPF program attachments and kernel memory writes as they occur. The findings highlight that process hiding is a view problem—hidden entries remain accessible via known /proc/PID paths—and that runtime monitoring provides orthogonal detection evidence independent of the rootkit's manipulation of system tools.

[Read original article](https://www.aquasec.com/blog/ironworm-ebpf-rootkit-ghostmap-linux/){: .btn .btn-primary }
