---
layout: post
title: "Inside Secretless Analysis: from CI identity to project-scoped access"
date: 2026-11-18 14:00:00 +0300
categories: [RSS]
tags: [ci-cd, supply-chain, oidc, secrets-management, authentication]
toc: true
---

SonarQube Cloud's Secretless Analysis eliminates CI secrets by implementing workload identity federation via OIDC token exchange (RFC 8693). Instead of storing SonarQube tokens as CI secrets—prime targets for supply-chain attacks—GitHub Actions and GitLab CI jobs request a signed OIDC token from their CI platform; SonarQube Cloud validates the token to verify job identity and repository, then exchanges it for a 30-minute project-scoped analysis token. This approach closes the attack surface demonstrated in real compromises: Trivy-action (March 2026), changed-files (CVE-2025-30066), and GhostAction campaigns (3,325+ stolen secrets), which all harvested repository secrets from CI environments. A single reusable workflow works across all repositories without manual token creation, rotation, or storage, available on every SonarQube Cloud plan.

[Read original article](https://www.sonarsource.com/blog/inside-secretless-analysis/){: .btn .btn-primary }
