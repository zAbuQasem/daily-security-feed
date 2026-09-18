---
layout: post
title: "Unpacking a laZzzy Donut"
date: 2026-09-17 04:00:00 +0300
categories: [RSS]
tags: [malware, reverse-engineering, obfuscation, shellcode, defensive-analysis]
toc: true
---

Trusted Security published a detailed reverse-engineering analysis of a multi-stage malware loader named laZzzy Donut that chains Python bytecode obfuscation, Donut shellcode wrapping, and encrypted .NET payloads. The attack flow begins with Kramer-obfuscated Python bytecode that decodes and decrypts RC4-encrypted shellcode, which is then copied into executable memory and executed. The shellcode (Stage 2) was generated using Thewover's Donut tool to wrap a binary into position-independent x86-64 code. The authors document their reverse-engineering methodology, including modifications to existing tools like kramer_python_deobfuscator.py (reducing key recovery time from hours to seconds) and use of Volexity's donut-decryptor to extract unencrypted components. This write-up provides practical defense-side techniques for analyzing heavily obfuscated, multi-stage loaders and demonstrates how existing public tooling can be adapted for threat analysis.

[Read original article](https://trustedsec.com/blog/unpacking-a-lazzzy-donut){: .btn .btn-primary }
