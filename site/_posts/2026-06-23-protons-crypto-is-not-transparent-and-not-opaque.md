---
layout: post
title: "Proton's crypto is not Transparent and not OPAQUE"
date: 2026-06-23 13:43:42 +0300
categories: [RSS]
tags: [key-transparency, cryptography, mitm, disclosure, encryption]
toc: true
---

A flaw in Proton's Key Transparency implementation allows man-in-the-middle attacks by exploiting the client's trust in server-provided email addresses during self-audit. When verifying its own public key, the client fetches its address from the untrusted backend and audits the wrong row, enabling Proton to serve a forged key for the real address while users receive a valid verification result. Additionally, ProtonPass lacks Key Transparency protection despite marketing claims that key sharing is verified via KT. This responsibly-disclosed vulnerability undermines Proton's core privacy guarantee that servers cannot intercept encrypted communications, and highlights the critical importance of binding user identity cryptographically to key transparency logs rather than relying on server-provided labels.

[Read original article](https://schaerli.org/weblog/5-proton//){: .btn .btn-primary }
