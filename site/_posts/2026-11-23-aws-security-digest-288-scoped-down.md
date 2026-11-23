---
layout: post
title: "AWS Security Digest #288 - Scoped Down"
date: 2026-11-23 13:00:00 +0300
categories: [RSS]
tags: [iam, cloud, policy-bypass, ai-security, threat-intelligence]
toc: true
---

AWS Security Digest covering three substantive findings: Capital Offense demonstrates a critical IAM policy bypass where case-sensitive tag enforcement (expect `admin`, get `Admin`) defeats AWS-recommended SCPs across 100+ GitHub repositories; ARTEX autonomous red teaming agents consistently trigger AWS canaries in replica production environments, with 59/59 runs hitting honeypots and policy evasion attempts now sophisticated enough to recognize and back away from decoys; and Amazon Threat Intelligence's discovery of Cairn, an exposed AI pentest framework where agents autonomously discovered a zero-day path traversal in medical imaging software and escalated it to root—demonstrating autonomous agent capability outpacing human incident response workflows.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-288){: .btn .btn-primary }
