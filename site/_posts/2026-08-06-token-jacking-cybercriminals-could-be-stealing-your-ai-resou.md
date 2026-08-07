---
layout: post
title: "Token Jacking: Cybercriminals Could Be Stealing Your AI Resources"
date: 2026-08-06 10:00:49 +0300
categories: [RSS]
tags: [ai, token-jacking, api-security, supply-chain, credential-theft]
toc: true
---

Token jacking—theft of AI API keys to gain unauthorized access to LLM services—has become a lucrative attack vector as frontier AI model costs and gray-market demand have converged. Attackers steal or hijack API credentials via phishing, information stealers, code repositories, and poisoned npm packages, then provision these keys into open-source proxy platforms ('transfer stations' built on new-api or one-api) that resell AI compute capacity at a discount. These proxies handle obfuscation, credential rotation, billing, and model routing, enabling attackers to generate tens of millions of API calls per day and incur hundreds of thousands of dollars in unauthorized charges before victims detect the breach. Attack vectors include harvesting developer credentials from dark web markets, removing billing limits, disabling usage alerts, and leveraging recent npm supply chain attacks (Shai-Hulud, Miasma) to steal credentials at scale. The financial impact is severe: victims face massive surprise bills due to limitless token consumption by default, with delays in detection creating an even larger attack window.

[Read original article](https://unit42.paloaltonetworks.com/ai-token-jacking/){: .btn .btn-primary }
