---
layout: post
title: "Parasitizing trust: How legitimate infrastructure becomes a delivery pipeline for attackers"
date: 2026-10-21 10:00:00 +0300
categories: [RSS]
tags: [supply-chain, platform-abuse, social-engineering, saas-abuse, email-security]
toc: true
---

Cisco Talos documents systematic abuse of 25+ legitimate platforms (retailers, SaaS, collaboration tools) as proxy delivery infrastructure. Attackers inject malicious content—particularly attacker-controlled phone numbers—into transactional template fields (shipping, billing, order notes) of trusted notifications from Dell and Staples. These messages pass DMARC/DKIM authentication because they legitimately originate from compromised platforms, inheriting trust before redirecting victims to attacker contact information for social engineering and fraud. The research also covers an evolution of list-bombing from simple DoS into a content delivery mechanism, exploiting the implicit trust platforms place in user-supplied data rendered into high-reputation automated notifications. Defense requires input validation on all user-influenced fields and correlating transaction context against account history.

[Read original article](https://blog.talosintelligence.com/parasitizing-trust-how-legitimate-infrastructure-becomes-a-delivery-pipeline-for-attackers/){: .btn .btn-primary }
