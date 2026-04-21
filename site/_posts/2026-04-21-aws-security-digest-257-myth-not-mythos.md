---
layout: post
title: "AWS Security Digest #257 - Myth not Mythos?"
date: 2026-04-21 03:12:32 +0300
categories: [RSS]
tags: [aws, cloud, xss, rce, logging]
toc: true
---

This AWS Security Digest issue is a curated roundup rather than original research, but it highlights two technically meaningful findings. The first is CVE-2026-5429 in AWS Kiro, where the IDE injects the `workbench.colorTheme` value into an inline script without escaping and ships without a CSP, allowing a malicious theme in `.vscode/` to trigger webview XSS and then reach a subprocess message handler for full command execution as the developer. The second covers a Varonis finding that anonymous S3 requests originating inside a VPC to an external bucket produced no caller-side CloudTrail management, data, or Network Activity events, creating a stealthy exfiltration path until AWS patched logging behavior. The digest also includes a critical discussion of Anthropic's Mythos marketing claims, but the real value is as a compact pointer to notable AWS-focused cloud and developer-tool security research.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-257){: .btn .btn-primary }
