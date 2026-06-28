---
layout: post
title: "A user account restriction (for example, a time-of-day restriction) is preventing you from logging on. For assistance, contact your system administrator or technical support."
date: 2026-06-27 07:39:24 +0300
categories: [RSS]
tags: [active-directory, authentication, kerberos, defense, hardening]
toc: true
---

The Protected Users security group in Active Directory forces Kerberos authentication instead of NTLM for member accounts, significantly raising the bar for network penetration testers and lateral movement attackers. This requires switching RDP connections from NTLM format (IP or CORP\username) to Kerberos format (user@domain UPN with FQDN hostname), and ensures DNS resolution of target hosts. The article provides practical troubleshooting for Kerberos authentication failures, including clock skew tolerance (5-minute drift limit between client, target, and domain controller), account expiration, and RDP service denial policies. This is a high-value, low-effort hardening control for privileged and sensitive accounts in enterprise AD environments.

[Read original article](https://projectblack.io/blog/a-user-account-restriction-for-example-a-time-of-day-restriction-is-preventing-you-from-logging-on-for-assistance-contact-your-system-administrator-or-technical-support/){: .btn .btn-primary }
