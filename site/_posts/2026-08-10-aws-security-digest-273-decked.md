---
layout: post
title: "AWS Security Digest #273 - Decked"
date: 2026-08-10 12:00:00 +0300
categories: [RSS]
tags: [supply-chain, cloud, credential-theft, rce, prompt-injection]
toc: true
---

A malicious commit to the npm `keyv` package triggered a self-propagating worm affecting hundreds of npm modules including `cacheable`, which scraped AWS STS credentials, Secrets Manager values across 17 regions, SSM Parameter Store, and GitHub Actions secrets from build hosts. Additionally, this digest covers multiple critical AWS vulnerabilities: LiteLLM's (OffGuard) IMDS bypass via header stripping to exfiltrate instance credentials despite IMDSv2, CloudShell websocket persistence allowing continued access after token revocation and uid 0 account creation, and eight AWS security bulletins including prompt injection flaws in Amazon MQ and Strands Agents Tools that leak broker credentials and OAuth tokens. The supply chain attack directly impacts AWS deployments; the IMDS bypass demonstrates cloud infrastructure abuse; and the agent/MCP vulnerabilities reflect expanding attack surface in AI tooling.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-273){: .btn .btn-primary }
