---
layout: post
title: "How I Found a $113,337 AF_ALG Linux Local Privilege Escalation Before Copy Fail"
date: 2026-09-24 00:00:00 +0300
categories: [RSS]
tags: [linux-kernel, lpe, race-condition, container-escape, cve]
toc: true
---

A race condition in Linux AF_ALG (a userspace cryptographic socket API) allows unprivileged users to escalate to root via out-of-bounds access when multiple writers share an AF_ALG socket and issue concurrent sendmsg() calls. CVE-2025-39964, discovered by STAR Labs researchers, affects Linux kernels since ~2011 and can also escape Docker containers to the host. The vulnerability is distinct from Copy Fail (also AF_ALG-based), which is a straight-line logic flaw in the AEAD path; this exploit targets the race between writers in socket state handling. The detailed technical analysis includes kernel internals, AF_ALG data flow, and exploit methodology that earned a $113,337 kernelCTF reward.

[Read original article](https://starlabs.sg/blog/2026/09-how-i-found-a-113337-af_alg-linux-local-privilege-escalation-before-copy-fail/){: .btn .btn-primary }
