---
layout: post
title: "Slow DNS with Pi-hole + Unbound: Fixing Cold Lookup Latency"
date: 2026-10-30 02:29:22 +0300
categories: [RSS]
tags: [dns, infrastructure, performance]
toc: true
---

A troubleshooting guide documenting DNS performance degradation in a Pi-hole + Unbound setup in New Zealand, where cold DNS lookups took 500+ ms due to recursive resolution traversing root-to-authoritative chains across high-latency international links. Root cause analysis identifies that Unbound's full recursion incurs 140–220 ms per-hop latency to distant root/TLD servers, compounded by Unbound cache crashes triggered by system clock adjustment. The fix switches Unbound from recursion to DoT forwarding (Cloudflare/Quad9), reducing cold lookup median from 500 ms to 150 ms, with detailed measurements and network diagnostics included.

[Read original article](https://www.uncommonengineer.com/docs/engineer/LAB/pihole-unbound-slow-dns){: .btn .btn-primary }
