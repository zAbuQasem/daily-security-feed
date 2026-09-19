---
layout: post
title: "Attacker infrastructure, but vibe-coded: tracking the evolution of credential harvesting platforms"
date: 2026-09-18 00:00:00 +0300
categories: [RSS]
tags: [threat-intelligence, credential-harvesting, aws, llmjacking, exploit-automation]
toc: true
---

Datadog researchers documented two active credential harvesting platforms ("Loot" and "UltraVault") housing 26k–42k stolen credentials, including live API keys for OpenAI (93 live), Gemini (55 live), Anthropic (10 live), and AWS. The platforms provide automated workflows for credential validation via `/api/credentials/validate`, AWS key-pair correlation through `/api/pairs` to recover complete IAM credentials, and exploit chain mapping that recommends CVE-based exploitation vectors (react2shell for CVE-2025-55182, wp2shell, xss2shell targeting WordPress, joomla2shell, and local privilege escalation matrices). Evidence of active abuse includes live Amazon Bedrock calls (GetCallerIdentity, InvokeModel) and regular re-probing to confirm credential validity, with only 2.7% of 42k secrets marked live—suggesting millions of validation attempts against known targets. The infrastructure exemplifies attacker evolution toward AI-assisted operations: LLM-generated dashboards automating reconnaissance, credential management, and exploitation recommendation end-to-end.

[Read original article](https://securitylabs.datadoghq.com/articles/attacker-infrastructure-but-vibe-coded/){: .btn .btn-primary }
