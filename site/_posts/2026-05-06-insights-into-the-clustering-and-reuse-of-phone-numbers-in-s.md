---
layout: post
title: "Insights into the clustering and reuse of phone numbers in scam emails"
date: 2026-05-06 10:00:12 +0300
categories: [RSS]
tags: [toad, phishing, voip, threat-intel, detection]
toc: true
---

Cisco Talos analyzes telephone-oriented attack delivery (TOAD) campaigns by treating phone numbers in scam emails as durable indicators of compromise rather than focusing only on disposable sender addresses. The post breaks down how attackers abuse VoIP infrastructure and API-driven CPaaS provisioning—highlighting providers such as Sinch, Twilio, and Bandwidth—to acquire numbers at scale, then rotate through sequential blocks and cool-down periods to evade reputation-based filtering. In Talos' February 26 to March 31 dataset, researchers identified 1,652 unique numbers, observed cross-campaign reuse across PayPal, Geek Squad, McAfee, and Norton-themed lures, and found that the same numbers were reused with different subjects and attachment formats such as PDF and HEIC. The practical value is in clustering campaigns around reused phone numbers, carrier metadata, and line type (VoIP, wireless, landline) to expose shared scam-call-center infrastructure that would be missed if defenders only tracked email IOCs.

[Read original article](https://blog.talosintelligence.com/insights-into-the-clustering-and-reuse-of-phone-numbers-in-scam-emails/){: .btn .btn-primary }
