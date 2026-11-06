---
layout: post
title: "How we investigated prompt cache misses with Datadog"
date: 2026-11-06 00:00:00 +0300
categories: [RSS]
tags: [ai, observability, cloud, optimization]
toc: true
---

Datadog investigated prompt cache misses in their LLM applications, where repeated requests should reuse cached content but frequently didn't, increasing costs significantly. They identified three technical root causes: non-deterministic request construction from Go map iteration causing tools/files to arrive in different orders between requests, changing request prefixes (timestamps or context injected before reusable content), and missing cache configuration propagation through API layers. Their methodology used observability tools to trace token usage and cache hit/miss rates, correlating effectiveness with request structure. Solutions included deterministic sorting of tools/files and reordering stable instructions before mutable context. The patterns and debugging approach generalize to any system using LLM prompt caching.

[Read original article](https://www.datadoghq.com/blog/prompt-cache-investigation-ccm-agent-observability/){: .btn .btn-primary }
