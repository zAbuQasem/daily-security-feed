---
layout: post
title: "Identity Abuse Through Trusted Communication Channels"
date: 2026-08-20 10:00:25 +0300
categories: [RSS]
tags: [phishing, identity, credential-theft, saas, social-engineering]
toc: true
---

Threat actors are increasingly abusing enterprise collaboration platforms (Slack, Teams, Discord) to conduct identity-focused attacks, with Unit 42 telemetry showing a 4.5x surge in related alerts over 12 months (1,490 to 6,799). Attackers exploit compromised accounts, external federation, guest access, or trusted third-party relationships to send phishing, impersonation, and credential theft requests that appear legitimate because they originate from authenticated user identities within trusted communication channels. The article documents real-world campaigns including APT29's use of Teams federation to impersonate IT support and credential-harvesting redirects via attacker-controlled Slack workspaces. Security controls remain primarily focused on email and authentication events, creating visibility gaps in post-authentication collaboration activity where malicious activity can masquerade as routine work communication. The paper maps these techniques to MITRE ATT&CK (T1566 phishing, T1684.001 impersonation, T1556 authentication modification) and provides detection and defensive recommendations.

[Read original article](https://unit42.paloaltonetworks.com/communication-channel-identity-risks/){: .btn .btn-primary }
