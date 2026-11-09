---
layout: post
title: "AWS Security Digest #286 - Top Ten 2026"
date: 2026-11-09 13:00:00 +0300
categories: [RSS]
tags: [cloud, aws, bucket-squatting, cross-tenant, rce, iam]
toc: true
---

AWS Security Digest #286 curates the year's top AWS security research, with deep dives into critical bucket-squatting vulnerabilities. Two cross-tenant attacks exploit unsafe default bucket naming: SageMaker's `default_bucket()` helper (used in 200+ AWS notebooks) allows attackers to pre-create buckets and inject malicious training scripts or endpoint code before container pull, bypassing AWS's 2023 ownership check; aws-sdk-pandas repeats this pattern for Athena query results and EMR logs, exfiltrating or poisoning data via predictably-named buckets. Additional coverage includes common IAM policy mistakes from LLM-generated code. Solid research from high-signal contributors on cloud infrastructure abuse patterns.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-286){: .btn .btn-primary }
