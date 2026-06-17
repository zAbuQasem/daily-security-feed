---
layout: post
title: "Mapping out your unknown: A threat hunter’s guide to Salesforce"
date: 2026-06-16 00:00:00 +0300
categories: [RSS]
tags: [cloud, saas, detection, threat-hunting, salesforce]
toc: true
---

Datadog Security Labs provides a comprehensive threat hunting guide for Salesforce environments, mapping real attack chains observed in the wild: compromised credentials, OAuth token abuse via malicious connected apps, and third-party integration compromise used to exfiltrate data and pivot to downstream systems. The article details the attacker playbook (authenticate → enumerate resources → extract data → exfiltrate) and provides concrete detection queries mapped to MITRE ATT&CK tactics, including examples for reconnaissance (Aura/API requests for configuration info), initial access (guest account logins, unusual API activity), and credential access (weak MFA brute force). Practical guidance covers Salesforce logging tiers (ELF vs Real-Time Event Monitoring) and Salesforce-specific audit log nuances, making it immediately actionable for threat hunters and defenders securing high-value SaaS infrastructure.

[Read original article](https://securitylabs.datadoghq.com/articles/mapping-out-your-unknown-threat-hunters-guide-to-salesforce/){: .btn .btn-primary }
