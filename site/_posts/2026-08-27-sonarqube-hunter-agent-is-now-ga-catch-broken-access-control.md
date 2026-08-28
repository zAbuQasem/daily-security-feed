---
layout: post
title: "SonarQube Hunter Agent is now GA: Catch broken access control and business logic flaws"
date: 2026-08-27 13:00:00 +0300
categories: [RSS]
tags: [idor, business-logic, ai, sast]
toc: true
---

SonarQube Hunter Agent, now generally available, addresses a critical SAST blind spot: broken access control and business logic flaws that pattern-based static analysis cannot detect. Unlike SAST tools that track data flow and injections, Hunter Agent uses an AI reasoning pipeline (Analyze → Explore → Validate Exploitability → Synthesize) to reason through authorization checks, workflow integrity, and session management the way a human security researcher would. The exploitability validation subagent independently confirms each finding before surfacing it, achieving 80–90% precision and detecting 200+ zero-day vulnerabilities in well-audited open source projects. This addresses a real problem: broken access control is OWASP Top 10 #1, found in 100% of tested applications across 1.8M instances, and has cost organizations hundreds of millions (Meta, First American, McDonald's, Yearn Finance). Findings integrate into existing SonarQube workflows as normal issues.

[Read original article](https://www.sonarsource.com/blog/hunter-agent-detects-logical-flaws/){: .btn .btn-primary }
