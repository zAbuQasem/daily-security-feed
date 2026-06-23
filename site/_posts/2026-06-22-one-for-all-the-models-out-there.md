---
layout: post
title: "One for all the models out there!"
date: 2026-06-22 09:59:45 +0300
categories: [RSS]
tags: [detection, ai-agents, honeypot, mcp]
toc: true
---

Thinkst released an MCP Canarytoken—a deception-based detection mechanism that alerts when LLM agents (Claude Code, Copilot CLI, Cursor, VSCode) access and enumerate MCP servers. The token offers two alerting modes: on initial MCP connection or on actual tool invocation, allowing defenders to catch agentic reconnaissance with low noise. A key strength: agents will invoke the token via curl if MCP is organizationally disabled, bypassing attempted restrictions and still triggering alerts. The token integrates into development tool configurations (.claude/mcp.json, .copilot/mcp-config.json, etc.) as a canary to detect unauthorized agent activity in code repositories.

[Read original article](https://blog.thinkst.com/2026/06/one-for-all-the-models-out-there.html){: .btn .btn-primary }
