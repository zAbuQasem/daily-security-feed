---
layout: post
title: "AWS Security Digest #287 - Trust Issues"
date: 2026-11-16 13:00:00 +0300
categories: [RSS]
tags: [supply-chain, cloud, iam, ci-cd, agents]
toc: true
---

AWS Security Digest #287 covers two critical threat narratives: (1) Qubole supply chain attack where compromised IAM user credentials in Qubole's AWS account were leveraged to assume customer roles via cross-account trust relationships, allowing attackers to exfiltrate Lambda environment variables, Secrets Manager secrets, SSM parameters, and entire S3 buckets from compromised customer accounts—many roles were unutilized or undeprovisioned. (2) ARTEX, an open-source LLM-based pentest framework, was observed attacking AWS environments in the wild; researchers traced its behavior through AWS honeypots (MadPot), where agents leaked their entire campaign memory in requests, revealing attackers targeting crypto exchanges with deepfake selfie checks. Both incidents exemplify active supply chain and cloud IAM abuse techniques with verified wild exploitation.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-287){: .btn .btn-primary }
