---
layout: post
title: "SVD-2026-1005: Third-Party Package Updates in Splunk Add-on for Amazon Web Services - September 2026"
date: 2026-10-07 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, dependencies, splunk, aws, golang]
toc: true
---

Splunk released a security advisory for the Add-on for Amazon Web Services version 8.2.2, patching multiple critical and high-severity vulnerabilities in bundled third-party libraries: Go compiler (23 CVEs including CVE-2026-39820, CVE-2026-39823), golang.org/x/net (12 CVEs including CVE-2026-33814), google.golang.org/grpc (CVE-2026-33186), Apache Thrift (CVE-2026-41602), and cryptography (7 CVEs). The vulnerable code resides in the parquet_decoder binaries across Linux and Windows distributions. Organizations running Splunk Add-on for AWS versions below 8.2.2 should upgrade immediately to remediate this cascading dependency vulnerability chain affecting core Go networking and serialization libraries.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1005){: .btn .btn-primary }
