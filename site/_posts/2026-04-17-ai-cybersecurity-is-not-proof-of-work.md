---
layout: post
title: "AI cybersecurity is not proof of work"
date: 2026-04-17 03:12:21 +0300
categories: [RSS]
tags: [ai, llm, secure-coding, vulnerability-research]
toc: true
---

This post argues that AI-assisted vulnerability discovery does not scale like proof-of-work systems, because repeated sampling from a weaker model eventually saturates the useful execution paths and reasoning branches it can explore. Using the OpenBSD TCP SACK bug as an example, the author claims the limiting factor is model intelligence rather than raw token volume: a weaker model may notice isolated issues such as missing start-window validation or an integer overflow, but fail to compose them into the actual bug condition where an unexpected NULL-path becomes reachable. The piece also highlights an inverse effect where somewhat stronger models may hallucinate less yet still lack the deeper reasoning needed to connect the primitives, making them less likely to flag the real issue than both noisy weak models and genuinely capable ones. Practically, it is a research-oriented argument about the limits of current LLM-based code auditing and why model quality matters more than brute-force inference throughput for complex bug finding.

[Read original article](http://antirez.com/news/163){: .btn .btn-primary }
