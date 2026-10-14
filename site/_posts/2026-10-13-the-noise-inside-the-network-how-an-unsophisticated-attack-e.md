---
layout: post
title: "The Noise Inside the Network: How an Unsophisticated Attack Exposed a Third-Party Risk"
date: 2026-10-13 22:00:04 +0300
categories: [RSS]
tags: [incident-response, third-party-risk, authentication, wsus, detection]
toc: true
---

Unit 42 analyzes an intrusion into a European bank initiated through a third-party-managed gateway appliance lacking strict authentication enforcement. After gaining initial access via compromised credentials, the attacker conducted noisy reconnaissance across thousands of systems, performed credential-guessing campaigns targeting administrators, and scraped internal documentation. The adversary's persistence attempt exploited a WSUS remote code execution vulnerability on the central configuration management server, but Cortex XDR detected and contained the attack before lateral movement. The case demonstrates that opportunistic attackers succeed through foundational security gaps—missing MFA, weak identity controls, and unpatched edge devices—rather than sophistication; swift detection and containment, combined with credential rotation and expanded endpoint coverage, completely neutralized the threat.

[Read original article](https://unit42.paloaltonetworks.com/noise-inside-network-third-party-risk/){: .btn .btn-primary }
