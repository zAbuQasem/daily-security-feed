---
layout: post
title: "What NIST should know when updating the SSDF for AI"
date: 2026-06-18 16:00:00 +0300
categories: [RSS]
tags: [ai, supply-chain, prompt-injection, ci-cd, sdlc]
toc: true
---

SonarSource analyzes how the NIST Secure Software Development Framework (SSDF) must evolve to address AI-generated code. The article identifies three structural problems: (1) non-determinism means AI code cannot self-certify compliance with training or standards; (2) agentic code volume (14x larger patches than developer-written) exceeds human review capacity past ~20 files, requiring mandatory automated verification; (3) AI agents accessing repos and CI/CD systems introduce novel adversarial attack surfaces including prompt injection, memory-based privilege escalation, and backdoor persistence via adversarial inputs. Data from 750 billion lines analyzed shows unverified AI code produces ~1,200 security issues per million lines. The framework must mandate deterministic verification layers (code review + SCA + CI validation) and explicitly treat agentic systems as active attack surfaces, not just unreliable tools.

[Read original article](https://www.sonarsource.com/blog/what-nist-should-know-when-updating-the-ssdf-for-ai/){: .btn .btn-primary }
