---
layout: post
title: "SVD-2026-1003: Third-Party Package Updates in Splunk Enterprise - September/October 2026"
date: 2026-10-07 00:00:00 +0300
categories: [RSS]
tags: [cve, splunk, patch, critical]
toc: true
---

Splunk Enterprise has released patches for multiple critical-severity vulnerabilities in bundled third-party Go libraries affecting etcd, etcdutl, spl2-preview, compsup, and agent-manager binaries. Vulnerabilities addressed include cryptographic flaws in golang.org/x/crypto (CVE-2026-39830–39834, CVE-2026-42508, CVE-2026-46595), network handling issues in golang.org/x/net (CVE-2026-39821, CVE-2026-27141), JWT signing vulnerabilities in go-jose (CVE-2026-34986), and HTTP client vulnerabilities in libcurl. Organizations running Splunk Enterprise versions 9.4.0–10.4.2 should upgrade to patched versions 9.4.15, 10.0.10, 10.2.7, or 10.4.3 or later.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1003){: .btn .btn-primary }
