---
layout: post
title: "AWS Security Digest #281 - Package Deal"
date: 2026-10-05 12:00:00 +0300
categories: [RSS]
tags: [ai-security, cloud, cves, rce, supply-chain]
toc: true
---

AWS Security Digest curates multiple critical 2026 findings spanning AI agent exploitation and cloud infrastructure security. Two RCE CVEs in AWS Bedrock's AgentCore Python SDK allow command injection via the `install_packages()` helper—attackers can bypass validation using newlines or pip extras syntax to execute arbitrary code and exfiltrate IAM role credentials from the execution sandbox. Novel "context bomb" attacks use forged secrets in canaries to manipulate AI models into stopping or changing behavior, reducing frontier agent success rates from 93% to 0%. AWS's own AI agent guardrails failed twice: the API MCP Server silently dropped its deny list on index load failures, and the MCP proxy's `--read-only` flag hid write tools but still executed them when requested by name. Additionally, cross-tenant Azure Key Vault compromises yielded $200K in bounties, demonstrating continued supply-chain and cloud infrastructure risk.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-281){: .btn .btn-primary }
