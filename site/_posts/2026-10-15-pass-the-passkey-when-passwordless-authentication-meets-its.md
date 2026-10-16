---
layout: post
title: "Pass the Passkey: When Passwordless Authentication Meets Its Achilles' Heel"
date: 2026-10-15 05:00:00 +0300
categories: [RSS]
tags: [passkeys, azure-ad, privilege-escalation, replay]
toc: true
---

Windows 11 writes complete WebAuthn assertions (challenge, signature, credential ID) to Event Logs accessible to low-privileged users, enabling attackers to capture tokens and replay them against Microsoft Entra ID to bypass conditional access and MFA without triggering alerts. Entra ID's reliance on short-lived JWT challenges with 10-minute clock skew tolerance, combined with missing signature counter tracking, makes replay attacks feasible. This affects enterprise authentication across Azure AD, password managers (1Password, Bitwarden), and hybrid FIDO2 flows. Disclosed by SpecterOps at Black Hat USA 2026; Microsoft partially addressed event log truncation but Windows Hello passkeys remain vulnerable to replay.

[Read original article](https://blog.syss.com/posts/pass-the-passkeys/){: .btn .btn-primary }
