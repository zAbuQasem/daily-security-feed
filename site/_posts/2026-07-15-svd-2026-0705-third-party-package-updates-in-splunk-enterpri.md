---
layout: post
title: "SVD-2026-0705: Third-Party Package Updates in Splunk Enterprise - July 2026"
date: 2026-07-15 00:00:00 +0300
categories: [RSS]
tags: [splunk, cve, patch, supply-chain]
toc: true
---

Splunk released critical patches for multiple third-party dependencies in Enterprise versions 9.4.13, 10.0.8, 10.2.5, and 10.4.1. Updates address high- and critical-severity CVEs in Go compiler (1.25.9–1.26.3), MongoDB (7.0.34, 8.0.23), golang-jwt/v5 (5.2.2), go-jose/v4 (4.1.4), and OpenTelemetry SDK (1.43.0). Go compiler CVEs include multiple vulnerabilities across compiler, cryptography, and runtime; MongoDB CVEs span security and stability across versions. The advisory provides specific binary paths (edge, cmp-orchestrator, etcd, mongod) affected per component, making patch application version-specific. Splunk admins operating affected versions should prioritize upgrading to remediate supply-chain exposure.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0705){: .btn .btn-primary }
