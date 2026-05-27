---
layout: post
title: "Intelligence Insights: May 2026"
date: 2026-05-26 13:55:13 +0300
categories: [RSS]
tags: [malware, threat-intelligence, entra-id, supply-chain, infostealer]
toc: true
---

Red Canary's May 2026 threat intelligence roundup covers the top 10 most prevalent threats observed in April. ClearFake leads via compromised-website JavaScript injection using fake CAPTCHA/ClickFix lures to deliver payloads including ACR Stealer (a C++ MaaS infostealer) and LummaC2. A notable surge in OAuth device code phishing is documented — adversaries abuse legitimate Microsoft device auth flows to obtain access/refresh tokens that satisfy MFA claims and bypass conditional access policies, using tools like GraphRunner against Entra ID, Outlook, SharePoint, and Teams; PhaaS platforms Kali365 and EvilTokens have commoditized this technique. The Axios npm package supply chain compromise (account takeover on March 30, 2026, resulting in two malicious versions propagated via automated updates) also ranks in the top 10. Mitigations include blocking device code authentication flows via conditional access policy and implementing continuous access evaluation (CAE).

[Read original article](https://redcanary.com/blog/threat-intelligence/intelligence-insights-may-2026/){: .btn .btn-primary }
