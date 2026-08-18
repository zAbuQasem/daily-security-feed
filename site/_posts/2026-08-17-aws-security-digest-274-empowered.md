---
layout: post
title: "AWS Security Digest #274 - Empowered"
date: 2026-08-17 12:00:00 +0300
categories: [RSS]
tags: [cloud, iam, aws, misconfig, security-architecture]
toc: true
---

AWS Security Digest curating cloud security research, with sharp editorial critique of AWS IAM Role Manager's design flaw: it attaches overly-permissive PowerUserAccess policies by default when provisioning roles for customer code, violating secure-by-default principles. The digest surfaces high-signal research including Trail of Bits' analysis of Nitro Enclaves KMS attestation reuse vulnerabilities (untrusted host can reuse valid attestation documents for unauthorized key operations), TrailTool for session-based CloudTrail forensics, and event-driven architecture security blind spots (network isolation does not guarantee execution isolation in serverless/cloud-native systems). Highlights persistent anti-patterns: AWS recommends post-hoc permission reduction via Access Analyzer despite decades of evidence that humans never voluntarily scope-down working permissions.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-274){: .btn .btn-primary }
