---
layout: post
title: "So… You Found AWS Access Keys (Part 1)"
date: 2026-09-10 04:00:00 +0300
categories: [RSS]
tags: [aws, cloud, iam, enumeration, credentials]
toc: true
---

A TrustedSec guide distinguishing AWS access key types: AKIA (long-term IAM user keys with 20-char ID + 40-char secret) and ASIA (temporary STS keys requiring an additional 825-char session token with 1–12 hour validity). The article explains practical implications for penetration testers who discover plaintext AWS credentials during assessments, including that account ID can be extracted from AKIA keys alone even without the secret, and that S3 presigned URLs present a third credential format providing time-limited direct object access. Provides reference-grade technical specifications and enumeration starting points for validating and leveraging found AWS credentials.

[Read original article](https://trustedsec.com/blog/so-you-found-aws-access-keys-part-1){: .btn .btn-primary }
