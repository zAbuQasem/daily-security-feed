---
layout: post
title: "Phantom Squatting: AI-Hallucinated Domains as a Software Supply Chain Vector"
date: 2026-07-01 01:00:11 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, llm, phishing]
toc: true
---

Unit 42 researchers identified phantom squatting, a novel supply chain attack vector where adversaries preemptively register hallucinated web domains that LLMs consistently generate for legitimate brands. Attackers weaponize these domains to intercept traffic from AI coding assistants, CI/CD pipeline agents, and autonomous AI systems that trust LLM-generated URLs without verification. The research analyzed 913 global brands across 685,339 queries, discovering 13,229 confirmed malicious domains already registered and ~250,000 additional unregistered hallucinated domains awaiting exploitation. A real-world case demonstrates an attacker using an AI coding assistant to build the Montana Empire phishing kit targeting a domain the researchers' detection pipeline had flagged as a high-risk hallucination target 23 days earlier. This attack class bypasses traditional reputation-based defenses because phantom domains are born clean—they carry no threat history, blocklist entries, or accumulated malicious signals, making them invisible to conventional URL filtering and threat intelligence systems.

[Read original article](https://unit42.paloaltonetworks.com/phantom-squatting-hallucinated-web-domains/){: .btn .btn-primary }
