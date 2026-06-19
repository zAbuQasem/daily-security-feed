---
layout: post
title: "AI is writing more of your Terraform"
date: 2026-06-18 16:00:00 +0300
categories: [RSS]
tags: [terraform, iac, cloud, ai-security, misconfiguration]
toc: true
---

AI agents generate insecure Terraform at alarming rates (19–40% pass rates on real-world tasks per NeurIPS/FSE/ICSE benchmarks), failing in four predictable ways: permissive IAM defaults, omitted security blocks, hardcoded credentials, and stale provider attributes. These misconfigurations—wildcard `Action: "*"`, missing `storage_encrypted`, plaintext secrets in Git—mirror patterns behind real cloud breaches. The article details each failure mode with concrete examples and explains why HCL is harder for LLMs than YAML/JSON, making detection at merge-gate critical as AI authorship scales.

[Read original article](https://www.sonarsource.com/blog/ai-is-writing-more-of-your-terraform/){: .btn .btn-primary }
