---
layout: post
title: "How We Hijacked an AI Agent With a Single Email"
date: 2026-10-01 12:00:00 +0300
categories: [RSS]
tags: [prompt-injection, ai-agents, indirect-injection, oauth-abuse, authorization-escalation]
toc: true
---

Salt Labs demonstrated a prompt injection attack against Manus, an AI agent platform with multi-service integrations (Gmail, cloud storage, code repos). By embedding malicious instructions in an email, attackers could hijack the agent's execution context within the user's sandbox, gaining access to OAuth tokens and performing unauthorized actions across integrated services without user interaction or credential theft. The core vulnerability—using untrusted content (email body) as agent instructions—has been patched, but the research highlights a critical architectural lesson: post-execution guardrails cannot protect autonomous systems. Security must extend to what agents actually do, not just what prompts they receive.

[Read original article](https://salt.security/blog/how-we-hijacked-an-ai-agent-with-a-single-email){: .btn .btn-primary }
