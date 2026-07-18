---
layout: post
title: "How we brought agentic workflows to Cloud SIEM with the Datadog MCP Server"
date: 2026-07-17 00:00:00 +0300
categories: [RSS]
tags: [cloud-siem, ai-agents, detection-engineering, platform-security]
toc: true
---

Datadog built MCP (Model Context Protocol) tools for Cloud SIEM to enable AI agents in security workflows. The core challenge is managing a shared context window across growing toolsets; they solved this with progressive disclosure—a schema tool that filters detection rule schemas by rule type and detection method, reducing token usage 15–47% vs. serving full schemas. For bulk triage, they shifted from context-carrying signal IDs to query-based resolution, enabling agents to act on hundreds of signals instead of the 50-signal UI cap. Real user analysis showed 44% of messages involved rule authoring and 25% of customers triaged signals in bulk—patterns that informed tool priority and design.

[Read original article](https://www.datadoghq.com/blog/creating-mcp-tools-for-cloud-siem/){: .btn .btn-primary }
