---
layout: post
title: "The Closed Quorum: Inside the first reported autonomous AI C2 implant"
date: 2026-09-22 10:00:58 +0300
categories: [RSS]
tags: [malware, ai, c2, autonomous, rce]
toc: true
---

CLOSEDQUORUM is the first reported autonomous Windows implant that replaces traditional attacker-operated C2 infrastructure with a quorum of commercial LLM providers (DeepSeek, Qwen, Mistral, Google Gemini). The 16.4MB Go-compiled binary queries four models in sequence, aggregates their responses via plurality voting on structured JSON decisions, and executes the winning action without human operator involvement—achieving full autonomy for credential harvesting and wallet theft. This represents a fundamental shift from AI augmenting human operators (speed/scale) to AI replacing them entirely in attack phases (effort displacement), enabling attacks to continue unattended. The design collapses C2 infrastructure into commercial APIs used by thousands of legitimate apps daily, making it harder to attribute and block than traditional domains or IPs. While no confirmed in-the-wild deployment exists, this Cisco Talos research demonstrates a novel attack class with broad applicability to future autonomous malware operations.

[Read original article](https://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/){: .btn .btn-primary }
