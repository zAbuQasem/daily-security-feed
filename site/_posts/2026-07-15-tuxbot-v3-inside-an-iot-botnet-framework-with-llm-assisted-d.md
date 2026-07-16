---
layout: post
title: "TuxBot v3: Inside an IoT Botnet Framework With LLM-Assisted Development"
date: 2026-07-15 10:00:54 +0300
categories: [RSS]
tags: [malware, botnet, iot, c2, ddos]
toc: true
---

Palo Alto Unit 42 discovered TuxBot v3 Evolution, a modular IoT botnet framework that cross-compiles to 17 architectures (ARM, MIPS, x86_64, PowerPC, RISC-V) and combines credential brute-forcing with exploit code targeting 30+ device families. The framework features a Go-based C2 server with DDoS-for-hire panel and resilient command fallback mechanisms including SHA512-based DGA, P2P gossip with Ed25519 signatures, IRC, DNS TXT, and HTTP polling. Threat actors leveraged LLM code generation to accelerate development, though the recovered sample is approximately 70% functional with several exploits and features broken due to unverified LLM hallucinations. Analysis reveals a production-ready threat: the development timeline (Jan 2025–Apr 2026) includes 254 automated DDoS benchmarks, git artifacts leaking developer infrastructure, and C2 infrastructure first observed in March 2026. Given adversaries have access to the same code, corrected iterations capable of full functionality likely exist in the wild.

[Read original article](https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/){: .btn .btn-primary }
