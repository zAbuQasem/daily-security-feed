---
layout: post
title: "SVD-2026-1001: Security Vulnerabilities in Splunk Enterprise - September/October 2026"
date: 2026-10-07 00:00:00 +0300
categories: [RSS]
tags: [access-control, authentication, splunk, sqli, ssrf]
toc: true
---

Splunk released a critical advisory covering 16 CVEs in Splunk Enterprise and Secure Gateway, with the highest being CVE-2026-76268 (CVSS 9.8)—missing authentication on the Patroni REST API in Splunk Enterprise allows unauthenticated remote code execution. Additional critical findings include authorization bypasses in REST API endpoints (CVE-2026-76265, CVE-2026-76269), SQL injection in the SPL2 Module Catalog (CVE-2026-76270), SSRF in the Observability Cloud app (CVE-2026-76274), and local privilege escalation through package upgrades (CVE-2026-76266). Patched versions: 10.4.3, 10.2.7, 10.0.10, 9.4.15; additional configuration changes required for some CVEs.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1001){: .btn .btn-primary }
