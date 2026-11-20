---
layout: post
title: "Breaking Free:  A New Jailbreak for the Unitree Go2"
date: 2026-11-19 22:03:34 +0300
categories: [RSS]
tags: [ble, iot, buffer-overflow, rce, reverse-engineering]
toc: true
---

Praetorian researchers discovered a pre-authentication crash in the Unitree Go2's btgatt-server binary via Bluetooth Low Energy (BLE) GATT messages. The vulnerability stems from improper length validation in EVP_DecryptUpdate: the outer parser fails to verify that declared nonce, tag, and ciphertext lengths fit within the received GATT value, and attacker-controlled ct_len is passed to EVP_DecryptUpdate without output buffer capacity checks. This allows an unauthenticated attacker to trigger a buffer overflow via crafted BLE messages, leading to denial of service or arbitrary code execution without requiring the device's AES key. The team demonstrated the PoC using their Caeruleus BLE testing tool and obtained root access on the robot dog, exposing a significant attack surface in a widely-available consumer IoT device.

[Read original article](https://www.praetorian.com/blog/breaking-free-a-new-jailbreak-for-the-unitree-go2/){: .btn .btn-primary }
