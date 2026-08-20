---
layout: post
title: "Putting models to the secure coding test: Plan vs default mode"
date: 2026-08-19 00:00:00 +0300
categories: [RSS]
tags: [llm-security, idor, secure-coding, sast, authentication]
toc: true
---

Datadog Security Labs evaluated how well coding agents (Claude Sonnet 5, Cursor Composer 2.5, GPT 5.5) generate secure code by comparing default mode against plan mode when scaffolding a document portal with JWT/session auth, file upload, and role-based access. Using SAST/SCA scanning and code audits, the research found that IDOR vulnerabilities appeared consistently across all models in all modes—agents failed to implement ownership verification on read/download routes despite correctly protecting delete operations. Additional findings included MIME-type validation bypasses on file uploads, inconsistent CSRF protection, rate-limiting gaps on authentication endpoints, and functional regressions (broken password-reset links, session handling bugs). The article demonstrates that coding agents, despite their speed and accessibility, require substantial security review and architectural guardrails before production deployment, with authorization checks being the most commonly overlooked area.

[Read original article](https://securitylabs.datadoghq.com/articles/putting-models-to-the-secure-coding-test-plan-vs-default-mode/){: .btn .btn-primary }
