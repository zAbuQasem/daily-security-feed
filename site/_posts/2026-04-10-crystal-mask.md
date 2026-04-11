---
layout: post
title: "Crystal Mask"
date: 2026-04-10 03:12:52 +0300
categories: [RSS]
tags: [evasion, cobalt-strike, malware, red-team, windows]
toc: true
---

Crystal Mask is a Cobalt Strike sleepmask implementation built on the Crystal Palace/Tradecraft Garden framework, which separates evasion logic from payload capabilities via IAT hooking and PICO memory-loaded modules. Rather than relying on Beacon's built-in BeaconGate customization, Crystal Mask hooks Beacon's IAT to redirect Win32 API calls through custom evasion wrappers — enabling call stack spoofing and memory obfuscation for APIs not natively supported by BeaconGate (e.g., CreateProcess). The article details how Beacon's software contracts (BEACON_INFO, FUNCTION_CALL, BUD) expose memory allocation metadata to the sleepmask, enabling XOR-based memory masking across PE sections with dynamic VirtualProtect permission management. The approach provides flexibility to swap evasion tradecraft independently of capability code at link-time, at the cost of additional developer overhead for tracking heap allocations and managing memory state during sleep cycles.

[Read original article](https://rastamouse.me/crystal-mask/){: .btn .btn-primary }
