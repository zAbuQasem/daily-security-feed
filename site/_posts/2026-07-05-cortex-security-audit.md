---
layout: post
title: "Cortex Security Audit"
date: 2026-07-05 22:00:00 +0300
categories: [RSS]
tags: [cloud, multi-tenant, authentication, xss, audit]
toc: true
---

Quarkslab's security audit of Cortex (an open-source, horizontally scalable multi-tenant Prometheus metrics store) identified 7 vulnerabilities spanning tenant isolation and data segregation. Critical findings include tenant impersonation via the PushStream gRPC handler (high-impact, low-probability attack), stored XSS in the UI, information leakage from the /config endpoint exposing sensitive credentials, unbound Gzip decompression, uncontrolled protobuf histogram memory allocation, and gossip protocol weaknesses (unbounded reads and missing integrity checks). All vulnerabilities have been remediated. The audit highlights multi-tenant isolation risks in cloud infrastructure monitoring at scale and reinforces the importance of secure-by-default configurations and centralized input validation.

[Read original article](http://blog.quarkslab.com/cortex-security-audit.html){: .btn .btn-primary }
