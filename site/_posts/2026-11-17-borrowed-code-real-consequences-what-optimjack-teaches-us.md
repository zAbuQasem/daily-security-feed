---
layout: post
title: "Borrowed Code, Real Consequences: What OPTIMJACK Teaches Us"
date: 2026-11-17 20:43:14 +0300
categories: [RSS]
tags: [supply-chain, vendor-compromise, javascript-injection, payment-fraud, crypto]
toc: true
---

OPTIMJACK exploited a vulnerability in Optimizely's Web Experimentation platform to inject malicious JavaScript into the custom Project JavaScript field of customer accounts. The tampered code was served from Optimizely's legitimate CDN under its own SSL certificate, reaching at least 178 organizations across media, technology, and financial services. The injected payload performed three attacks: cryptocurrency wallet address swapping, payment card skimming from checkout forms, and delivery of Coruna and DarkSword exploit kits to iOS devices. This supply chain attack demonstrates how a single vendor vulnerability can bypass perimeter defenses at scale; the report provides concrete segmentation strategies including removing non-essential tags from sensitive pages and isolating payment collection in hardened cross-origin iframes.

[Read original article](https://unit42.paloaltonetworks.com/optimjack-supply-chain-attack/){: .btn .btn-primary }
