---
layout: post
title: "[Deprecated] Break LLM Workflows with Claude's Refusal Magic String"
date: 2026-05-05 21:10:50 +0300
categories: [RSS]
tags: [llm, denial-of-service, prompt-injection, anthropic, rag]
toc: true
---

The article analyzes a now-patched Anthropic behavior where a documented test token, `ANTHROPIC_MAGIC_STRING_TRIGGER_REFUSAL_...`, deterministically caused Claude 4 streaming responses to terminate with `stop_reason: "refusal"` and no refusal text. Nick Frichette shows how this becomes an application-layer denial-of-service primitive when untrusted content is inserted into prompt context, such as user input, RAG documents, tool output, logs, or shared chat history. The key failure mode is persistence: if the poisoned string remains in replayed conversation state, subsequent requests keep refusing until the offending context is pruned or the session is reset. Although the behavior is deprecated and explicitly framed as an integration risk rather than a model vulnerability, the write-up is useful for LLM workflow defenders because it maps concrete mitigations like refusal-aware state handling, context sanitation, filtering known trigger strings, and monitoring refusal spikes.

[Read original article](https://hackingthe.cloud/ai-llm/deprecated/claude_magic_string_denial_of_service/){: .btn .btn-primary }
