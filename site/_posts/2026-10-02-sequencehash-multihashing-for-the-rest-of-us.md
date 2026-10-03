---
layout: post
title: "SequenceHash: multihashing for the rest of us"
date: 2026-10-02 11:00:00 +0300
categories: [RSS]
tags: [cryptography, multihashing, zk-proofs, standards, defensive]
toc: true
---

Trail of Bits introduces SequenceHash and SequenceMAC, hash-agnostic multihashing constructs that solve the security problem of combining multiple inputs into a single hash via unambiguous encoding. Unlike NIST's TupleHash (limited to Keccak/SHA3), SequenceHash uses length-prefix encoding to work with any secure hash function (SHA2, BLAKE, RIPEMD) and prevents collision attacks that arise from simple concatenation. The constructions are critical for securing Fiat-Shamir transforms in zero-knowledge proofs, cryptographic commitments, and any protocol requiring authenticated multi-input hashes. Trail of Bits releases production implementations in Rust, Go, and Python with comprehensive test vectors and contributes a full specification to the Community Cryptography Specification Project (C2SP).

[Read original article](https://blog.trailofbits.com/2026/10/02/sequencehash-multihashing-for-the-rest-of-us/){: .btn .btn-primary }
