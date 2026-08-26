---
layout: post
title: "C2PA Cameras Do Not Survive Contact With Reality"
date: 2026-08-25 00:00:00 +0300
categories: [RSS]
tags: [c2pa, android, key-attestation, supply-chain, rce]
toc: true
---

David Buchanan demonstrates that C2PA's media provenance system on Android is fundamentally broken through attacks on its underlying trust model. C2PA relies on Android Key Attestation and Google Play Integrity to cryptographically bind image signatures to device hardware, but root privilege escalation exploits (including the publicly available CVE-2026-43499 one-click root for Pixel devices) and low-cost hardware fault injection attacks (DRAM EMFI) allow attackers to bypass these protections. Once rooted, attackers can use the KeyStore API to sign arbitrary data (including AI-generated images and videos) with legitimate C2PA keys, forging media provenance without extracting the underlying hardware-protected keys. The author provides working exploits and a keystork tool for practical demonstration, and notes that hardware vulnerabilities cannot be realistically patched, making this a permanent architectural failure of Android's strongest C2PA implementation (Google Pixel, Assurance Level 2).

[Read original article](https://www.da.vidbuchanan.co.uk/blog/android-c2pa.html){: .btn .btn-primary }
