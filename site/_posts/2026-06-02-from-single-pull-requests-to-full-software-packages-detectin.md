---
layout: post
title: "From single pull requests to full software packages: Detecting malicious code at scale"
date: 2026-06-02 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, detection, malware]
toc: true
---

Datadog describes BewAIre, a two-stage LLM-based system for detecting malicious code in supply chain dependencies at scale. A cheap filter phase screens all changes quickly; flagged items escalate to an agentic investigation phase with access to GitHub APIs, file inspection, commit history analysis, and dependency validation tools. The system achieved 99.86% accuracy and eliminated false positives by combining stacked LLM evaluations with active investigation, directly addressing recent supply chain compromises (axios, LiteLLM, Mistral) and enabling detection of obfuscated code injection in package registries.

[Read original article](https://www.datadoghq.com/blog/engineering/scaling-malicious-code-detection/){: .btn .btn-primary }
