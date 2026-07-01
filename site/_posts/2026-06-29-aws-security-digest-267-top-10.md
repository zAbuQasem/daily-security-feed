---
layout: post
title: "AWS Security Digest #267 - Top 10"
date: 2026-06-29 12:00:00 +0300
categories: [RSS]
tags: [cloud, credential-theft, phishing, aitm, supply-chain]
toc: true
---

AWS Security Digest #267 highlights two significant active threats: (1) Amazon Q VS Code Extension auto-executed MCP servers from untrusted repos without user approval, allowing booby-trapped projects to exfiltrate AWS credentials and session tokens via inherited shell environment; (2) A sophisticated AiTM phishing kit running on three look-alike AWS sign-in domains forwards victim passwords and live MFA codes to attacker infrastructure for real-time account takeover—the same PoisonSeeds kit documented targeting SendGrid and Okta in 2025, now retargeted at AWS. Both include actionable indicators (DNS IOCs, CloudTrail patterns) for defenders. Additionally covers Lambda MicroVMs security edges and curator announcement for AWS Security Digest Top 10 research rankings.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-267){: .btn .btn-primary }
