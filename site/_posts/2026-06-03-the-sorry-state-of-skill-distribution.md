---
layout: post
title: "The sorry state of skill distribution"
date: 2026-06-03 11:00:00 +0300
categories: [RSS]
tags: [supply-chain, ai-security, scanner-bypass, prompt-injection]
toc: true
---

Trail of Bits bypassed malicious skill scanners in ClawHub, Cisco, skills.sh (Gen, Socket, Snyk), and VirusTotal using simple techniques: prepending 100,000 newlines to evade truncation, embedding shell scripts inside .docx archives (ZIP format with XML), and Python bytecode poisoning. AI skill marketplaces have become a new supply chain vector—skills can contain both code and natural language instructions to compromise agents—yet existing security scanners use static analysis that is easily defeated. The researchers demonstrated these bypasses took less than an hour per attack and submitted hardening patches upstream; the fundamental problem is that static scanning cannot keep pace with adversarial content in a rapidly evolving agent ecosystem.

[Read original article](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/){: .btn .btn-primary }
