---
layout: post
title: "Curiouser and Curiouser"
date: 2026-08-13 18:00:18 +0300
categories: [RSS]
tags: [phishing, mfa-bypass, social-engineering, malware]
toc: true
---

Cisco Talos discovered JWR, a previously undocumented phishing-as-a-service framework (likely a variant of "The Outsider"), deployed via SMS lures impersonating regional toll and postal authorities. JWR uses an open WebSocket connection for real-time keystroke monitoring and dynamic steering of victims through fake checkout and login flows, enabling live collection of payment data, 2FA codes, identity documents, and device fingerprints. The framework's real-time operator control allows attackers to actively intercept and bypass multi-factor authentication by prompting victims for 2FA codes at precisely the right moment. Its seamless integration with legitimate e-commerce platforms like Shopify makes the phishing lures highly convincing. The comprehensive identity profiles collected enable extensive follow-on fraud and network compromise.

[Read original article](https://blog.talosintelligence.com/curiouser-and-curiouser/){: .btn .btn-primary }
