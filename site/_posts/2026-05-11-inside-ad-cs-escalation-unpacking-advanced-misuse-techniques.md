---
layout: post
title: "Inside AD CS Escalation: Unpacking Advanced Misuse Techniques and Tools"
date: 2026-05-11 22:00:43 +0300
categories: [RSS]
tags: [ad-cs, active-directory, privilege-escalation, certificate-abuse, detection]
toc: true
---

Unit 42 analyzes how attackers abuse Active Directory Certificate Services by chaining certificate template misconfigurations, overly broad enrollment rights, and shadow credential techniques to impersonate privileged identities without exploiting a traditional memory-corruption bug. The write-up focuses on AD CS as an identity escalation surface: once a low-privileged principal can request an authentication-capable certificate or manipulate key mappings, it can obtain long-lived credentials that work for domain authentication, persistence, and lateral movement. The article ties these tradecraft patterns to real intrusion activity, including abuse related to CVE-2022-26923 where issued machine certificates do not match the requesting host identity, creating detectable anomalies in certificate issuance workflows. Its main value is the defensive depth: it maps offensive AD CS techniques to telemetry, event log correlation, and behavioral analytics defenders can use to detect certificate-based privilege escalation that would otherwise look like normal PKI activity.

[Read original article](https://unit42.paloaltonetworks.com/active-directory-certificate-services-exploitation/){: .btn .btn-primary }
