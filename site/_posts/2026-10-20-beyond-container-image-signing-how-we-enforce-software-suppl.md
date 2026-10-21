---
layout: post
title: "Beyond container image signing: How we enforce software supply chain policies at Datadog"
date: 2026-10-20 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, container, attestation, policy]
toc: true
---

Datadog's Turnstile system extends container image signing by generating cryptographically signed attestations across an artifact's lifecycle and evaluating them against environment-specific policies. Image signing alone cannot detect supply chain compromises introduced before the build (malicious source changes, poisoned dependencies, compromised runners); Turnstile addresses this gap by collecting and binding attestations (commit safety, source provenance, PR approvals, build metadata, SBOMs) using a modified in-toto framework. Attestations are queried and verified at deployment time against policies that can vary by environment (dev vs. production). This operationalizes SLSA threat model principles for enterprise-scale policy enforcement across tens of thousands of deployments daily, enabling organizations to answer whether an artifact satisfies security requirements—not just whether it has been tampered with post-signing.

[Read original article](https://www.datadoghq.com/blog/engineering/software-supply-chain-policy-enforcement/){: .btn .btn-primary }
