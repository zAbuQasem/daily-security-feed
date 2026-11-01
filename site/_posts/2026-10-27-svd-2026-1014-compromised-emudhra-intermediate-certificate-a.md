---
layout: post
title: "SVD-2026-1014: Compromised eMudhra Intermediate Certificate Authorities on Splunk Products - October 2026"
date: 2026-10-27 00:00:00 +0300
categories: [RSS]
tags: [pki, supply-chain, ca-compromise, splunk]
toc: true
---

A fundamental error in eMudhra's Key Generation Ceremony (April 2025) rendered eight intermediate CA private keys cryptographically weak, allowing brute-force recovery within seconds. This affects the integrity of certificate chains relying on these CAs. Splunk investigated whether its products include eMudhra CA certificates in trust stores and found no confirmed compromise of Splunk services or products, though investigation into 25+ products and services remains ongoing. The core issue is infrastructure-critical: any deployment using affected eMudhra certificates for TLS validation could be vulnerable to man-in-the-middle attacks via forged certificates.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1014){: .btn .btn-primary }
