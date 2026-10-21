---
layout: post
title: "MbedTLS Security Audit"
date: 2026-10-19 22:00:00 +0300
categories: [RSS]
tags: [tls, crypto, audit, embedded]
toc: true
---

Quarkslab's OSTIF-commissioned security audit of MbedTLS 4.0 assessed the major architectural refactoring that extracted cryptography into the standalone TF-PSA-Crypto library implementing PSA Cryptography API v1.2. Findings included a HIGH-severity heap buffer overflow in `mbedtls_ssl_context_load()` during session deserialization and a LOW-severity issue where `mbedtls_pk_verify()` accepts unvalidated BER-encoded signatures; three informational findings covered 0-RTT anti-replay gaps and test infrastructure issues. The audit comprehensively reviewed the TLS/crypto layer trust boundary, PSA API correctness, memory safety in SSL/DTLS and X.509 parsing, default configurations, and RFC compliance—essential for MbedTLS's use across IoT, automotive, industrial, and Trusted Firmware infrastructure. All vulnerabilities have been resolved.

[Read original article](http://blog.quarkslab.com/mbedtls-security-audit.html){: .btn .btn-primary }
