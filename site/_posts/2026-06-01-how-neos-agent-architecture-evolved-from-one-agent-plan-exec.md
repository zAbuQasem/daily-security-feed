---
layout: post
title: "How Neo's Agent Architecture Evolved: From One Agent → Plan, Execute & Verify"
date: 2026-06-01 18:28:00 +0300
categories: [RSS]
tags: [security-tooling, automation, architecture, llm, devsecops]
toc: true
---

ProjectDiscovery explains how their Neo security agent evolved from a single-agent design to a multi-agent orchestrator system to handle long-running security assessments. The original architecture hit context window limits when tasks accumulated large tool outputs and security evidence that couldn't be effectively summarized. The new design uses an orchestrator that delegates to specialized subagents (browser-agent, sandbox-agent, recon-agent), with each subagent returning concise summaries rather than full execution details, enabling tasks that run up to 14.7 hours with 2,154 LLM steps. The architecture separates the agent loop from an isolated sandbox container where commands execute, allowing horizontal scaling and persistent filesystems across sessions.

[Read original article](https://projectdiscovery.io/blog/neo-agent-architecture){: .btn .btn-primary }
