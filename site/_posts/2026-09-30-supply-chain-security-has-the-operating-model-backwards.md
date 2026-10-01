---
layout: post
title: "Supply Chain Security Has the Operating Model Backwards"
date: 2026-09-30 12:47:21 +0300
categories: [RSS]
tags: [supply-chain, malware, runtime-security, terraform, detection]
toc: true
---

Aquasec argues supply chain security should invert its operating model: runtime context and execution behavior should drive upstream prioritization, not sit passively at the end. The article details the Graphalgo campaign (Terraform providers and Go modules with conditional activation via SHA-256 hashes or specific data values), showing how dormant malicious code evades static scanning. A 2023 Sysdig report found 87% of production container images have critical vulnerabilities, yet only 15% are actually loaded at runtime—85% wasted effort. Runtime enforcement can detect and block novel behaviors at execution time without prior artifact discovery, and those blocks feed back upstream as build policies. This shifts security from finding-first to production-evidence-first without abandoning upstream controls.

[Read original article](https://www.aquasec.com/blog/supply-chain-security-has-the-operating-model-backwards/){: .btn .btn-primary }
