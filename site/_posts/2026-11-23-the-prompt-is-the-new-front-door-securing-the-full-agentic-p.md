---
layout: post
title: "The Prompt Is the New Front Door: Securing the Full Agentic Path on AWS"
date: 2026-11-23 13:00:00 +0300
categories: [RSS]
tags: [ai-security, prompt-injection, cloud, agent-security, detection-engineering]
toc: true
---

Article introduces the agentic security model for AWS: treating the full path from user prompt through LLM, MCP server, backend API, to data as a single attack surface. Describes three attack classes—direct prompt injection, indirect injection via embedded data in documents/emails, and multi-stage campaigns that bypass prompt inspection by targeting APIs directly. Proposes defensive framework combining Agentic Security Posture Management (discovery and risk analysis) with Agentic Detection and Response (runtime protection across triggers, LLM, MCP, and API layers). Key insight: single-point (gateway-only) prompt protection misses attacks that skip the LLM entirely and target exposed MCP/API backends; multifocal out-of-band and inline detection with full-path correlation is necessary. Relevant to teams deploying AI agents on cloud infrastructure with privileged tool access.

[Read original article](https://salt.security/blog/the-prompt-is-the-new-front-door-securing-the-full-agentic-path-on-aws){: .btn .btn-primary }
