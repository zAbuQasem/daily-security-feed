---
layout: post
title: "Dirty Frag: Linux Kernel Local Privilege Escalation via ESP and RxRPC"
date: 2026-05-08 08:57:17 +0300
categories: [RSS]
tags: [linux-kernel, lpe, esp, rxrpc, memory-corruption]
toc: true
---

Wiz describes a Linux kernel local privilege-escalation bug class in the networking stack where packet fragment handling can be driven through the ESP (IPsec Encapsulating Security Payload) and RxRPC paths to corrupt kernel memory. The issue appears to stem from inconsistent assumptions around fragmented skb/page-backed buffers across those subsystems, letting a local attacker turn crafted packet processing into a reliable privilege-escalation primitive instead of a simple crash. The affected surface is Linux systems that expose the relevant kernel features, making the bug especially relevant for hardened multi-user and containerized environments where kernel attack surface matters. Even without being a remote exploit, the write-up is valuable because it connects two relatively obscure kernel components into a practical root-to-kernel compromise path and shows how fragment-management bugs remain exploitable in modern Linux.

[Read original article](https://www.wiz.io/blog/dirty-frag-linux-kernel-local-privilege-escalation-via-esp-and-rxrpc){: .btn .btn-primary }
