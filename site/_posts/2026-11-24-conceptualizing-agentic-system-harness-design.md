---
layout: post
title: "Conceptualizing Agentic System Harness Design"
date: 2026-11-24 00:00:00 +0300
categories: [RSS]
tags: [infrastructure, tool, architecture]
toc: true
---

Blog post on designing `llmtty`, a local LLM agent harness around Ollama for trustworthy system interaction. The core design philosophy emphasizes three security-adjacent properties: determinism at the application layer (pure-function projections of append-only journals ensure reproducibility), nothing-silent logging (every decision and failure is typed, classified, and recorded with stable codes), and verifiable outcomes (full audit trail enables line-by-line inspection and undo). Uses JSON-based append-only event logs as the single source of truth; sessions can resume deterministically after failure, storage faults degrade gracefully, and context windowing decisions are owned by application logic, not delegated to the model. Relevant primarily to practitioners building systems that must handle long-running agent sessions with strong auditability requirements.

[Read original article](https://jakewnuk.com/posts/creating-agentic-infra-3-conceptualizing-agentic-system-harness-design/){: .btn .btn-primary }
