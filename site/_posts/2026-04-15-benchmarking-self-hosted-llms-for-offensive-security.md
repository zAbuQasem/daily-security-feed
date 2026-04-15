---
layout: post
title: "Benchmarking Self-Hosted LLMs for Offensive Security"
date: 2026-04-15 03:12:25 +0300
categories: [RSS]
tags: [llm, offensive-security, benchmark, agents, ollama]
toc: true
---

TrustedSec benchmarks self-hosted LLMs on offensive-security tasks by giving each model a minimal agent loop against OWASP Juice Shop: a system prompt, target-specific context, and just two tools for raw HTTP requests and payload encoding. The harness runs locally through Ollama’s OpenAI-compatible API, executes model-generated requests, feeds response bodies back into the conversation, and evaluates success with simple response-string predicates such as JWT prefixes or known LFI file content. The experiment deliberately withholds rich tool documentation, examples, memory management, and orchestration so the results reflect whether models can independently infer payload structure and chain requests rather than being coached by prompt engineering. Across 4,800 runs (six models, eight challenges, 100 attempts each), the article argues that local-model performance should be treated as a lower bound and that tool description quality materially affects success rates in practical offensive agent setups.

[Read original article](https://trustedsec.com/blog/benchmarking-self-hosted-llms-for-offensive-security){: .btn .btn-primary }
