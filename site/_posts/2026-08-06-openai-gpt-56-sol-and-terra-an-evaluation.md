---
layout: post
title: "OpenAI GPT-5.6 Sol and Terra: An evaluation"
date: 2026-08-06 13:00:00 +0300
categories: [RSS]
tags: [ai, code-quality, vulnerability, supply-chain]
toc: true
---

SonarSource evaluated OpenAI's GPT-5.6 Sol and Terra code generation against GPT-5.5 across 4,444 Java tasks using SonarQube analysis. Sol achieves 81.99% pass rate (up from 78.66%) and generates more complex logic in fewer, longer functions with reduced cyclomatic complexity. However, security vulnerabilities increased from 68 to 197 per million lines of code, with blocker vulnerabilities halving but critical vulnerabilities surging from 20 to 125 per mLOC—a fundamental shift in the threat profile. Concurrency and threading bugs more than doubled to 352 per mLOC, becoming the dominant bug category. The evaluation highlights that stronger code generation comes with shifted risk, moving vulnerabilities into categories that code review often misses.

[Read original article](https://www.sonarsource.com/blog/openai-gpt-5-6-sol-and-terra/){: .btn .btn-primary }
