---
layout: post
title: "On the hunt for ARTEX: understanding agentic attacks in AWS environments"
date: 2026-11-09 00:00:00 +0300
categories: [RSS]
tags: [cloud, supply-chain, ai, iam, detection]
toc: true
---

ARTEX is an AI-native penetration framework using LLM agents to automate attack planning and execution, linked to Storm-0940 supply chain threat actor. Datadog observed in-the-wild exploitation against AWS environments through two vectors: compromised long-term IAM access keys and unauthenticated Amazon Cognito public pools. Post-compromise activity focused on CloudWatch FilterLogEvents queries (hardcoded 1000-event limit) hunting financial data and secrets, plus S3 enumeration using placeholder object names like 'zzz_nonexistent_abc.txt' as baseline detection. Researchers identified hundreds of internet-exposed ARTEX consoles hosted in Singapore/Hong Kong, many in Mandarin, revealing active infrastructure supporting the campaign with behavioral indicators useful for detection and hunting.

[Read original article](https://securitylabs.datadoghq.com/articles/artex-agentic-attacks-aws-environments/){: .btn .btn-primary }
