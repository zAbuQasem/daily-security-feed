---
layout: post
title: "AWS Security Digest #256 - TY Mythos"
date: 2026-04-14 03:12:07 +0300
categories: [RSS]
tags: [aws, cloud, iam, sandbox-escape, incident-response]
toc: true
---

This digest highlights two substantive AWS-focused research findings rather than simple news. The first covers Palo Alto Unit 42's AgentCore work, where AWS Code Interpreter sandbox isolation can be bypassed because DNS egress remains available for covert C2 and exfiltration, while the microVM Metadata Service exposes credentials without session-token enforcement, effectively recreating an IMDSv1-style weakness inside the sandbox. A follow-on issue in the AgentCore starter toolkit creates overly broad wildcard IAM roles across agents, letting a compromised agent access other agents' ECR images, memory, runtimes, and conversation history for cross-agent compromise. The second featured research analyzes IAM credential revocation gaps: disabling an access key takes roughly four seconds to propagate, which allows a tool like notyet to detect containment attempts and race to create new roles, rewrite policies, or mint replacement identities, with Organizations SCPs standing out as the most reliable containment control.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-256){: .btn .btn-primary }
