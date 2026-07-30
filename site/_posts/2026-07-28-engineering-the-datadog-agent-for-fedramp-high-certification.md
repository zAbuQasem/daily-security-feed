---
layout: post
title: "Engineering the Datadog Agent for FedRAMP High® Certification"
date: 2026-07-28 00:00:00 +0300
categories: [RSS]
tags: [compliance, cryptography, infrastructure, fedramp]
toc: true
---

Datadog engineers its Agent to meet FedRAMP High certification by moving cryptographic enforcement from an external proxy into the Agent itself, ensuring FIPS-validated cryptography operates across Go and Python runtimes with well-defined cryptographic boundaries. The High baseline's 400+ controls require stricter guarantees than the previous proxy-based architecture (FIPS Proxy) could provide, particularly around handling customer integrations that perform internal cryptographic operations. The new design implements deterministic failure modes, cryptographic boundary enforcement, and continuous compliance validation to withstand High baseline requirements during patches, updates, and environment changes. This technical deep-dive is valuable for organizations engineering systems that must maintain cryptographic control over software running in customer-managed infrastructure without vendor visibility into the surrounding operating system or network configuration.

[Read original article](https://www.datadoghq.com/blog/engineering-the-datadog-agent-for-fedramp-high/){: .btn .btn-primary }
