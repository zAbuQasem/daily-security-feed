---
layout: post
title: "Securing AI agents: Why guardrail placement is a key design decision"
date: 2026-05-22 00:00:00 +0300
categories: [RSS]
tags: [ai-agents, prompt-injection, llm-security, aws, guardrails]
toc: true
---

This article analyzes how guardrail placement inside an AI agent’s orchestration loop changes the ability to stop indirect prompt injection attacks, using a demo where a benign request to summarize a GitHub issue causes the agent to read attacker-controlled issue text and then invoke a secret-reading tool. The Bedrock-specific example shows that developer-added checks often end up in the Action Group Lambda and must call the ApplyGuardrail API on tool output (`source="OUTPUT"`), because that Lambda only receives the current tool invocation’s parameters rather than the full prompt, memory, and conversation history. That visibility gap means the guardrail can inspect or filter individual tool responses but cannot reason over the entire agent state at earlier decision points where the model decides to call `GetLocalSecret` in the first place. The post contrasts this with self-orchestrated agents that can insert evaluations at multiple hook points around prompt construction, tool execution, and response generation, making it easier to detect prompt-injection-driven control-flow changes instead of just sanitizing downstream content.

[Read original article](https://www.datadoghq.com/blog/securing-ai-agents-guardrail-placement/){: .btn .btn-primary }
