---
layout: post
title: "Agents didn’t break code review, they exposed it"
date: 2026-11-17 14:00:00 +0300
categories: [RSS]
tags: [code-review, ci-cd, ai-security, supply-chain, verification]
toc: true
---

This article argues that AI agents have exposed, not broken, existing weaknesses in code review practices. Traditional human code review was unreliable at scale—reviewers rubber-stamp large pull requests without full comprehension—and delivery pressure now makes this worse by pushing developers to skip review entirely of AI-generated code. The author advocates a multi-layered verification strategy combining LLM-based code review (fast, repeatable, but catches only ~33% of issues) with deterministic static analysis, compiler checks, tests, and exploratory testing. The key insight is that gaps between developer intent and implementation—where agents may write syntactically perfect code that misses security or business requirements—require both AI reasoning and deterministic analysis to detect. Teams must engineer verification into every loop, from guardrails during generation to quality gates at merge, since delivery pressure makes willpower and heroic review hours unsustainable.

[Read original article](https://www.sonarsource.com/blog/ai-code-verification-has-to-scale-past-the-human-reviewer/){: .btn .btn-primary }
