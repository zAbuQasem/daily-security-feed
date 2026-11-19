---
layout: post
title: "SVD-2026-1111: Security Vulnerabilities in Splunk AI Assistant - November 2026"
date: 2026-11-18 00:00:00 +0300
categories: [RSS]
tags: [authorization, access-control, splunk, api]
toc: true
---

Splunk AI Assistant versions below 2.0.0 contain four authorization and input validation vulnerabilities in the REST API. CVE-2026-131304 allows unauthenticated users to bypass authorization by submitting a client-controlled tenant identifier, enabling cross-tenant data access and action attribution (CVSS 8.1). CVE-2026-131305 permits modification of response metadata through unvalidated feature settings (CVSS 8.1). CVE-2026-131303 allows disclosure of indexes and data sources outside authorized scope (CVSS 7.1), while CVE-2026-131302 permits non-admin users to modify AI chat training-data consent settings (CVSS 4.3). All are fixed in version 2.0.0.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1111){: .btn .btn-primary }
