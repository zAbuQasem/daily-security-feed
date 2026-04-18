---
layout: post
title: "Anonymous credentials: an illustrated primer (Part 2)"
date: 2026-04-18 03:10:45 +0300
categories: [RSS]
tags: [privacy, cryptography, anonymous-credentials, blind-signatures, privacypass]
toc: true
---

This post examines how real anonymous credential systems are built and deployed, focusing on Privacy Pass as a concrete implementation of Chaum-style blind-signature credentials. It walks through the issuance flow where a user chooses a token type, optional metadata, and a random serial number, then obtains a blind signature so the issuer signs the credential without learning its contents. The verifier later checks the issuer signature and enforces single use by storing previously seen serial numbers, while the metadata field can bind a token to a specific site, date, or session challenge without exposing that binding to the issuer. The article frames these design choices as practical defenses against credential cloning and cross-site reuse, and uses Privacy Pass deployment by Cloudflare, Apple, Google, and others to show that anonymous authentication is now operational at Internet scale.

[Read original article](https://blog.cryptographyengineering.com/2026/04/17/anonymous-credentials-an-illustrated-primer-part-2/){: .btn .btn-primary }
