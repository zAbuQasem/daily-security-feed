---
layout: post
title: "Behind the console: An AiTM phishing kit harvesting AWS console credentials and beyond"
date: 2026-06-24 00:00:00 +0300
categories: [RSS]
tags: [cloud, aws, aitm, phishing, mfa]
toc: true
---

Datadog Security Labs documented an active AiTM phishing campaign (June 16–19, 2026) targeting AWS console credentials with real-time MFA relay. Attackers registered three domains impersonating the AWS login page and hosted them on Cloudflare; the phishing kit used JavaScript to extract encrypted victim email from URL parameters, validate targets via server-side cookies, then relay initial credentials and MFA codes (email, SMS, TOTP) through backend API endpoints to the legitimate AWS console, automatically branching to the correct MFA path based on AWS's response. Phishing emails were delivered via compromised SendGrid and Nimbu infrastructure to bypass email authentication checks. The campaign included hunting indicators (three domains registered via NICENIC INTERNATIONAL GROUP CO., LIMITED), CloudTrail signatures (ConsoleLogin events), and evidence of attacker infrastructure validation scripts on VirusTotal.

[Read original article](https://securitylabs.datadoghq.com/articles/behind-the-console-aws-aitm-phishing-kit-and-beyond/){: .btn .btn-primary }
