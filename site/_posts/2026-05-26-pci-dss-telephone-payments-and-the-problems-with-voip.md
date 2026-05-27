---
layout: post
title: "PCI DSS, Telephone Payments, and the Problems With VoIP"
date: 2026-05-26 04:00:00 +0300
categories: [RSS]
tags: [pci-dss, compliance, voip, payment-security]
toc: true
---

Merchants accepting card payments over VoIP cannot use the reduced-scope SAQ C-VT or P2PE Self-Assessment Questionnaires to limit their PCI DSS compliance burden — a fact many have only discovered during assessments or when transaction volumes force a QSA review. PCI SSC guidance (FAQ 1153 and the Telephone-Based Payment Card Data supplement) treats VoIP traffic carrying account data identically to any other in-scope IP traffic, meaning the VoIP phone or softphone workstation enters CDE scope the moment call audio crosses the merchant network boundary. This invalidates C-VT and P2PE eligibility, potentially expanding applicable requirements from ~15–44 to 108–236. The article maps all SAQ types against telephone payment use cases and scopes, helping merchants identify which SAQ their processor has been silently applying via guided questionnaire flows.

[Read original article](https://trustedsec.com/blog/pci-dss-telephone-payments-and-the-problems-with-voip){: .btn .btn-primary }
