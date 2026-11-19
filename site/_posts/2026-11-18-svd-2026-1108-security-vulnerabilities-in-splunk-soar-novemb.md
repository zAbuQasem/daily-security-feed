---
layout: post
title: "SVD-2026-1108: Security Vulnerabilities in Splunk SOAR - November 2026"
date: 2026-11-18 00:00:00 +0300
categories: [RSS]
tags: [rce, authorization-bypass, access-control, xss, splunk]
toc: true
---

Splunk addressed 23 vulnerabilities in Splunk SOAR (versions prior to 8.8.0), including multiple critical remote code execution flaws via the App Wizard (CVE-2026-131253, 9.9 CVSS) and REST API endpoints (CVE-2026-131256, CVE-2026-131261). Additional high-impact issues include authorization bypasses across multiple APIs, improper access controls allowing cross-tenant asset manipulation (CVE-2026-131252, 8.8 CVSS), stored and reflected XSS via REST endpoints, privilege escalation through user role assignment, and information disclosure affecting sensitive configuration and credentials. Authenticated attackers can exploit these to gain RCE, escalate privileges, bypass authorization controls, and exfiltrate sensitive data; unauthenticated users can trigger privilege escalation via CVE-2026-131255. Immediate patching to version 8.8.0 or higher is critical for all Splunk SOAR deployments.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1108){: .btn .btn-primary }
