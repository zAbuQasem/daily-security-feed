---
layout: post
title: "LiteLLM Compromised, Steals Credentials"
date: 2026-10-21 13:44:12 +0300
categories: [RSS]
tags: [supply-chain, malware, pypi, cloud-secrets, c2]
toc: true
---

LiteLLM version 1.107.0 was compromised and uploaded to PyPI and Docker registries on October 21, 2026, containing a credential stealer that exfiltrates browser, cloud, and AI secrets from affected systems. The malicious package also includes dormant C2 capability for potential post-exploitation control. This is a high-impact supply chain attack targeting developers and organizations using LiteLLM for LLM integration, with credentials from multiple attack surfaces at risk. Immediate package rotation and credential rotation recommended for all LiteLLM users.

[Read original article](https://www.wiz.io/blog/litellm-compromised-steals-credentials){: .btn .btn-primary }
