---
layout: post
title: "AWS Security Digest #278 - Mutually trusted"
date: 2026-09-14 12:00:00 +0300
categories: [RSS]
tags: [aws, cloud, ssrf, rce, imds]
toc: true
---

AWS Security Digest #278 aggregates multiple high-impact CVEs affecting cloud infrastructure. CVE-2026-89049 is a CVSS 9.9 SSRF in AWS SSM Agent that bypasses destination denylists using alternate representations of link-local addresses, enabling remote IMDS credential theft. Wiz's research on LiteLLM (an open-source LLM gateway) reveals authentication bypass (default key `sk-1234` still active on 9.6% of internet-facing deployments), unauthenticated MCP tool execution (CVE-2026-59822), container RCE as root via any valid API key (CVE-2026-59821), and IMDS credential exfiltration through unvalidated pass-through endpoints with header stripping bypassing IMDSv2 token validation. Sysdig's instrumentation of CVE-2026-39987 (marimo notebook RCE) shows actors pivoting from unauthenticated WebSocket access to credential theft in seconds. Digest also highlights Lambda Managed Instances' container-based isolation model, which eliminates per-execution Firecracker microVMs and requires mutual trust between all functions on the same capacity provider.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-278){: .btn .btn-primary }
