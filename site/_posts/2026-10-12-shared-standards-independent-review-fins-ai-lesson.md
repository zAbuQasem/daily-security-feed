---
layout: post
title: "Shared standards, independent review: Fin's AI lesson"
date: 2026-10-12 13:00:00 +0300
categories: [RSS]
tags: [code-review, ai, verification, workflow, standards]
toc: true
---

AI coding agents accelerate implementation but shift quality assurance bottlenecks to verification. Fin addressed this by introducing size-based PR limits (small changes auto-approve, larger ones require review), unifying standards between generation and review agents to prevent drift, and critically, tracking verifier quality on both recall and false positives. A cheaper model passed offline evaluation with identical recall but generated excessive false positives once deployed, eroding developer trust within a week—demonstrating that noise is as damaging as missed catches. The team now measures verifiers using production signals (thumbs up/down on comments, soft adoption of suggestions, human overrides of flags) rather than synthetic benchmarks. The core insight: when verification is built into the workflow, developers will ignore feedback if the signal-to-noise ratio drops, making precision essential to delivery velocity.

[Read original article](https://www.sonarsource.com/blog/when-agents-outpace-the-organization/){: .btn .btn-primary }
