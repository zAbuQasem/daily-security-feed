---
layout: post
title: "Discovering a Backdoor and Flaws in More Encrypted USB Drives"
date: 2026-10-22 16:00:00 +0300
categories: [RSS]
tags: [backdoor, cryptography, reverse-engineering, encryption, ai-security]
toc: true
---

Binary Ninja researchers used AI-assisted reverse engineering to break multiple encrypted USB drive products, discovering backdoors and fundamental cryptographic flaws in commercial copy-protection solutions. YutianDun's system contains hardcoded account credentials (Buffer/123456, System/SECZURE.COM) that decrypt files regardless of the administrator password, and uses weak cryptography: MD5 for hashing, HMAC-MD5 with only 64-bit effective key entropy, and ECB-mode AES encryption. NetacFileLock stores a fixed 32-byte AES-256 key in the executable, allowing anyone to decrypt files without knowing the user's password—a flaw AI discovered through static analysis in just seven minutes. KakaSoft's 'Highest' encryption setting uses 256-bit Blowfish with weak key derivation. The research underscores how security through obscurity in opaque binary-only products creates dangerous false confidence.

[Read original article](https://binary.ninja/2026/10/22/breaking-more-encrypted-usb-drives-with-ai.html){: .btn .btn-primary }
