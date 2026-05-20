---
layout: post
title: "Coverage-Driven Sustained Testing (CDST): A Graph-Oriented Model for Open-Ended Agentic Workflows"
date: 2026-05-19 04:00:00 +0300
categories: [RSS]
tags: [agentic-workflows, pentesting, coverage, llm, automation]
toc: true
---

TrustedSec proposes Coverage-Driven Sustained Testing (CDST), a graph- or matrix-based orchestration model for agentic security testing that generates new work from uncovered areas instead of stopping when an initial task list is exhausted. The core mechanism tracks partial coverage across dimensions such as vulnerability class, authentication state, input path, technique used, and confidence, then repeatedly selects the most under-explored node (for example, specific endpoints or extracted binary functions) and builds a scoped briefing for a fresh agent context. The article contrasts this with backlog-driven loops like Ralph: findings, credentials, or newly exposed attack surface become first-class nodes that recursively expand the search space rather than merely completing predefined stories. Practically, the model is positioned for open-ended penetration testing and reverse engineering where coverage saturation—not an agent's subjective sense of 'done'—should determine termination.

[Read original article](https://trustedsec.com/blog/coverage-driven-sustained-testing-cdst-agentic-workflows){: .btn .btn-primary }
