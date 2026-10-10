---
layout: post
title: "OpenAI GPT-6.1 Sol: An evaluation"
date: 2026-10-09 13:00:00 +0300
categories: [RSS]
tags: [ai-security, code-quality, benchmark]
toc: true
---

SonarSource's evaluation of OpenAI's GPT-6.1 Sol reveals a 2.2-point functional improvement (85.29% pass rate) while generating 39.4% more code than GPT-6 Sol across 4,444 Java tasks. Vulnerability density improved 32.4% (285 to 193 per million lines), bug density fell 3.3%, and code smell density dropped 5.2%. However, concurrency-related bugs increased 21% by density and 69% by count, now accounting for 48% of all findings—these are expensive to debug as they produce intermittent failures in production. The model generates safer code per-line but produces substantially higher absolute bug volume, requiring proportionally more triage despite per-line improvements.

[Read original article](https://www.sonarsource.com/blog/openai-gpt-6-1-sol-evaluation/){: .btn .btn-primary }
