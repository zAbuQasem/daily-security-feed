---
layout: post
title: "SVD-2026-0804: Security Hardening Release for Splunk SOAR - August 2026"
date: 2026-08-19 00:00:00 +0300
categories: [RSS]
tags: [authentication-bypass, rce, path-traversal, sqli, ssrf]
toc: true
---

Splunk released a security hardening advisory addressing 14 vulnerabilities in SOAR versions below 8.6.0, with a critical authentication bypass (CVE-2026-76356, CVSS 8.1) allowing unauthenticated RCE via IP address spoofing in the Automation Broker notification endpoint—the vulnerability exploits insufficient validation of client-supplied IP headers. The advisory also covers multiple path traversal issues in app/forwarder installation and REST API handlers (CVE-2026-76357, CVSS 7.6 for authenticated but role-less users), SQL injection in REST API and custom function/list processing, SSRF in connectivity checks, and information disclosure through missing authorization controls. Remediation requires upgrade to 8.6.0 or higher, with additional manual steps required for CVE-2026-76362 (CyberArk Vault certificate validation).

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-0804){: .btn .btn-primary }
