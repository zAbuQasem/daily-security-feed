---
layout: post
title: "Inside the Modern SOC: The Identity Front Door"
date: 2026-08-07 23:00:01 +0300
categories: [RSS]
tags: [identity, threat-intelligence, social-engineering, mfa, incident-response]
toc: true
---

Unit 42 analysis of incident response data shows identity compromise as the dominant initial access vector, appearing in 90% of investigated incidents with 65% of breaches starting via credential theft, phishing, MFA fatigue attacks, and social engineering. Threat groups like Scattered Spider leverage identity abuse for persistence and privilege escalation, with attackers typically establishing footholds across multiple domains before detection. The article emphasizes that compromised identities enable attackers to masquerade as legitimate users, bypassing traditional perimeter controls. SOC detection strategies focus on correlating identity activity across endpoints, cloud, and network telemetry to distinguish legitimate users from compromised accounts, combined with continuous threat hunting to uncover hidden persistence before incidents escalate.

[Read original article](https://unit42.paloaltonetworks.com/soc-identity-front-door/){: .btn .btn-primary }
