---
layout: post
title: "Barracuda Networks is your new best friend (Barracuda Email Security Gateway Pre-Auth Remote Root RCE CVE-2026-116606 / CVE-2026-111560)"
date: 2026-11-05 21:19:58 +0300
categories: [RSS]
tags: [rce, auth-bypass, appliance, cve, edge-security]
toc: true
---

Two critical pre-authentication vulnerabilities in Barracuda Email Security Gateway (CVE-2026-116606 and CVE-2026-111560) allow unauthenticated remote code execution on an edge appliance used to inspect all inbound email. CVE-2026-116606 is a pre-authentication authorization bypass in the password-change handler: when a password change fails, the code incorrectly returns the low-privilege login-screen role object instead of calling bailout(), allowing the request to continue executing with elevated privileges. This bypass chains with CVE-2026-111560 (OS command injection) to achieve pre-auth RCE. The analysis includes binary diffing methodology comparing vulnerable (9.4.0.027) and patched (9.4.0.029) versions, with detailed code-level vulnerability mechanics in the Index.pm handler and identification of the root cause in the Perl authentication framework.

[Read original article](https://labs.watchtowr.com/barracuda-networks-is-your-new-best-friend-barracuda-email-security-gateway-pre-auth-remote-root-rce-cve-2026-116606-cve-2026-111560/){: .btn .btn-primary }
