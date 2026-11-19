---
layout: post
title: "Drone Hacking Part 2: Authorized ~_~ by Potensic ~_~"
date: 2026-11-19 00:00:00 +0300
categories: [RSS]
tags: [reverse-engineering, firmware, iot, wifi, weak-crypto]
toc: true
---

Detailed reverse engineering of the Potensic Atom 2 drone ecosystem reveals a critical WiFi password vulnerability: the access point password is derived directly from the last four characters of the publicly broadcast device ID via hex-encoded ASCII values, allowing attackers within WiFi range to connect and exfiltrate photos and videos. The authors reverse engineered multiple communication channels (app-to-drone BLE/WiFi, app-to-RC USB/AOA, RC-to-drone proprietary protocol using Artosyn AR8030 baseband), analyzed the firmware update flow by decompiling the Android app with JADX (bypassing certificate pinning via Magisk), and uncovered undocumented debug functionality. The write-up demonstrates practical firmware extraction via NAND desoldering, ECC correction, and systematic protocol analysis of consumer IoT hardware.

[Read original article](https://neodyme.io/en/blog/drone_hacking_part_2/){: .btn .btn-primary }
