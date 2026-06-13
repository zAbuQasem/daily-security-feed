---
layout: post
title: "Factoring \"short-sleeve\" RSA keys with polynomials"
date: 2026-06-12 11:00:00 +0300
categories: [RSS]
tags: [rsa, cryptanalysis, keygen, supply-chain]
toc: true
---

Trail of Bits and Hanno Böck discovered a polynomial-based cryptanalytic technique that factors RSA keys where bits are heavily biased toward 0, converting integer factorization into polynomial factorization. By representing integers as polynomials in base-2^w (where w is the limb size), keys with structured zero blocks yield polynomials with exceptionally small coefficients that are efficiently factorable. They identified two real-world patterns: pattern 1 in certificates from Yahoo, Verizon, and NetApp devices (now expired), and pattern 2 traced to a type mismatch bug in CompleteFTP versions 10.0.0–12.0.0 (RSA) and 10.0.0–23.0.4 (DSA). Internet scans recovered 603 unique RSA private keys and 74 DSA keys with these vulnerabilities, demonstrating tangible impact.

[Read original article](https://blog.trailofbits.com/2026/06/12/factoring-short-sleeve-rsa-keys-with-polynomials/){: .btn .btn-primary }
