---
layout: post
title: "The Trojan horse of cybercrime: Weaponizing SaaS notification pipelines"
date: 2026-04-08 00:00:00 +0300
categories: [Research]
tags: [phishing, saas-abuse, email-security, social-engineering, github]
toc: true
---

Cisco Talos documents a technique dubbed Platform-as-a-Proxy (PaaP), where attackers abuse legitimate SaaS notification pipelines — specifically GitHub commit notifications and Jira Service Management invitation emails — to deliver phishing and scam content that passes SPF, DKIM, and DMARC validation. For GitHub, attackers create repositories and embed malicious lures (fake invoices, fraudulent support numbers) in commit summary and description fields, triggering automated notification emails sent from verified GitHub SMTP servers (e.g., out-28.smtp.github.com, d=github.com DKIM). For Jira, attackers inject malicious content into configurable data fields (project name, welcome message) which Atlassian's own email templates wrap and cryptographically sign. Talos observed ~1.20% of noreply@github.com traffic containing invoice lures over five days, peaking at 2.89% on Feb. 17, 2026. The attack fundamentally undermines reputation-based email filtering since the malicious content is authenticated and delivered by the platforms' own infrastructure.

---

[Read original article](https://blog.talosintelligence.com/weaponizing-saas-notification-pipelines/)
