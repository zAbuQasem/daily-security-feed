---
layout: post
title: "Secure What Agents Do, Not Just What They Say"
date: 2026-08-31 18:00:00 +0300
categories: [RSS]
tags: [agents, authorization, api-security, architecture]
toc: true
---

This article articulates an important distinction in agentic AI security: agents pose risks not just from prompt injection (model-layer attacks) but from overpermissioning and insecure downstream dependencies. The authors illustrate with a bank agent example where a legitimate request triggers a runtime-assembled path through unauthenticated APIs, hardcoded credentials, exposed internal services, and excessive tool permissions—vulnerabilities invisible at the prompt/response layer. The core insight is that agents decide their execution path at runtime (unlike traditional software), making authorization a live question about what systems they can reach, not a static property. Salt's approach adds discovery (inventory of agents, MCP servers, APIs, permissions) and behavioral detection (runtime baselines for agent-driven activity) to complement model-layer prompt injection defenses.

[Read original article](https://salt.security/blog/secure-what-agents-do-not-just-what-they-say){: .btn .btn-primary }
