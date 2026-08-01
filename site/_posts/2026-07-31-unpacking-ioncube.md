---
layout: post
title: "Unpacking ionCube"
date: 2026-07-31 22:25:00 +0300
categories: [RSS]
tags: [reverse-engineering, cryptography, obfuscation, php]
toc: true
---

A technical reverse engineering analysis of ionCube, a commercial PHP encoder/obfuscator, using Binary Ninja. The author details the multi-layered cryptographic protection scheme: base64-encoded payloads with custom alphabet are decrypted using keys derived from Jenkins's one-at-a-time hash and MurmurHash3-32, seeding a dual 16-bit MWC (Multiply-with-carry) PRNG that generates a keystream. ionCube supports five key derivation methods, including a novel anti-tamper mechanism that executes a designated function and hashes its bytecode as part of key material. Crucially, evaluation/unlicensed files use an all-zero constant key, making them fully decodable offline. The decrypted payload reconstructs PHP opcodes within ionCube's statically-linked Zend VM, protected by a custom reflection API reimplementation and deserialization pipeline.

[Read original article](https://dustri.org/b/unpacking-ioncube.html){: .btn .btn-primary }
