---
layout: post
title: "How we fine-tuned a faster model for Patterns on Baseten"
date: 2026-11-18 00:00:00 +0300
categories: [RSS]
tags: [ml-observability, fine-tuning, llm, mlops, baseten]
toc: true
---

Datadog optimized its Patterns LLM observability feature by fine-tuning Qwen 3.5 9B instead of relying on frontier models for trace summarization, which accounted for 80% of p99 cost and 50% of latency. Using production LLM span data as training examples and Baseten's Loops SDK, the fine-tuned model achieved 93% pass rate versus 45% for the base model and reduced generation time from ~45 seconds to <1 second per interaction. The team introduced 'pup finetune,' a CLI extension that automates the fine-tuning workflow via a coding agent while maintaining cost and data controls—crucially, it treats trace content as untrusted data to prevent instruction injection attacks. The approach demonstrates practical cost optimization for LLM applications through targeted fine-tuning with safety guards in place.

[Read original article](https://www.datadoghq.com/blog/fine-tuning-patterns-baseten/){: .btn .btn-primary }
