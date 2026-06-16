---
layout: post
title: "Zombie COTables: Resurrecting Freed Memory to Escape VirtualBox"
date: 2026-06-15 15:44:54 +0300
categories: [RSS]
tags: [virtualization, use-after-free, hypervisor-escape, memory-safety]
toc: true
---

A use-after-free vulnerability in VirtualBox's SVGA (VMware SVGA-II) graphics device allows guest-to-host escape via resurrection of freed memory structures (COTables). The attack exploits the FIFO command queue and memory-mapped I/O registers in VirtualBox's graphics acceleration subsystem to corrupt freed heap objects, gaining arbitrary code execution on the hypervisor. The vulnerability was patched in Oracle's January 2026 Critical Patch Update and presented at OffensiveCon 2026 by Exodus Intelligence researchers.

[Read original article](https://blog.exodusintel.com/2026/06/15/zombie-cotables-resurrecting-freed-memory-to-escape-virtualbox/){: .btn .btn-primary }
