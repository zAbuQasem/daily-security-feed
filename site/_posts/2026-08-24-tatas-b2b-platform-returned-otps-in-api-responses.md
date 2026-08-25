---
layout: post
title: "Tata’s B2B platform returned OTPs in API responses"
date: 2026-08-24 14:25:14 +0300
categories: [RSS]
tags: [authentication, account-takeover, api-security, bug-bounty, logic-flaw]
toc: true
---

Tata nexarc's B2B procurement platform returned the OTP in cleartext within API responses to its AES-encrypted OTP request endpoint, enabling account takeover with only knowledge of a target's phone number. The vulnerability arose from an unnecessary "otpGeneratedForMobile" field that was transmitted but never used by the client — an attacker could intercept it via browser DevTools breakpoints on the JavaScript decryption code. Successful exploitation granted complete admin access to corporate accounts, including employee management, order history, licenses, and marketplace data. The platform serves 55k+ LinkedIn followers; the researcher gained access to high-privilege accounts affiliated with Tata Business Hub and Tata Steel. Disclosed to India's CERT-IN on July 30, 2026; fixed by July 31, 2026.

[Read original article](https://eaton-works.com/2026/08/24/tata-nexarc-hack/){: .btn .btn-primary }
