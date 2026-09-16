---
layout: post
title: "Turning WerEnc.dll LOLBIN into an attacker-controlled encryption primitive (BYOK)"
date: 2026-09-15 17:53:25 +0300
categories: [RSS]
tags: [lolbin, encryption, evasion, opsec, windows]
toc: true
---

Windows ships an unused but functional LOLBIN, WerEnc.dll, that implements AES-256+RSA-4096 hybrid encryption for WER artifacts. Researchers reverse-engineered the embedded RSA-4096 public key (4KB blob at RVA 0x5610) and demonstrated a "Bring Your Own Key" (BYOK) technique: patching 539 bytes in memory to swap Microsoft's public key for an attacker-controlled one, then calling EncryptDumpFile/EncryptDumpStream to produce encrypted output indistinguishable from legitimate WER dumps. The attack bypasses EDR detection (RC4 via SystemFunction033 is flagged; WerEnc loading is undetected), providing red teams and malware a signed, high-entropy encryption primitive with container format mimicking legitimate artifacts.

[Read original article](https://0xsp.com/research/turning-werenc-dll-lolbin-into-an-attacker-controlled-encryption-primitive-byok/?utm_source=rss&utm_medium=rss&utm_campaign=turning-werenc-dll-lolbin-into-an-attacker-controlled-encryption-primitive-byok){: .btn .btn-primary }
