---
layout: post
title: "The first 72 hours of a ransomware attack: Why restored isn’t recovered"
date: 2026-10-02 00:00:00 +0300
categories: [RSS]
tags: [ransomware, incident-response, forensics, backup, business-continuity]
toc: true
---

Datadog provides a detailed incident response framework for the first 72 hours of a ransomware attack, using a realistic scenario where attackers encrypt critical systems and steal data. The guide covers forensic investigation (determining attacker entry points, analyzing lateral movement), containment strategies (network isolation decisions, identity provider review for unauthorized admin accounts created via weak/missing MFA), and malware discovery. Key preparation recommendations include maintaining isolated, tested, ransomware-resistant backups; preauthorizing specific roles to isolate systems without business sign-off; defining system restoration priorities (desktop ~8h, server ~2d, enterprise systems ~3d) and dependencies; and establishing offline communication channels for when email/chat are compromised. The article emphasizes that organizational recovery extends far beyond technical restoration—weeks of data validation, dependency reconnection, and business continuity planning follow weeks of system recovery work itself.

[Read original article](https://www.datadoghq.com/blog/the-first-72-hours-of-a-ransomware-attack-why-restored-isnt-recovered/){: .btn .btn-primary }
