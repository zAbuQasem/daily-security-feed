---
layout: post
title: "How to Hack Time, With C2PA"
date: 2026-10-02 00:00:00 +0300
categories: [RSS]
tags: [c2pa, cryptography, spec-flaw, authentication]
toc: true
---

A specification footgun in C2PA (Coalition for Content Provenance and Authenticity) allows attackers to create cryptographically valid signatures that cover an empty string by deliberately excluding an entire file's byte range from signature calculations. Once excluded, files can be arbitrarily modified (e.g., photoshopped) after signing without invalidating the signature or tamper-proof timestamp from a Time Stamp Authority. The author demonstrates this with a PoC that claims to have photographed tomorrow's lottery numbers hours in advance, with a valid C2PA manifest and RFC 3161 timestamp proof. While exclusions are necessary in the spec for legitimate reasons (e.g., PNG CRC checksums), current C2PA verifiers do not enforce constraints on which parts can be excluded, making deliberate abuse undetectable. The fundamental tension is that any fix must distinguish between harmless exclusions and those that could completely alter image content without invalidating signatures.

[Read original article](https://www.da.vidbuchanan.co.uk/blog/hacking-time.html){: .btn .btn-primary }
