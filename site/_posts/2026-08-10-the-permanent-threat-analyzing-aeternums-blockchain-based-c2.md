---
layout: post
title: "The Permanent Threat: Analyzing Aeternum’s Blockchain-Based C2 Operations and Communications"
date: 2026-08-10 22:00:02 +0300
categories: [RSS]
tags: [malware, blockchain, c2, evasion, rce]
toc: true
---

Aeternum is a C++ botnet loader that decentralizes command-and-control by storing encrypted instructions directly in Polygon blockchain smart contracts, which infected Windows systems retrieve via JSON-RPC queries to public endpoints. The loader employs multi-stage unpacking, persistence via AppData shortcuts, XOR-based deobfuscation of configuration strings, and weak PBKDF2HMAC/AES-GCM encryption for command decryption. Palo Alto Networks' analysis details three associated samples including a Python-based Telegram C2 variant and XWorm RAT combined with XMRig cryptocurrency mining. This architecture creates a highly resilient, low-cost threat that resists traditional takedown methods since threat actors control infrastructure through immutable on-chain smart contracts rather than domain registrars or hosting providers.

[Read original article](https://unit42.paloaltonetworks.com/aeternum-blockchain-c2-analysis/){: .btn .btn-primary }
