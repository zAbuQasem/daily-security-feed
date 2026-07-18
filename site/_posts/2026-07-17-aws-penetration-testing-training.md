---
layout: post
title: "AWS Penetration Testing Training"
date: 2026-07-17 21:30:21 +0300
categories: [RSS]
tags: [cloud, iam, ci-cd, aws, evasion]
toc: true
---

AWS attacks follow permission graphs rather than network topology. The article catalogs concrete privilege escalation paths (iam:PassRole+lambda:CreateFunction, iam:CreatePolicyVersion, cross-account trust abuse), S3 exploitation via bucket policy abuse and CloudTrail tampering, Lambda/serverless attacks through event injection and environment variable extraction, EC2 IMDS vulnerabilities in both IMDSv1 and IMDSv2, and CI/CD pipeline compromise through CodeBuild/CodePipeline. Techniques are mapped to real threat actor tradecraft from SCARLETEEL and AMBERSQUID, providing actionable guidance that effective AWS assessment requires understanding implicit service permissions and IAM privilege chains rather than scanning for open ports.

[Read original article](https://blog.pwnedlabs.io/aws-penetration-testing-training){: .btn .btn-primary }
