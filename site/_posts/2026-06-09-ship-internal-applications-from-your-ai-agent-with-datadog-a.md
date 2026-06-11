---
layout: post
title: "Ship internal applications from your AI Agent with Datadog Apps"
date: 2026-06-09 00:00:00 +0300
categories: [RSS]
tags: [devops, authorization, secure-credentials, audit, internal-tools]
toc: true
---

Datadog announces Datadog Apps, a platform for building internal applications using AI agents (Claude Code, Cursor) and standard web tech (React, Vite). Applications inherit Datadog's authentication model, RBAC, SSO, and Teams configuration without separate identity systems. Apps connect to external services through the Actions platform with server-side credential resolution—app code references connections by ID only, and Datadog resolves actual secrets at runtime, preventing credential leakage into application code. All user activity flows into Datadog Audit Trail for unified governance and compliance monitoring. Security-relevant for teams building internal tools and seeking to avoid scattered credential management across services.

[Read original article](https://www.datadoghq.com/blog/internal-applications-datadog-apps/){: .btn .btn-primary }
