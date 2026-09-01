---
layout: post
title: "Don't Let Abliteration Abliterate Your Bug Hunting: Discovering Verdict Bias in Uncensored Models"
date: 2026-09-01 06:00:00 +0300
categories: [RSS]
tags: [ai-security, vulnerability-research, model-bias, supply-chain]
toc: true
---

This research demonstrates that abliterated (uncensored) large language models exhibit systematic verdict bias when used for vulnerability discovery — they report 3–4× more false positive findings than their base models on identical code analysis tasks. The author discovered this while testing local open-weight models against known CVEs; abliterated variants would "confirm" candidates that the base models correctly rejected, including a false heap overflow claim in FreeBSD's auth_unix.c that is actually bounded by MAX_AUTH_BYTES. Verdict bias is defined as a model's disposition to return positive verdicts under uncertainty, independent of evidence; chain-of-thought traces show models recognizing correct bounds analysis, then overriding themselves. The practical implication is significant for security researchers using modified models to bypass guardrails during bug hunting — the weight modifications that remove safety constraints appear to also degrade decision calibration under ambiguity, generating substantially more triage work without finding real bugs.

[Read original article](https://clearbluejar.github.io/posts/does-abliteration-skew-your-bug-hunting/){: .btn .btn-primary }
