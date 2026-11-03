---
layout: post
title: "Filen's password onion made me cry"
date: 2026-11-03 10:55:33 +0300
categories: [RSS]
tags: [cryptography, e2e, cloud-storage, password-hashing, downgrade-attack]
toc: true
---

Security researcher discloses multiple cryptographic weaknesses in Filen's end-to-end encrypted cloud storage. The protocol supports deprecated password hashing via cascaded legacy functions (MD2/MD4/MD5/SHA1/SHA256/SHA384/SHA512) that are computationally efficient to brute-force; servers can trigger downgrade attacks at login to harvest weak hashes from any account. Filename search was implemented using HMAC-hashed character chunks, vulnerable to statistical attacks via substitution cipher analysis by analyzing chunk frequencies. File sharing uses unauthenticated recipient public keys, enabling man-in-the-middle attacks to intercept encrypted metadata and keys during uploads, moves, and renames. Latest versions address password hashing with argon2 and phase out server-side search, but backward compatibility and unauthenticated key handling remain exploitable.

[Read original article](https://schaerli.org/weblog/7-filen//){: .btn .btn-primary }
