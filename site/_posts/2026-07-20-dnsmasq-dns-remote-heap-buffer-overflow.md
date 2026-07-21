---
layout: post
title: "Dnsmasq DNS Remote Heap Buffer Overflow"
date: 2026-07-20 15:15:06 +0300
categories: [RSS]
tags: [heap-overflow, dns, rce, cve, exploitation]
toc: true
---

CVE-2026-2291 is a heap buffer overflow in Dnsmasq's DNS caching system introduced by a 2015 code change that added escape sequences for special characters, potentially doubling domain name length, but failed to update the 1,025-byte `bigname` buffer allocation. The root cause is an unsafe `strcpy()` that copies escaped domain names without length validation. Exodus Intelligence demonstrates a complete remote exploitation chain: craft malicious DNS responses with overlong escaped domain names to overflow the buffer, corrupt the free list's `next` pointer, achieve write-what-where primitive via heap manipulation, and hijack a function pointer in musl's `ld.so` to gain remote code execution on Dnsmasq instances (affecting OpenWRT and other deployments). This affects versions before 2.92rel2 and 2.93 (patched May 11, 2026).

[Read original article](https://blog.exodusintel.com/2026/07/20/dnsmasq-dns-remote-heap-buffer-overflow/){: .btn .btn-primary }
