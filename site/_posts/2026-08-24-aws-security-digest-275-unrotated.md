---
layout: post
title: "AWS Security Digest #275 - Unrotated"
date: 2026-08-24 12:00:00 +0300
categories: [RSS]
tags: [aws, credentials, key-rotation, account-security]
toc: true
---

Truffle Security tested 10,616 AWS key pairs leaked publicly between August 2022–2026 and found 88% still authenticate to live accounts. One in six of 64,024 verified keys are root keys (unscoped, full account compromise), with median age of 1,831 days and only 13.7% ever rotated; 130 root keys belong to organization management accounts. This large-scale analysis reveals the persistence and privilege escalation risk of exposed AWS credentials, particularly the failure of rotation practices and AWS's own AWSCompromisedKeyQuarantine policy application. The digest also covers post-quantum cryptography CA implementation on AWS and an AI-driven threat hunting architecture, but the leaked credentials research is the primary security substance.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-275){: .btn .btn-primary }
