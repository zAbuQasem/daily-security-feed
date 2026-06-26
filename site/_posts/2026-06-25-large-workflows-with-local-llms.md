---
layout: post
title: "Large Workflows with Local LLMs"
date: 2026-06-25 04:00:00 +0300
categories: [RSS]
tags: [llm, reverse-engineering, mcp, automation, ai-tools]
toc: true
---

This article explores the practical challenges of using local LLMs for security workflows like reverse engineering and code analysis, comparing smaller models (4B–9B) against larger ones (20B–35B) and frontier models. The author identifies three key pain points: context window limitations (most models capped at 256K), LLM tool control (models ignore instructions and guess undefined tool names), and context degradation over long workflows. To address these, the author built a Python library interfacing with OpenAI-compatible endpoints and MCP servers to auto-generate modular harnesses that divide tasks into smaller chunks, implement per-tool access control via validation, and enforce tool-call timeouts to prevent infinite loops. Real-world testing with binaries containing 700+ and 10,000+ functions revealed that tool validation, prompt engineering, and output size management are critical for stability.

[Read original article](https://trustedsec.com/blog/large-workflows-with-local-llms){: .btn .btn-primary }
