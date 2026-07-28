---
layout: post
title: "Detection primitives for eBPF rootkits"
date: 2026-07-27 00:00:00 +0300
categories: [RSS]
tags: [ebpf, rootkit, detection, linux, kernel]
toc: true
---

Datadog Security Labs analyzes detection primitives for actively-deployed eBPF rootkits bypassing standard Linux introspection tools. VoidLink abuses bpf_probe_write_user() to inflate Netlink message length fields in the recvmsg() buffer, causing user-space parsers like ss to skip hidden connections entirely without detecting parse errors. LinkPro uses bpf_override_return() to intercept BPF_PROG_GET_NEXT_ID syscalls and return -ENOENT for allowlisted program IDs, hiding its own eBPF programs from enumeration tools like bpftool. The research identifies specific detection signals: comparing bpftool prog list output against BPF_PROG_GET_FD_BY_ID (a hook the malware doesn't intercept) reveals truncation artifacts. These techniques defeat established detection methods and are observed in production malware families including VoidLink, LinkPro, and the Atomic Arch npm campaign.

[Read original article](https://securitylabs.datadoghq.com/articles/detection-primitives-for-ebpf-rootkits/){: .btn .btn-primary }
