---
layout: post
title: "Bring your own hook: a 5-line PostToolUse template calling sonar analyze agentic"
date: 2026-08-17 13:00:00 +0300
categories: [RSS]
tags: [devtools, sast, ci-cd, defensive]
toc: true
---

A technical tutorial from SonarQube on integrating their Agentic Analysis into Claude Code's PostToolUse hook system with a 5-line bash script. The hook uses `sonar analyze agentic --depth DEEP` to ship modified files to SonarQube Cloud, which restores dependency graph and type information from prior CI analysis and performs SAST including cross-file taint analysis, returning findings via exit code 51 for Claude to remediate. Covers hook event parsing via jq, exit-code semantics (0=clean, 51=issues, others=errors), error handling strategies (fail-open vs fail-closed), and advisory context attachment. Relevant for developers seeking programmatic control over SonarQube integration scope and blocking behavior rather than automatic setup.

[Read original article](https://www.sonarsource.com/blog/bring-your-own-hook/){: .btn .btn-primary }
