---
layout: post
title: "Wiz Red Agent Finds Its Way Into Snowflake’s Internal Jira Through a Flaw in a GitHub Copilot–Assisted PR"
date: 2026-08-17 14:00:00 +0300
categories: [RSS]
tags: [ci-cd, supply-chain, secrets-exfiltration, ai-assisted]
toc: true
---

Wiz's Red Agent autonomously discovered and exploited a GitHub Actions workflow injection vulnerability in Snowflake's codebase within five days of deployment. The flaw was present in a pull request assisted by GitHub Copilot but was missed by GitHub's automated AI code review, allowing execution of arbitrary commands in the CI/CD pipeline and access to sensitive data in Snowflake's internal Jira. This demonstrates a critical vulnerability class where AI-assisted code generation can introduce subtle injection flaws that bypass both human reviewers and automated security scanning, with direct access to secrets and sensitive infrastructure.

[Read original article](https://www.wiz.io/blog/red-agent-snowflake-copilot-cicd-bug){: .btn .btn-primary }
