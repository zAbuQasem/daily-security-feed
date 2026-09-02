---
layout: post
title: "The context tax: why your coding agent reads the same 600 lines 400 times"
date: 2026-09-01 13:00:00 +0300
categories: [RSS]
tags: [ai-agents, llm-economics, prompt-caching, context-management]
toc: true
---

This article analyzes the hidden cost of context accumulation when AI coding agents navigate large codebases through grep and file reads. Each file read persists in the conversation and is re-billed as a cache-read token on every subsequent turn; on a single ~800-line PR in SemSitter's own codebase, this reached 152.8 million cache-read tokens (~$41 cost) across 512 model round-trips. The root cause: agents lack semantic understanding and fall back to naive grep, then read whole files, creating a compounding cost that scales with repository size and complexity. SonarSource's solution uses a local semantic graph (UDG) to replace grep/file-slice navigation with targeted semantic queries, reducing round-trips and context bloat.

[Read original article](https://www.sonarsource.com/blog/stop-the-context-tax/){: .btn .btn-primary }
