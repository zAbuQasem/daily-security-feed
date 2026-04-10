---
layout: post
title: "How We Cut LLM Costs by 59% With Prompt Caching"
date: 2026-04-10 03:12:54 +0300
categories: [RSS]
tags: [llm, ai-security, agentic-systems, prompt-caching]
toc: true
---

ProjectDiscovery details the prompt caching architecture behind Neo, their multi-agent security testing platform, which runs 26-step tasks with 40 tool calls and 20K+ token system prompts per agent. Without caching, costs compound quadratically as every step re-sends the full conversation history. They implement three Anthropic cache breakpoints — static system prompt (1-hour TTL), static tool definitions (sorted to front, 1-hour TTL), and a sliding window on the last tool result (5-minute TTL) — achieving an 84% cache hit rate and 59–70% cost reduction. The key insight is a 'relocation trick': dynamic content like working memory and runtime context was originally mid-prefix and silently invalidating cache hits, so they strip it from system messages and inject it as a tail user message wrapped in XML tags to prevent the model from treating it as a user request.

---

[Read original article](https://projectdiscovery.io/blog/how-we-cut-llm-cost-with-prompt-caching){: .btn .btn-primary }
