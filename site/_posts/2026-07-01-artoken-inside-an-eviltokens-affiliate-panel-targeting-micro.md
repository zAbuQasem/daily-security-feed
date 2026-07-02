---
layout: post
title: "ARToken: Inside an EvilTokens affiliate panel targeting Microsoft 365"
date: 2026-07-01 10:00:38 +0300
categories: [RSS]
tags: [phishing, oauth, bec, mfa-bypass, cloud]
toc: true
---

Cisco Talos reverse-engineered ARToken, a phishing-as-a-service (PhaaS) panel infrastructure-linked to EvilTokens, which abuses Microsoft's OAuth 2.0 Device Authorization Grant (RFC 8628) to capture tokens while bypassing MFA entirely. The platform exposes 80+ API endpoints enabling device code phishing, Primary Refresh Token (PRT) persistence, email interception, and automated business email compromise (BEC) operations through a multi-tenant dashboard serving affiliate operators. ARToken deploys a seven-layer anti-analysis defense combining behavioral verification (mouse/touch interaction requirements, browser fingerprinting, User-Agent detection) with XOR-encrypted payloads, escalating evasion beyond prior EvilTokens observations. Real-world lures impersonate legitimate vendor relationships, exploiting SharePoint URL spoofing to redirect accounts-payable staff to attacker-controlled tenants; Talos documented 1,000+ phishing pages across 500+ Cloudflare Workers domains. The platform operationalizes AI-augmented targeting via Groq Llama and GPT-4o-mini for financial exposure scoring and BEC scenario generation, sold at $1,500 + $500/month subscription, representing a mature evolution of account takeover infrastructure with significant impact to corporate email security.

[Read original article](https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/){: .btn .btn-primary }
