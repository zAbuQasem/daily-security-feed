---
layout: post
title: "Spring Ring: An Inside Look at Voice Phishing Campaigns in Microsoft Teams"
date: 2026-08-31 10:00:36 +0300
categories: [RSS]
tags: [phishing, social-engineering, identity, cloud, active-threat]
toc: true
---

Spring Ring is a coordinated vishing operation targeting Microsoft Teams users across 150+ employees in 10+ organizations (January–April 2026). Attackers create external Microsoft Teams accounts with spoofed identities (external.onmicrosoft[.]com tenants) posing as IT help desk, initiate voice calls to build trust and manipulate victims into executing RMM tools or custom malware. Advanced variant escalates via NTLM relay attacks against domain controllers using open-source tools like PetitPotam. This represents an evolution from previous Teams attacks by merging real-time voice interaction with domain privilege escalation, exploiting the trust and lower monitoring of SaaS communication platforms compared to email. Unit 42 tracked 26 distinct attacker identities and attributes the 41% rise in Teams-based attacks to the platform's default 'Chat with Anyone' feature.

[Read original article](https://unit42.paloaltonetworks.com/spring-ring-voice-phishing-campaigns/){: .btn .btn-primary }
