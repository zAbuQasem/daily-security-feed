---
layout: post
title: "Shai-Hulud Goes Open Source"
date: 2026-05-13 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, npm, credential-theft]
toc: true
---

Datadog analyzes the leaked source code of Shai-Hulud, a modular TypeScript/Bun offensive framework attributed to TeamPCP that operationalizes software supply-chain poisoning, credential harvesting, and encrypted exfiltration against both developer workstations and CI/CD environments. The code exposes a staged architecture of loaders, providers, a buffered collector, a dispatcher, sender backends, and mutators, matching previously observed payloads such as `router_init.js`, `setup.mjs`, and `opensearch_init.js`. Its most significant tradecraft includes reading GitHub Actions `Runner.Worker` process memory via `/proc/<pid>/mem` to recover unmasked secrets, harvesting `gh auth token` and `process.env`, and enumerating/decrypting AWS Secrets Manager, SSM, Kubernetes secrets, and HashiCorp Vault data using custom credential resolution logic. The source also shows evolution toward stealth and persistence, including sigstore provenance on malicious releases and AI-agent integration, making this a high-signal look at a real-world supply-chain framework rather than just another campaign summary.

[Read original article](https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/){: .btn .btn-primary }
