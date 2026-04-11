---
layout: post
title: "Introducing our open source AI-native SAST"
date: 2026-04-11 03:10:17 +0300
categories: [RSS]
tags: [sast, llm, static-analysis, appsec, open-source]
toc: true
---

Datadog released an open source "AI-native" SAST engine that replaces purely rule-based scanning with a pipeline that first heuristically selects risky files, then pulls related functions/files to give an LLM enough code context to reason about exploitable paths. The analysis stage looks for issues such as SQL injection, command injection, path traversal, and XSS by examining user-controlled inputs and how they flow through code, then a post-processing layer uses both heuristics and an LLM-based false-positive filter to classify findings and suppress non-issues. To control cost, the system does a full repository scan once and then switches to incremental rescans only when a file or its surrounding context changes, reducing the number of expensive multi-call LLM analyses. On OWASP Benchmark tests, Datadog reports materially higher recall than its traditional SAST pipeline for context-dependent bugs, including gains from 59% to 90% for command injection, 63% to 86% for SQL injection, and 65% to 93% for XSS.

---

[Read original article](https://www.datadoghq.com/blog/open-source-ai-sast/){: .btn .btn-primary }
