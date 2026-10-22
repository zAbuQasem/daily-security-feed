---
layout: post
title: "SVD-2026-1011: Security Hardening in Splunk SOAR - October 2026"
date: 2026-10-21 00:00:00 +0300
categories: [RSS]
tags: [splunk, soar, cves, access-control]
toc: true
---

Splunk SOAR versions prior to 8.7.0 contain eight internally identified vulnerabilities ranging from CVSS 5.5 to 9.9 (critical). The vulnerabilities span access control (CWE-284, score 9.3), improper resource lifetime control (CWE-664, 8.8), improper input neutralization (CWE-707, 8.8), alternate path bypass (CWE-424, 7.5), unauthorized file/directory access (CWE-552, 9.9), and exception handling weaknesses (CWE-703, 5.5). The advisory provides no technical explanation of exploitation methods or attack surface, requiring users to either upgrade or consult CVE details for more information. Immediate patching to SOAR 8.7.0 is recommended given the critical severity scores.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1011){: .btn .btn-primary }
