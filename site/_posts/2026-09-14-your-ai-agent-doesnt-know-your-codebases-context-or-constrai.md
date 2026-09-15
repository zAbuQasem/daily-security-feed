---
layout: post
title: "Your AI agent doesn't know your codebase's context or constraints, and that's costing you"
date: 2026-09-14 13:00:00 +0300
categories: [RSS]
tags: [ai-security, llm-security, code-quality]
toc: true
---

SonarSource's empirical study of 4,444 LLM code generation tasks in Java found that all tested models exhibit critical security deficiencies: code smells comprise 89–94% of issues, and security vulnerabilities are widespread, with Claude Sonnet 4 producing 93% more BLOCKER-severity bugs than its v3.7 predecessor (13.71% vs 7.10%), and Llama 3.2 90B reaching 70.73% BLOCKER vulnerability rate. GitClear's analysis of 211M lines of committed code (2020–2024) shows architectural drift from AI-generated code: duplicated 5-line blocks jumped from 1.8% of commits in 2023 to 6.7% in 2024 (fourfold increase), moved code dropped from 24.8% to 9.5% of changed lines (agents clone rather than refactor), and co-changed clones are involved in bugs 57% of the time on average. The article argues that context-free code generation optimizes for local plausibility rather than architectural fitness; providing agents with codebase constraints upfront reduces both token cost (7–8.5% savings) and drift-induced rework compared to downstream linting and code review.

[Read original article](https://www.sonarsource.com/blog/your-ai-agent-doesnt-know-your-codebases-context-or-constraints/){: .btn .btn-primary }
