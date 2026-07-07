---
layout: post
title: "Hook Chains (how I built Crystal Kit incorrectly*)"
date: 2026-07-06 20:29:30 +0300
categories: [RSS]
tags: [evasion, hooking, red-team, windows, malware]
toc: true
---

A technical deep-dive on hook chains in Crystal Palace, demonstrating how to compose modular evasion tradecraft by chaining multiple IAT hooks rather than monolithic hook implementations. The article compares single-hook architecture (e.g., a Sleep hook that combines sleep obfuscation + call stack spoofing in one function) to hook chains, where separate hooks are layered to handle orthogonal concerns — allowing tradecraft to be swapped, removed, or reordered via spec files rather than code modifications. Concrete example chains sleep obfuscation with call stack spoofing via DFR forwarding, making it trivial to replace stack spoofing with syscalls or remove it entirely. Applicable to defenders understanding advanced red team evasion architecture and red teamers building maintainable, composable toolchains.

[Read original article](https://rastamouse.me/cpl-hook-chains/){: .btn .btn-primary }
