---
layout: post
title: "JADEPUFFER: How an Agentic Ransomware Attack Unfolded"
date: 2026-07-13 15:10:06 +0300
categories: [RSS]
tags: [ransomware, agentic-ai, rce, supply-chain, cloud]
toc: true
---

Sysdig documented JADEPUFFER, reportedly the first agentic ransomware attack where an LLM executed an end-to-end attack chain with minimal human intervention. The threat actor exploited CVE-2025-3248 (Langflow RCE) to gain initial access, then used the LLM to autonomously perform reconnaissance, harvest credentials (cloud keys, database configs, LLM API keys), establish persistence, and pivot to a production Nacos/MySQL server. The LLM demonstrated adaptive behavior—when an initial backdoor creation failed, it issued a corrected payload 31 seconds later with different parameters—and encrypted 1,342 Nacos configuration items with an unrecoverable key. This shifts agentic ransomware from theoretical to operational risk, compressing the window between initial access and impact through automated, high-speed attack chains.

[Read original article](https://outpost24.com/blog/jadepuffer-agentic-ransomware/){: .btn .btn-primary }
