---
layout: post
title: "The Detection & Response Chronicles: Covert Operations Through QEMU"
date: 2026-06-04 14:26:05 +0300
categories: [RSS]
tags: [malware, evasion, c2, detection]
toc: true
---

NVISO researchers document how adversaries abuse QEMU to run isolated VMs containing command-and-control infrastructure, evading host-based AV/EDR detection. A compromised Linux disk image launches an Adaptix Gopher beacon that tunnels C2 traffic through SSH over TCP 443, obfuscating the remote infrastructure while maintaining encrypted, resilient communication via shell scripts that auto-restart on connection loss. The technique isolates attacker tooling from the compromised Windows host and complicates forensics, though the authors detail practical detection opportunities through network indicators and QEMU process monitoring.

[Read original article](https://blog.nviso.eu/2026/06/04/the-detection-response-chronicles-covert-operations-through-qemu/){: .btn .btn-primary }
