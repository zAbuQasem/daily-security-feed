---
layout: post
title: "Jev as a judge: How counterfeit policy steers Jev"
date: 2026-10-15 00:00:00 +0300
categories: [RSS]
tags: [ai-security, prompt-injection, adversarial-ml, security-evaluation, llm]
toc: true
---

Datadog Security Labs evaluates Jev, TypeSafe AI's new structured-decision model used in production security controls (LangChain tool-risk gating, Vercel eve), to assess whether attacker-controlled conversational content can steer its classification decisions and bypass security checks. The research tests Jev's robustness against prompt injection using 12,295 labeled samples across four public datasets with defined attack categories (policy evasion, indirect injection, credential access, privilege escalation, tool abuse, and poisoning). Using Jev's Noul (probability) and Choice (multi-category) primitives, the researchers systematically evaluate whether malicious framing or embedded instructions in tool arguments can manipulate Jev's risk assessments—a critical threat model for AI-driven security controls in production deployment.

[Read original article](https://securitylabs.datadoghq.com/articles/jev-as-a-judge-how-counterfeit-policy-steers-jev/){: .btn .btn-primary }
