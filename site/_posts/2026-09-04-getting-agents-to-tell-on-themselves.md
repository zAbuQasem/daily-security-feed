---
layout: post
title: "Getting Agents to tell on themselves"
date: 2026-09-04 10:02:34 +0300
categories: [RSS]
tags: [ai-agents, deception, detection, social-engineering, exploitation]
toc: true
---

Thinkst introduces Agent Provocateur, a deception-based detection tool that exploits fundamental weaknesses in AI agent behavior. Agents are vulnerable because they operate on attacker-controlled output and are highly suggestible to social engineering, even without explicit prompt injection. Agent Provocateur deploys a fake backend service that agents encounter during reconnaissance and can be tricked into revealing sensitive information (SSH keys, MAC addresses, usernames, process context) and executing arbitrary code (reverse shells) through conversational manipulation. Testing across multiple frontier models shows 100% detection rate, with practical implications for defending against autonomous agent-driven infrastructure attacks.

[Read original article](https://blog.thinkst.com/2026/09/getting-agents-to-tell-on-themselves.html){: .btn .btn-primary }
