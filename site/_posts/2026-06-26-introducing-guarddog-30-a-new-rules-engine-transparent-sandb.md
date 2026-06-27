---
layout: post
title: "Introducing GuardDog 3.0: A new rules engine, transparent sandboxing, and more"
date: 2026-06-26 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, malware, detection, python, npm]
toc: true
---

GuardDog 3.0, Datadog's open-source malicious package detector, migrated its rule engine from Semgrep to YARA to improve performance and reduce memory overhead on large-scale scans. The release introduces a new risk-scoring engine that combines capability detection (what a package can do) and threat indicators (suspicious domains, deobfuscation routines, credential access patterns) to quantify maliciousness across a 0–10 scale based on attack chain completeness, specificity, and sophistication. GuardDog 3.0 also adds transparent sandboxing via nono-py, running extraction and analysis in an isolated environment with restricted network and filesystem access as defense-in-depth against vulnerabilities in the scanning tool itself. The tool now supports PyPI, npm, and Golang module scanning with a framework for detecting typical malware attack stages: initial access, post-compromise credential exfiltration, and persistence injection.

[Read original article](https://securitylabs.datadoghq.com/articles/guarddog-3-0-release/){: .btn .btn-primary }
