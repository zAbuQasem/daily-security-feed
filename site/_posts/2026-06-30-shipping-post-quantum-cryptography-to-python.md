---
layout: post
title: "Shipping post-quantum cryptography to Python"
date: 2026-06-30 11:00:00 +0300
categories: [RSS]
tags: [post-quantum, cryptography, supply-chain, nist]
toc: true
---

Trail of Bits has implemented ML-KEM (NIST FIPS 203) and ML-DSA (NIST FIPS 204) in pyca/cryptography 48+, bringing NIST-standard post-quantum key encapsulation and digital signatures to Python. The article details practical tradeoffs: ML-DSA-65 signatures are ~52× larger than Ed25519 (3,309 B vs 64 B), and ML-KEM-768 ciphertexts are ~34× larger than X25519 (1,088 B vs 32 B). Since pyca/cryptography is the 11th most-downloaded PyPI package (~1.2B monthly downloads), this work unblocks Python ecosystem migration toward the White House's post-quantum cryptography mandate (key establishment by 2030, signatures by 2031). The article includes concrete code examples and discusses protocol integration requirements.

[Read original article](https://blog.trailofbits.com/2026/06/30/shipping-post-quantum-cryptography-to-python/){: .btn .btn-primary }
