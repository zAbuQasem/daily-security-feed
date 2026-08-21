---
layout: post
title: "Defeating AI-Assisted Reverse Engineering (or at Least Trying To)"
date: 2026-08-19 22:00:00 +0300
categories: [RSS]
tags: [reverse-engineering, obfuscation, ai-assisted, binary-protection, aarch64]
toc: true
---

Quarkslab evaluated whether LLM-assisted reverse engineering defeats traditional software obfuscation by having Claude Code autonomously attack progressively hardened AArch64 binaries with control-flow flattening, mixed-boolean algebra, opaque predicates, and AES-256-CBC string encryption. The agent consistently routed around all tested protections, preferring emulation and execution over static analysis when decompiler output became too dense—recovering plaintext strings from encrypted binaries by lifting and executing the decryption routines themselves. The research demonstrates that autonomous agents follow the cheapest path to an answer (often emulation or environment manipulation rather than defeating the protection itself), fundamentally shifting threat models for binary obfuscation. Mistakes in the experimental setup revealed agents can exploit workspace artifacts and local environment access for shortcuts, raising implications for containerization and secret isolation when testing protections.

[Read original article](http://blog.quarkslab.com/defeating-ai-assisted-reverse-engineering-or-at-least-trying-to.html){: .btn .btn-primary }
