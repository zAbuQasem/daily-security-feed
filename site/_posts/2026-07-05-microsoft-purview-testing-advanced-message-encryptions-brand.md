---
layout: post
title: "Microsoft Purview: Testing Advanced Message Encryption’s Branding, Revocation, and Expiration"
date: 2026-07-05 05:00:00 +0300
categories: [RSS]
tags: [microsoft, email-encryption, dlp, configuration, testing]
toc: true
---

A technical deep-dive into Microsoft Purview Advanced Message Encryption (AME) reveals configuration requirements and product limitations. Message revocation consistently fails with 401 authentication errors from internal Microsoft service-to-service authentication, completely blocking the revocation feature. The expiration parameter `-ExternalMailExpiryInDays` accepts decimal values (e.g., 0.1 days = 14m24s), well below the documented 1–730 day minimum, representing undocumented behavior not guaranteed across tenants. Enabling revocation and expiration requires both a DLP policy enforcing Do Not Forward encryption and a separate transport rule applying a custom branding template to force portal-based delivery for all external recipients. The article documents practical gaps in Microsoft 365 email security enforcement that administrators should account for when designing message protection and retention policies.

[Read original article](https://thalpius.com/2026/07/05/microsoft-purview-testing-advanced-message-encryptions-branding-revocation-and-expiration/){: .btn .btn-primary }
