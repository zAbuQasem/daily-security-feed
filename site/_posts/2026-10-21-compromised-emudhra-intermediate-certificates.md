---
layout: post
title: "Compromised eMudhra intermediate certificates"
date: 2026-10-21 20:43:29 +0300
categories: [RSS]
tags: [pki, supply-chain, cloud, tls, cve]
toc: true
---

eMudhra's key generation ceremony on April 30, 2025 produced eight intermediate CA certificates with catastrophically weak P-384 keys—entropy reduced from 384 bits to 3–8 bits during a wrap/unwrap step, making private key recovery trivial. Six TLS intermediates and two code-signing intermediates are affected; attackers with these keys could issue fraudulent certificates to impersonate any website or service. Major browsers (Chrome, Mozilla, Apple) and Microsoft blocked the affected TLS and code-signing keys, but embedded certificate stores in cloud-native systems (Go crypto/x509, Docker, Kubernetes, Terraform, Prometheus) are exposed because they rely on static or legacy root pools that ignore revocation. The Go team released CVE-2026-111943 (Go 1.27.3, 1.26.10) to hardcode the compromised certificate hashes, and enterprises must audit VPN appliances, proxies, load balancers, and package managers for exposure through stale trust stores or validation paths that still accept the affected intermediates. No active exploitation has been observed as of October 21, 2026.

[Read original article](https://blog.talosintelligence.com/compromised-intermediate-certificates/){: .btn .btn-primary }
