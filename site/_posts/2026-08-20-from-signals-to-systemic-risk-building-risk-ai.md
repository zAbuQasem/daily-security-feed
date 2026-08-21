---
layout: post
title: "From signals to systemic risk: Building Risk AI"
date: 2026-08-20 00:00:00 +0300
categories: [RSS]
tags: [risk-management, ai-security, detection, operational-security]
toc: true
---

Datadog describes a Systemic Risk Detection Pipeline that correlates security and engineering signals (vulnerabilities, incidents, identity permissions, resource exposure, configuration) to move beyond individual finding severity and identify organizational risk paths. The system uses deterministic pattern matching to detect conditions that combine to amplify exposure (e.g., a medium-severity vulnerability on an internet-facing service with excessive identity permissions and access to sensitive data), then applies Risk AI Agents to investigate relationships, contextualize impact, and prioritize remediation. The approach separates deterministic detection from agentic reasoning to preserve explainability and human oversight, scoring risks based on factors like internet exposure, privilege, business criticality, blast radius, and existing controls. This methodology addresses a key operational security challenge: understanding how interconnected weaknesses create systemic risk beyond individual findings.

[Read original article](https://www.datadoghq.com/blog/systemic-risk-ai-agents-datadog/){: .btn .btn-primary }
