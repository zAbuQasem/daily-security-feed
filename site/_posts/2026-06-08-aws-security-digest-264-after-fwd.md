---
layout: post
title: "AWS Security Digest #264 - After fwd"
date: 2026-06-08 12:00:00 +0300
categories: [RSS]
tags: [cloud, supply-chain, iam, privilege-escalation, malware]
toc: true
---

AWS Security Digest aggregates critical research from fwd:cloudsec conference including OIDC namespace hijacking: attackers can register deleted organization/repository namespaces and mint tokens matching forgotten IAM role trust policies to assume roles without credentials (14% of checked AWS namespaces were vulnerable). Data Perimeter bypass via Bedrock AgentCore allows C2 exfiltration through legitimate AWS API calls using server-side discovery URL validation and protected metadata endpoints that bypass CloudTrail logging. Real-world HazyBeacon malware campaign abuses victim AWS accounts to deploy Lambda Function URLs with no authentication as C2 infrastructure, evading IP/domain reputation filters by proxying through trusted *.lambda-url.*.on.aws domains. Additional research covers AI-driven IAM privilege escalation discovery and SIEM detection rule validation.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-264){: .btn .btn-primary }
