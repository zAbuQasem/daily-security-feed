---
layout: post
title: "CitrixBleed To Infinity And Beyond (Citrix NetScaler Pre-Auth Memory Overread CVE-2026-8451)"
date: 2026-06-30 19:35:58 +0300
categories: [RSS]
tags: [memory-disclosure, saml, netscaler, pre-auth, xml-parsing]
toc: true
---

CVE-2026-8451 is a pre-auth memory overread in Citrix NetScaler's SAML identity provider implementation (CVSS 8.8), caused by improper whitespace and quote handling in XML attribute parsing. Unauthenticated attackers can read arbitrary memory beyond buffer boundaries via crafted SAML requests to the /saml/login endpoint, potentially disclosing authentication credentials and session tokens. The vulnerability affects NetScaler ADC/Gateway versions 14.1 (before 72.61) and 13.1 (before 63.18). watchTowr Labs discovered this zero-day in March 2026 as part of an endemic pattern of memory management vulnerabilities in NetScaler's codebase—this is the latest in a series of similar exploitable memory issues found in the same critical appliance.

[Read original article](https://labs.watchtowr.com/citrixbleed-to-infinity-and-beyond-citrix-netscaler-pre-auth-memory-overread-cve-2026-8451/){: .btn .btn-primary }
