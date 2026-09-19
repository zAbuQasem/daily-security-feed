---
layout: post
title: "A Vault with a Heap-View: The Uncomfortable Space Between AgentCore Harness and Identity"
date: 2026-09-18 10:00:36 +0300
categories: [RSS]
tags: [cloud, ai-agents, prompt-injection, credential-theft, rce]
toc: true
---

Unit 42 researchers identified a security issue in AWS AgentCore Harness where credentials managed by AgentCore Identity are resolved to plaintext in the same memory space accessible to the default-enabled shell tool, which runs as root. An attacker can use prompt injection against the agent to trigger shell commands that read these credentials directly from memory or environment context, bypassing encryption at rest and KMS protections. The vulnerability stems from AgentCore's default configuration enabling both the shell and file_operations tools; AWS recommended defenses include scoping allowedTools to least privilege, restricting Identity vault service account permissions, and filtering egress traffic. This represents a novel attack surface combining prompt injection, default-enabled tooling, and credential memory exposure in a managed AI agent platform. The finding was disclosed to AWS, which closed the report as expected behavior under their shared responsibility model.

[Read original article](https://unit42.paloaltonetworks.com/securing-aws-agentcore-harness-credentials/){: .btn .btn-primary }
