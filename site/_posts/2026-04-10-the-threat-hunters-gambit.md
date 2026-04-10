---
layout: post
title: "The threat hunter’s gambit"
date: 2026-04-10 03:12:54 +0300
categories: [RSS]
tags: [phishing, saas, email-security, detection, threat-hunting]
toc: true
---

Cisco Talos highlights a 'Platform-as-a-Proxy' (PaaP) phishing technique where threat actors abuse legitimate SaaS notification pipelines (GitHub, Jira) to send phishing emails that pass SPF, DKIM, and DMARC checks because they originate from trusted platform infrastructure. The technique exploits 'automation fatigue' — users conditioned to trust system-generated alerts — to harvest credentials while bypassing traditional email security gateways. Recommended mitigations include ingesting SaaS API logs into a SIEM to detect anomalous precursor activity (mass invitations, suspicious project creation), instance-level verification against internal SaaS directories, and semantic intent analysis on notification content. The newsletter also briefly covers APT28 router compromise for credential theft, Storm-1175 deploying Medusa ransomware via CVE-2026-1731 (BeyondTrust RCE), and a new Lua-based malware family (LucidRook) targeting Taiwanese NGOs.

---

[Read original article](https://blog.talosintelligence.com/the-threat-hunters-gambit/){: .btn .btn-primary }
