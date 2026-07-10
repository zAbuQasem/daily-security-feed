---
layout: post
title: "Not-so-anonymous telemetry: The @injectivelabs/sdk-ts backdoor"
date: 2026-07-09 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, npm, credential-theft, malware, blockchain]
toc: true
---

A malicious commit injected a hidden credential-stealing module into @injectivelabs/sdk-ts (v1.20.21), a popular TypeScript SDK for the Injective blockchain with 175,000+ monthly downloads. The attacker hooked the PrivateKey.fromMnemonic() and PrivateKey.fromHex() functions to capture raw BIP-39 seed phrases and private keys at wallet load time, base64-encoding them and exfiltrating them via the X-Request-Id HTTP header to a remote endpoint. Forensic analysis of Git metadata (UTC-4 timezone anomaly, direct-to-main push, CI fix attempts) indicates account compromise. The malicious version was live for approximately 49 minutes before the legitimate maintainer reverted it and released v1.20.23.

[Read original article](https://securitylabs.datadoghq.com/articles/not-so-anonymous-telemetry-injectivelabs-sdk-ts-backdoor/){: .btn .btn-primary }
