---
layout: post
title: "The Acceptance Gap: Why AI-Generated Code Still Fails to Become Shipped Work"
date: 2026-09-29 13:00:00 +0300
categories: [RSS]
tags: [devops, code-quality, development, metrics]
toc: true
---

SonarSource analyzes the 'acceptance gap' — the widening chasm between AI code generation and production shipment. The article argues that generated code fails to ship not due to generation quality but due to late-stage verification: review backlogs, test failures, security findings, and rework loops discovered post-merge. Drawing on industry telemetry (22,000 developers, 623M commits), it shows AI-assisted PRs merge at half the rate of human-authored code, wait 5x longer for review, and account for 24% of tracked issues surviving to production. The fix is upstream verification: moving checks into IDEs and pre-commit gates so feedback is fast and cheap, with metrics tracking acceptance rate, time-to-merge, rework rate, and escaped defects rather than lines generated.

[Read original article](https://www.sonarsource.com/blog/the-acceptance-gap/){: .btn .btn-primary }
