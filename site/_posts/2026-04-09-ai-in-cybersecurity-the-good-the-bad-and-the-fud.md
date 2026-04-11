---
layout: post
title: "AI in cybersecurity: The good, the bad, and the FUD"
date: 2026-04-09 03:11:32 +0300
categories: [RSS]
tags: [ai-security, prompt-injection, mcp, supply-chain, detection]
toc: true
---

Red Canary's 2026 Threat Detection Report overview covering the dual-edged role of AI in cybersecurity. On the offensive side, nation-state actors (Iran, China, North Korea) have used LLMs and MCP servers as force multipliers — notably, an Anthropic-identified campaign used Claude to automate 80–90% of tactical cyber espionage operations. The primary threat to AI infrastructure is prompt injection via model hijacking: adversaries plant malicious instructions in public locations (GitHub issues, docs) to trick autonomous agents — which operate with elevated privileges — into pivoting through networks, harvesting credentials, and exfiltrating data. Defensive recommendations focus on least-privilege for AI agents, secrets management (short-lived scoped credentials over long-lived API keys), internal MCP server registries, and environment segmentation isolating public-data agents from sensitive internal systems. The defensive AI angle highlights human-guided SOC agents reducing investigation times from 30+ minutes to under two minutes.

[Read original article](https://redcanary.com/blog/security-operations/ai-in-cybersecurity/){: .btn .btn-primary }
