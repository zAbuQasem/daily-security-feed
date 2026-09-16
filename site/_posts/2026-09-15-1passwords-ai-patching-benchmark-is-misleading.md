---
layout: post
title: "1Password's AI patching benchmark is misleading"
date: 2026-09-15 11:00:00 +0300
categories: [RSS]
tags: [ai-security, methodology, vulnerability-patching, benchmark]
toc: true
---

Trail of Bits critiques 1Password's published AI patching benchmark, exposing methodological flaws in the headline-grabbing 26% clean-fix rate. The study suffered from sampling bias (six deliberately complex vulnerabilities), deliberately instructing agents to apply wrong fixes (22% of trials), prohibiting code testing in 36% of trials, and mismatched model reasoning settings. When re-analyzed correctly, Trail of Bits found 86% of 1Password's patches blocked supplied exploits. The post also provides real-world data from 2,265 vulnerabilities in security assessments, showing developers themselves fail to fully resolve issues 12.5% of the time on first attempt—suggesting AI performance claims require careful contextualization. Trail of Bits releases two new agent skills for patch validation and review walkthrough.

[Read original article](https://blog.trailofbits.com/2026/09/15/1passwords-ai-patching-benchmark-is-misleading/){: .btn .btn-primary }
