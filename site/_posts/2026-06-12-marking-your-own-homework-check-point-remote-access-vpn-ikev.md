---
layout: post
title: "Marking Your Own Homework (Check Point Remote Access VPN IKEv1 Authentication Bypass CVE-2026-50751)"
date: 2026-06-12 05:17:20 +0300
categories: [RSS]
tags: [vpn, auth-bypass, ikev1, exploit, ransomware]
toc: true
---

Check Point Remote Access VPN contains a critical authentication bypass in the IKEv1 implementation (CVE-2026-50751, CVSS 9.3) where a logic flaw allows clients to control whether machine certificate validation occurs. The vulnerable function `process_cert_payloads()` accepted a caller-supplied flag determining whether to process machine certificates; an attacker could set this flag to skip validation entirely. The vulnerability affects Check Point R80.20–R82.10 when IKEv1 is enabled and machine certificate authentication is optional. Exploitation has been active in the wild since May 2026, impacting dozens of organizations and linked to Qilin ransomware operators, making it a critical perimeter security risk.

[Read original article](https://labs.watchtowr.com/marking-your-own-homework-check-point-remote-access-vpn-ikev1-authentication-bypass-cve-2026-50751/){: .btn .btn-primary }
