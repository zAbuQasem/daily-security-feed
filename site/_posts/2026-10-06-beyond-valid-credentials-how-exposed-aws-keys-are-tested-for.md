---
layout: post
title: "Beyond valid credentials: How exposed AWS keys are tested for Amazon Bedrock access"
date: 2026-10-06 00:00:00 +0300
categories: [RSS]
tags: [aws, cloud, credentials, threat-intel, llm]
toc: true
---

Attackers are actively harvesting and validating AWS credentials specifically for Amazon Bedrock access, treating LLM-capable credentials as a distinct product with resale value. Analysis of the KMON_NOC credential harvesting platform reveals a workflow that uses STS GetCallerIdentity for basic validation, then ListFoundationModels and InvokeModel/Converse API calls to probe Bedrock access across regions, while also extracting AWS_BEARER_TOKEN_BEDROCK environment variables for direct model access. Multiple Python scripts on VirusTotal perform similar validation chains, some including billing:GetCredits enumeration to assess financial value of compromised accounts. The campaign has been active since August 31, 2026, and has targeted over 80 Datadog Cloud SIEM customers. Defenders should monitor for patterns of credential validation followed by Bedrock model enumeration and invocation attempts, as well as batch GetCallerIdentity calls indicative of credential stuffing.

[Read original article](https://securitylabs.datadoghq.com/articles/beyond-valid-credentials-how-exposed-aws-keys-are-tested-for-amazon-bedrock-access/){: .btn .btn-primary }
