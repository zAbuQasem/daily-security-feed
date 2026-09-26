---
layout: post
title: "From Opus 5 to Opus 5.5: better fixes at 58% less cost in the SonarQube Remediation Agent"
date: 2026-09-25 13:00:00 +0300
categories: [RSS]
tags: [ai-tooling, code-quality, benchmarking, sonarqube]
toc: true
---

SonarSource benchmarks their SonarQube Remediation Agent after upgrading from Claude Opus 5 to Opus 5.5, demonstrating that the newer model improves end-to-end issue resolution by 11.9%, increases merge-ready fix quality by 15.8%, and reduces cost per fix by approximately 58%, while maintaining functional test pass rates. The agent works by generating code fixes in a sandbox, re-running static analysis to validate the fix clears the issue without introducing new ones, and only surfacing verified changes as pull requests—a feedback loop where model quality directly correlates with resolution rate. The 4% wall-clock time increase is minimal and represents a favorable tradeoff, particularly relevant for teams with large code-quality backlogs where the dramatic cost reduction makes comprehensive remediation now economically feasible.

[Read original article](https://www.sonarsource.com/blog/the-sonarqube-remediation-agent-using-claude-opus-5-5/){: .btn .btn-primary }
