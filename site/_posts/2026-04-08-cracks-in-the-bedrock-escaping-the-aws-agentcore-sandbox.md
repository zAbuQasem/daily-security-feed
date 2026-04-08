---
layout: post
title: "Cracks in the Bedrock: Escaping the AWS AgentCore Sandbox"
source_url: https://unit42.paloaltonetworks.com/bypass-of-aws-sandbox-network-isolation-mode/
date: 2026-04-08
priority: 1
tags: [cloud, aws, sandbox-escape, ssrf, dns-tunneling, github-zabuqasem, linkedin-zeyad-abulaban]
feed: https://unit42.paloaltonetworks.com/feed/
---

Unit 42 researchers discovered that AWS Bedrock AgentCore's Code Interpreter sandbox mode — advertised as providing 'complete isolation with no external network access' — permits DNS resolution, enabling covert bi-directional data exfiltration via DNS tunneling. By mapping egress paths through incremental DNS probing from within the sandbox, researchers confirmed queries reaching external DNS servers, effectively turning the 'offline' sandbox into a C2-capable exfiltration channel. Additionally, the AgentCore Runtime's microVM Metadata Service (MMDS) lacked session token enforcement, meaning a standard SSRF vulnerability in any agent-exposed endpoint could directly extract sensitive IAM credentials from the metadata service. AWS has since updated documentation to acknowledge limited external network access and deployed internal remediations, but customers cannot directly patch the managed environment.
