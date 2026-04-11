---
layout: post
title: "CI/CD security: How to secure your GitHub ecosystem"
date: 2026-04-09 03:11:38 +0300
categories: [RSS]
tags: [ci-cd, supply-chain, detection, npm]
toc: true
---

Datadog's threat modeling guide for GitHub CI/CD security maps attack surfaces across inputs (workflows, secrets, source code), identities (PATs, SSO, GitHub Apps), and risks (malicious code execution, data exfiltration). The post details detection strategies using GitHub audit logs and SAST tools for threats like injected workflow files, dependency poisoning, and mass repo cloning via compromised PATs. A significant portion covers the Shai-Hulud npm worm family (late 2025), which compromised 1,000+ npm packages and 14,000+ GitHub repos by embedding TruffleHog in package.json install scripts to harvest and exfiltrate secrets to attacker-controlled webhooks and public repos. The worm's self-replication mechanism — publishing new poisoned package versions upon discovering npm/GitHub credentials — makes it a canonical supply chain propagation case. Detection opportunities include monitoring for environment variable enumeration in CI jobs, unexpected curl/wget usage in workflows, and anomalous PAT activity via GitHub audit logs.

[Read original article](https://www.datadoghq.com/blog/secure-your-github-ecosystem/){: .btn .btn-primary }
