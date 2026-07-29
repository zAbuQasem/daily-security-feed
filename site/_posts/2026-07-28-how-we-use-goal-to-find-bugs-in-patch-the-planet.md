---
layout: post
title: "How we use /goal to find bugs in Patch the Planet"
date: 2026-07-28 11:00:00 +0300
categories: [RSS]
tags: [vulnerability-research, supply-chain, ai-security, threat-modeling]
toc: true
---

Trail of Bits describes three core techniques for using Codex's `/goal` feature to autonomously discover vulnerabilities in high-value open-source projects (Rust, curl, zlib, Keycloak) as part of their Patch the Planet initiative. The key innovations are: (1) meta-prompting Codex to draft its own goal prompts based on threat models rather than manual specification, (2) defining precise success criteria (the outcome) while letting the model choose its execution path, and (3) assigning one outcome per agent to prevent optimization conflicts. The methodology has found critical bugs including a Rust soundness hole, multiple variant CVEs via automated Semgrep rules, and two potential privilege-escalation vulnerabilities in Keycloak's SAML authentication component. Trail of Bits also developed aicov tooling to verify actual code coverage and prevent models from skipping codebase sections.

[Read original article](https://blog.trailofbits.com/2026/07/28/how-we-use-goal-to-find-bugs-in-patch-the-planet/){: .btn .btn-primary }
