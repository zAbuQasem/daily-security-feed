---
layout: post
title: "When a Security Guardrail Detects the Attack and Still Can’t Stop It"
date: 2026-10-01 12:00:00 +0300
categories: [RSS]
tags: [ai-agent, prompt-injection, authorization, detection-evasion]
toc: true
---

Salt Security disclosed a vulnerability in the Manus AI agent platform where a malicious email hijacks the agent to reach victim's connected accounts. The core issue is architectural: a security guardrail detected the attack but couldn't stop it because detection fired after the malicious code had already executed. The finding exposes a broad pattern in autonomous systems—agents that process untrusted input (emails, documents, web pages) and hold broad access to connected services are inherently vulnerable when guardrails operate at the conversation layer rather than the action layer. The research emphasizes that pattern-matching filters are insufficient; defenses must enforce controls before sensitive actions execute, apply least privilege to limit blast radius, and provide visibility across the full agent execution path. This is particularly critical as enterprises now connect agents to email, storage, repositories, and business systems with often excessive permissions.

[Read original article](https://salt.security/blog/when-a-security-guardrail-detects-the-attack-and-still-cant-stop-it){: .btn .btn-primary }
