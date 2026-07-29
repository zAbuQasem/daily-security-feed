---
layout: post
title: "IR Trends Q2 2026: Phishing and weaponized remote management tools drive attack chains"
date: 2026-07-28 10:00:01 +0300
categories: [RSS]
tags: [phishing, mfa-bypass, ransomware, rmm, m365]
toc: true
---

Cisco Talos IR Q2 2026 report reveals phishing as the primary initial access vector (appearing in >50% of engagements), with attackers evading email gateways via QR code-embedded PDFs and trusted cloud infrastructure. MFA bypass techniques—including adversary-in-the-middle proxies, session token theft, MFA fatigue, and OAuth device authorization flow abuse—appeared in 65% of engagements. Ransomware operators (Sinobi, Nitrogen, Warlock) weaponized legitimate remote management tools: a trojanized MeshAgent binary deployed as a SYSTEM-level backdoor communicating over encrypted WebSocket, and Zoho Assist for unattended remote control. Talos also documented ARToken, a phishing-as-a-service platform offering 80+ API endpoints for device code phishing, primary refresh token persistence, and post-compromise token management. Defenders should implement QR code blocking in email, phishing-resistant MFA, behavioral monitoring of administrative tools, and strict application allowlisting.

[Read original article](https://blog.talosintelligence.com/ir-trends-q2-2026/){: .btn .btn-primary }
