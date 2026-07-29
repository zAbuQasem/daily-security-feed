---
layout: post
title: "Investigate every security event with an AI agent, without the frontier bill"
date: 2026-07-28 00:00:00 +0300
categories: [RSS]
tags: [detection, ai, logs, machine-learning]
toc: true
---

Datadog presents Mambark, a 96.9M-parameter Mamba state-space model that scores security events with linear-time inference, enabling analysis of contexts spanning tens of thousands of events. The model operates as the first stage in a two-stage detection pipeline, using next-event prediction (negative log-likelihood) as an unsupervised anomaly score, reducing the volume from 10 billion daily events to ~10,000 candidates forwarded to an AI agent. Unlike transformers with quadratic attention cost, Mambark's selective state-space architecture handles slow-unfolding attacks and normalizes heterogeneous telemetry (syslog, auth, network flows, insider threat) through uniform tokenization. The approach matches or exceeds prior benchmarks (F1 1.000 on Thunderbird, 0.999 on BGL, 0.994 on UNSW-NB15), while reducing AI reasoning costs from millions to tens of dollars daily. This enables fleet-scale security detection without expensive frontier LLM calls on every event.

[Read original article](https://www.datadoghq.com/blog/ai/ai-security-detection-pipeline/){: .btn .btn-primary }
