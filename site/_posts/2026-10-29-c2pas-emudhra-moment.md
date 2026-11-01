---
layout: post
title: "C2PA's eMudhra Moment"
date: 2026-10-29 00:00:00 +0300
categories: [RSS]
tags: [pki, c2pa, ca-compromise, trust-model, revocation]
toc: true
---

The C2PA media provenance ecosystem lacks revocation mechanisms present in Web PKI, leaving it vulnerable to CA compromise scenarios like eMudhra. The author demonstrates forging S/MIME certificates that chain to Google's C2PA root CA—producing a valid leaf certificate with private key '4' via an undisclosed method to prove intermediate compromise is possible. Unlike TLS, C2PA's trust model assumes intermediates will never be compromised; if they are, media verification tools cannot detect forged provenance chains. This analysis reveals that popular C2PA media verification tools offer no defense against a hypothetical CA compromise, highlighting a critical gap in an emerging ecosystem designed for media authenticity.

[Read original article](https://www.da.vidbuchanan.co.uk/blog/c2pa-four.html){: .btn .btn-primary }
