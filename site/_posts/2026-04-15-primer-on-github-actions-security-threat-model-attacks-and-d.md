---
layout: post
title: "Primer on GitHub Actions Security - Threat Model, Attacks and Defenses (Part 1/2)"
date: 2026-04-15 03:12:29 +0300
categories: [RSS]
tags: [ci-cd, supply-chain, oidc, defense]
toc: true
---

This primer maps the GitHub Actions threat model around workflows, runners, repository secrets, the built-in GITHUB_TOKEN, and third-party actions, showing how CI/CD automation becomes an attack surface. It highlights common abuse paths such as attacker-controlled pull requests, unsafe trigger choices like pull_request_target, over-privileged workflow permissions, and compromised or unpinned external actions that execute inside trusted pipelines. The defensive guidance focuses on isolating untrusted code, reducing token and secret scope, pinning actions to immutable SHAs, and enforcing review or environment protections before sensitive jobs run. For organizations using Actions to build, publish, or deploy software, these controls matter because workflow misconfigurations can lead to repository takeover, package supply-chain abuse, or theft of cloud credentials issued through OIDC federation.

[Read original article](https://www.wiz.io/blog/github-actions-security-threat-model-and-defenses){: .btn .btn-primary }
