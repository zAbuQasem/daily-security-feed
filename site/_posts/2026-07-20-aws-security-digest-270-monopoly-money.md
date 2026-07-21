---
layout: post
title: "AWS Security Digest #270 - Monopoly Money"
date: 2026-07-20 12:00:00 +0300
categories: [RSS]
tags: [aws, iam, oidc, persistence, detection, cloud]
toc: true
---

AWS Security Digest #270 covers three pieces of solid technical security research: Aidan Steele's reverse-engineering of the `sts:RoleAuthorizedByIdp` condition key, which allows OIDC tokens to restrict which AWS roles they can assume via an allow-list claim checked before the role's trust policy; Victor Grenu's open-source ClickOps Sentinel tool that uses Claude agents to analyze console changes detected via CloudTrail's `sessionCredentialFromConsole` flag and evaluate their legitimacy against adjacent activity; and Jan Blažek's reference guide on four AWS persistence mechanisms (backdoor IAM users, assume-role-policy whitelist, Lambda backdoors, federated sessions) with CloudTrail-based hunting queries. The digest also announces GuardDuty AI Protection's GA, which detects anomalous model invocations and cost-harvesting attacks on Bedrock and SageMaker.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-270){: .btn .btn-primary }
