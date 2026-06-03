---
layout: post
title: "How we cut Spark compute costs by 44% with agentic AI and Datadog Jobs Monitoring"
date: 2026-06-01 00:00:00 +0300
categories: [RSS]
tags: [ai-agents, performance, spark, devops, automation]
toc: true
---

Datadog's Referential Data Platform team built an AI agent using Claude and their Jobs Monitoring product to automatically debug Spark performance bottlenecks in ServiceQueryEdge, a daily job processing 27TB and 16 billion records. The agent ingests Spark SQL execution plans, stage metrics, and source code via Model Context Protocol (MCP) to correlate slow operators back to application code, addressing context window exhaustion by delegating data acquisition to scoped subagents. A second validation subagent filters false positives by checking contraindications—whether fixes address measured bottlenecks, whether Spark already handles the optimization, or whether root causes lie upstream—and rates proposals by impact using stage CPU contribution. This multi-agent architecture reduced manual debugging time and achieved 44% compute cost reduction and 60% runtime improvement in their largest datacenter, demonstrating practical patterns for LLM-assisted performance optimization of distributed systems.

[Read original article](https://www.datadoghq.com/blog/using-agentic-ai-with-jobs-monitoring/){: .btn .btn-primary }
