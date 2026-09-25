---
layout: post
title: "Bypassing EDR with Local AI"
date: 2026-09-24 02:34:40 +0300
categories: [RSS]
tags: [edr-evasion, malware, llm, red-team, lsass]
toc: true
---

Demonstrates EDR evasion through AI-assisted malware development. A penetration tester shows that while commercial LLMs (Claude) refuse to generate evasion tools, uncensored open-weight models (DeepSeek, Qwen 3.8) readily produce LSASS dumpers using process reflection, in-memory minidump creation, XOR encryption, and string scrubbing without fine-tuned prompting. The resulting executable bypassed two EDR solutions in their lab. Defenders are advised to prioritize attack surface reduction, least privilege enforcement, and credential hygiene, as rented compute and uncensored models now make undetected post-exploitation accessible to lower-skilled attackers.

[Read original article](https://projectblack.io/blog/bypassing-edr-with-local-ai/){: .btn .btn-primary }
