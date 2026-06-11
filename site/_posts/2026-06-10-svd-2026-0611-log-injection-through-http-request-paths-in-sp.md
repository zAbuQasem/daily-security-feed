---
layout: post
title: "SVD-2026-0611: Log Injection through HTTP Request Paths in Splunk SOAR"
date: 2026-06-10 00:00:00 +0300
categories: [RSS]
tags: [log-injection, cve, input-validation, splunk-soar]
toc: true
---

Splunk SOAR versions below 8.5.0 are vulnerable to ANSI escape code injection through HTTP request paths (CVE-2026-20260). The vulnerability stems from SOAR failing to strip control characters from request paths before writing them to application logs. An unauthenticated attacker can craft malicious HTTP requests with ANSI escape sequences embedded in the path, which are then logged; when an administrator views logs in a terminal emulator, the escape sequences execute, potentially causing log spoofing or terminal manipulation. The attack requires user interaction (admin viewing logs) and has a Medium CVSS score of 4.3. Fix: upgrade to SOAR 8.5.0 or higher.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0611){: .btn .btn-primary }
