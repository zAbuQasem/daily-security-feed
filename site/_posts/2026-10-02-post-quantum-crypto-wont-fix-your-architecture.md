---
layout: post
title: "Post-Quantum Crypto Won't Fix Your Architecture"
date: 2026-10-02 10:11:28 +0300
categories: [RSS]
tags: [crypto, rce, key-management, cloud]
toc: true
---

A comprehensive security audit of Internxt, a post-quantum-encrypted cloud storage provider, uncovering critical architectural and implementation flaws. The researcher discovered remote code execution in the desktop application (≤2.6.12), unauthenticated key exchange enabling man-in-the-middle attacks, and a fundamentally broken key hierarchy where the master mnemonic is shared unencrypted with other users when enabling folder sharing—giving both attackers and Internxt backend access to all file encryption keys. Additional vulnerabilities include weak password derivation (3 MD5 iterations) and lack of key pinning or verification. The audit demonstrates that post-quantum cryptography claims are undermined by deeper architectural problems: the system requires trusting Internxt not to intercept the master key during user-to-user sharing, and no TOFU or out-of-band verification prevents such interception. Findings were responsibly disclosed three months prior; while the RCE fix was merged, it had not been released as of publication.

[Read original article](https://schaerli.org/weblog/6-internxt//){: .btn .btn-primary }
