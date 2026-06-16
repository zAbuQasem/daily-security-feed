---
layout: post
title: "AWS Security Digest #265 - Promises"
date: 2026-06-15 12:00:00 +0300
categories: [RSS]
tags: [cloud, aws, data-residency, logging-evasion, ai-security]
toc: true
---

AWS Bedrock's new flagship Claude models (Fable 5, Mythos 5) require prompts and outputs to be shared with Anthropic and retained for 30 days with human review access, violating Bedrock's longstanding zero-retention promise and introducing data-residency, CLOUD Act, and compliance exposure. The digest also covers cloud logging evasion—including UpdateTrail-based KMS key manipulation to silently stop CloudTrail log delivery—and demonstrates that hardened AI email agents can be socially engineered via traditional phishing tactics to forward AWS IAM keys, database credentials, and SSH secrets despite explicit identity-verification policies.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-265){: .btn .btn-primary }
