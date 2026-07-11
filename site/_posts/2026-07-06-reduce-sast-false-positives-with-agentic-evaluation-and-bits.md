---
layout: post
title: "Reduce SAST false positives with agentic evaluation and Bits Memories"
date: 2026-07-06 00:00:00 +0300
categories: [RSS]
tags: [sast, detection, false-positive, code-analysis]
toc: true
---

Datadog Static Code Analysis introduces agentic evaluation and Bits Memories to reduce SAST false positives. Agentic evaluation enables the AI to explore repository-wide code paths, validators, and callers when assessing a flagged finding, rather than evaluating code in isolation—for example, discovering that an SSRF-vulnerable function is always called through an allowlist validator. Bits Memories captures organizational knowledge by learning from repeated false positive reports and custom context (e.g., framework behavior, internal validation libraries) scoped per rule, allowing the system to apply team-specific conventions to future assessments. All evaluations are sandboxed with read-only repository access and run through prompt-injection defenses.

[Read original article](https://www.datadoghq.com/blog/sast-triage-agentic-evaluation-bits-memories/){: .btn .btn-primary }
