---
layout: post
title: "More Evidence That Words Don't Mean What We Thought They Meant (Ivanti Sentry Pre-Auth OS Command Injection CVE-2026-10520)"
date: 2026-06-10 00:52:20 +0300
categories: [RSS]
tags: [rce, pre-auth, ivanti, auth-bypass, infrastructure]
toc: true
---

Watchtowr Labs published a detailed technical analysis of two critical vulnerabilities in Ivanti Sentry, a network gateway for enterprise mobile device management. CVE-2026-10520 is a pre-authenticated OS command injection in the `/mics/api/v2/sentry/mics-config/handleMessage` endpoint that accepts a user-supplied `message` parameter passed directly into `ConfigServiceHandler.handleMessage()` without sanitization, allowing remote unauthenticated attackers to achieve root-level RCE with a CVSS score of 10/10. CVE-2026-10523 is an authentication bypass vulnerability permitting unauthenticated attackers to create arbitrary administrative accounts. Since Ivanti Sentry sits at the enterprise network edge between corporate mobile devices and backend systems like Microsoft Exchange, compromising it provides direct access to internal infrastructure.

[Read original article](https://labs.watchtowr.com/more-evidence-that-words-dont-mean-what-we-thought-they-meant-ivanti-sentry-pre-auth-os-command-injection-cve-2026-10520/){: .btn .btn-primary }
