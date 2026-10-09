---
layout: post
title: "Novinarya: An Android stealer that hides its live C2 in a shop bio"
date: 2026-10-08 00:00:00 +0300
categories: [RSS]
tags: [malware, android, banking, c2, reverse-engineering]
toc: true
---

Novinarya is a two-layer Android stealer targeting 54 cryptocurrency exchanges and 27 Iranian banking apps, using native packing (libuibridge_9203.so) with RC4 encryption (32-byte key, 768-byte keystream drop) and zlib compression to obfuscate its Basic4Android payload. The malware employs a novel dead-drop C2 infrastructure, resolving its command server from an encrypted manifest metadata value (AES-CBC keyed by X_CID) to a legitimate marketplace seller profile, then decrypting the bio field to retrieve the live C2 address—enabling operator-controlled rotation without repackaging. Credential theft occurs via phishing WebView with a JavaScript form-grabber over a native bridge, while SMS and notification interception captures account numbers, balances, and OTP codes from 25 hardcoded banking regex patterns. The analysis recovered the live C2 (theapi.the-x-services[.]xyz) from the active Basalam marketplace profile (m6AJm5), demonstrating the full attack chain with shared inner dex across multiple builds.

[Read original article](https://starlabs.sg/blog/2026/10-novinarya-an-android-stealer-that-hides-its-live-c2-in-a-shop-bio/){: .btn .btn-primary }
