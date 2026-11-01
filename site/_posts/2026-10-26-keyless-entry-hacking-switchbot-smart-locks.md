---
layout: post
title: "Keyless Entry: Hacking SwitchBot Smart Locks"
date: 2026-10-26 00:00:00 +0300
categories: [RSS]
tags: [crypto, ble, iot, hardware, bit-flip]
toc: true
---

The SwitchBot Lock Pro series contains a critical cryptographic flaw in its Bluetooth Low Energy communication protocol. The device uses AES in counter (CTR) mode for encryption without integrity protection, enabling bit-flip attacks that exploit the malleability of stream ciphers. By XORing a captured encrypted LOCK command with a precomputed difference (computed once across all devices), an attacker can convert it into a valid encrypted UNLOCK command. The attack requires no physical tampering and silently opens doors from within Bluetooth range. While SwitchBot has already patched the vulnerability and deployed firmware updates, this research demonstrates the critical risks of deploying malleable encryption modes without authentication in security-critical IoT devices.

[Read original article](https://neodyme.io/en/blog/switchbot/){: .btn .btn-primary }
