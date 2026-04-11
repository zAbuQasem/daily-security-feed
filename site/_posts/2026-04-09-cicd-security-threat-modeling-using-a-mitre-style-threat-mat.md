---
layout: post
title: "CI/CD security: threat modeling using a MITRE-style threat matrix"
date: 2026-04-09 03:11:37 +0300
categories: [RSS]
tags: [ci-cd, supply-chain, threat-modeling, detection, mitre]
toc: true
---

Datadog presents a MITRE ATT&CK-style threat matrix specifically mapped to CI/CD pipeline attack paths, covering tactics from Reconnaissance through Impact across SCM, CI, and CD trust boundaries. The matrix enumerates concrete techniques such as dependency tampering, IaC injection, CI runner image implants, cloud metadata credential access (IMDS), and pipeline log exfiltration — drawing from historical attacks and frameworks like OWASP Top 10 CI/CD Risks and Microsoft's DevOps Threat Matrix. The post explains how attackers exploit overly permissive SCM access policies, third-party integrations, and PR-triggered pipeline execution to pivot from initial access to secret theft and downstream supply chain poisoning. It frames the matrix as a threat modeling tool for identifying detection gaps and evaluating countermeasures across the software delivery lifecycle. Part 2 applies the model specifically to GitHub environments with historical attack cases.

[Read original article](https://www.datadoghq.com/blog/ci-cd-threat-matrix/){: .btn .btn-primary }
