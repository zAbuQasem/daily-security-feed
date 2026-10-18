---
layout: post
title: "Two Hawks in a Pod: one Android RAT behind a flock of fake Japanese brands"
date: 2026-10-17 00:00:00 +0300
categories: [RSS]
tags: [malware, android, rat, fraud, reverse-engineering]
toc: true
---

A coordinated Android malware campaign uses dropper apps impersonating legitimate Japanese brands (e-Tax, Rakuten, LINE, Mercari) to deliver a WebSocket-based RAT controlled from two identical panels branded as 'Black Hawk' and 'Eagle' Android Remote Control. The two-stage attack chains a libsa native XOR packer (with plaintext 32-byte keys in the binary) to an nmmp VM-protected RAT, with capabilities to steal lock-screen credentials and patterns, intercept payment input, mirror the screen, and escalate privileges so operators can open banking apps and execute transfers undetected. Analysis of 64 samples (Sept 15–Oct 16, 2026) identifies consistent dropper fingerprints and component structure, alongside actionable indicators including specific APK hashes, package name patterns, and permission abuse patterns.

[Read original article](https://starlabs.sg/blog/2026/10-two-hawks-in-a-pod-one-android-rat-behind-a-flock-of-fake-japanese-brands/){: .btn .btn-primary }
