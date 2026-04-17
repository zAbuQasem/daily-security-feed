---
layout: post
title: "Spotting CI/CD misconfigurations before the bots do: Securing GitHub Actions with Datadog IaC Security"
date: 2026-04-17 03:12:32 +0300
categories: [RSS]
tags: [ci-cd, iac, supply-chain, detection]
toc: true
---

Datadog analyzes common GitHub Actions misconfigurations that enabled recent CI/CD attacks, focusing on cases where user-controlled values like PR titles, commit messages, and branch names are interpolated into `run` blocks via `${{ }}` and become shell-injection primitives. The post also covers high-risk workflow patterns such as `pull_request_target` combined with checkout of untrusted fork code, missing explicit `permissions`, mutable action tags instead of full commit SHAs, deprecated `set-env`/`add-path` commands, and overprivileged tokens that can be abused for repo takeover or artifact tampering. It describes how static analysis on workflow YAML can catch these issues at review time by flagging dangerous triggers, unsafe conditions, unpinned actions and images, cache-poisoning paths, and privileged Dependabot execution contexts directly in pull request diffs. The piece is vendor-backed, but it still provides a useful defensive checklist for securing GitHub Actions against secret exfiltration, supply-chain abuse, and runner-side lateral movement.

[Read original article](https://www.datadoghq.com/blog/github-actions-iac-security/){: .btn .btn-primary }
