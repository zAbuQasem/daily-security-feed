---
layout: post
title: "AWS Security Digest #282 - Assimilated"
date: 2026-10-12 12:00:00 +0300
categories: [RSS]
tags: [ci-cd, supply-chain, cloud, credential-theft, prompt-injection]
toc: true
---

AWS Security Digest #282 aggregates multiple high-priority cloud security research pieces. GhostAction malware now scans GitHub repository histories for exposed AWS keys and secrets, targeting CI/CD pipelines. Attackers actively enumerate stolen AWS credentials for Bedrock API access, using lightweight checker scripts that probe ListFoundationModels and make minimal Converse requests to assess key value before exploitation. AgentCorruption demonstrates prompt injection on AWS Bedrock agents to exfiltrate execution role credentials via IMDS, enabling lateral movement across private agents and conversations. The Terraplane research describes a production architecture isolating Terraform plan and apply steps with short-lived, role-scoped credentials per execution stage to prevent agent/attacker credential leakage during the planning phase.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-282){: .btn .btn-primary }
