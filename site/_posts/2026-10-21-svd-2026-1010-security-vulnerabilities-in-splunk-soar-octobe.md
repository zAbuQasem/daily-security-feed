---
layout: post
title: "SVD-2026-1010: Security Vulnerabilities in Splunk SOAR - October 2026"
date: 2026-10-21 00:00:00 +0300
categories: [RSS]
tags: [cve, access-control, info-disclosure, xss]
toc: true
---

Splunk SOAR versions below 8.7.0 contain seven CVEs spanning authentication, authorization, and information disclosure flaws. CVE-2026-76306 and CVE-2026-76307 allow authenticated users with the Observer role to infer password hashes and authorization tokens via unprotected REST API query filters applied before sensitive field masking. CVE-2026-76305 permits unauthorized users to download app archives exposing proprietary source code. CVE-2026-76303 enables stored XSS through app documentation via improper sanitization, while CVE-2026-76304 leaks Automation Broker Docker Compose configuration including SOAR instance URLs. All require authentication or high-privilege roles and affect the enterprise SOAR automation platform; upgrade to 8.7.0 resolves all issues.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1010){: .btn .btn-primary }
