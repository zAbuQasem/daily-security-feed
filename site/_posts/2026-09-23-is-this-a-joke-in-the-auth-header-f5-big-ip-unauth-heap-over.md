---
layout: post
title: "Is This A Joke? In The Auth Header? (F5 BIG-IP UnAuth Heap-Overflow to RCE CVE-2026-94127)"
date: 2026-09-23 23:19:19 +0300
categories: [RSS]
tags: [heap-overflow, rce, infrastructure, unauthenticated]
toc: true
---

CVE-2026-94127 is an unauthenticated heap buffer overflow in F5 BIG-IP APM's Authorization header processing. The vulnerable code allocates a 0x4100-byte buffer but fails to validate the actual Authorization header size before memcpy, allowing an attacker to overflow the heap and achieve remote code execution without authentication. watchtowr's patch analysis reveals the fix merely adds a size check (v20 > 0x4100). Affects BIG-IP 21.1.0 and 17.x APM modules; the vulnerability is actively being exploited in the wild. Given BIG-IP's critical role in load balancing, SSL termination, and authentication, this is a high-impact infrastructure vulnerability.

[Read original article](https://labs.watchtowr.com/is-this-a-joke-in-the-auth-header-f5-big-ip-unauth-heap-overflow-to-rce-cve-2026-94127/){: .btn .btn-primary }
