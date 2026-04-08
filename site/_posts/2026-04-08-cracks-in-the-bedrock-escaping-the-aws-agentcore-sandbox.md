---
layout: post
title: "Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox"
date: 2026-04-08 00:00:00 +0300
categories: [Research, Critical]
tags: [cloud, aws, sandbox-escape, ssrf, dns-tunneling]
pin: true
toc: true
---

Unit 42 researchers discovered that AWS Bedrock AgentCore's Code Interpreter sandbox mode — advertised as providing 'complete isolation with no external network access' — permits DNS resolution, enabling covert bi-directional data exfiltration via DNS tunneling. By mapping egress paths through incremental DNS probing from within the sandbox, researchers confirmed queries reaching external DNS servers, effectively turning the 'offline' sandbox into a C2-capable exfiltration channel. Additionally, the AgentCore Runtime's microVM Metadata Service (MMDS) lacked session token enforcement, meaning a standard SSRF vulnerability in any agent-exposed endpoint could directly extract sensitive IAM credentials from the metadata service. AWS has since updated documentation to acknowledge limited external network access and deployed internal remediations, but customers cannot directly patch the managed environment.

---

[Read original article](https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/)

> Source: `unit42.paloaltonetworks.com`
