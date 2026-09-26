---
layout: post
title: "OpenAI GPT-6 Sol: An evaluation"
date: 2026-09-24 13:00:00 +0300
categories: [RSS]
tags: [ai-security, code-quality, vulnerability-analysis, llm]
toc: true
---

SonarSource benchmarks OpenAI's GPT-6 Sol against GPT-6 Astra on 4,444 Java coding tasks (HumanEval, MBPP, ComplexCodeEval). While Sol generates 27% less code and achieves a 2.76 percentage point lower pass rate (83.09% vs 85.85%), the critical finding is that vulnerability density increases 60%—from 178 to 285 per million lines of code. Sol concentrates severe bugs in the blocker tier (56 per mLOC vs 37 for Astra), the most likely to reach production. The evaluation uses systematic static analysis via SonarQube to measure cyclomatic complexity, cognitive complexity, bug density, and vulnerability density, revealing that fewer lines of generated code does not guarantee safer code. This is essential context for organizations adopting AI code generation tools in production pipelines.

[Read original article](https://www.sonarsource.com/blog/open-ai-gpt-6-sol-evaluation/){: .btn .btn-primary }
