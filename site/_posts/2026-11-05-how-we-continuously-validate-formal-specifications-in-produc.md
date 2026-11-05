---
layout: post
title: "How we continuously validate formal specifications in production"
date: 2026-11-05 00:00:00 +0300
categories: [RSS]
tags: [formal-verification, runtime-monitoring, distributed-systems, bug-detection]
toc: true
---

Datadog built FETCh (Formal Execution Trace Checker), a system that converts TLA+ formal specifications into runtime monitors to continuously validate production behavior against formal models at scale. The tool addresses a critical limitation of traditional formal methods: specifications can drift from implementation as systems evolve over time, creating false confidence. The authors discovered this problem in Husky, their event database, where a routing logic bug persisted undetected for a year—harmless during normal operation, but capable of crashing the backfill system during recovery. FETCh detects these discrepancies by checking production traces against observable (unbounded) specifications, a novel approach distinct from verifying invariants alone, which can mask violations of the formal model.

[Read original article](https://www.datadoghq.com/blog/engineering/continuous-formal-spec-validation/){: .btn .btn-primary }
