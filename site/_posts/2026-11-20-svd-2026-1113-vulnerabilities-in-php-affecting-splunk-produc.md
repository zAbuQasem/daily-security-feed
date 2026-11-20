---
layout: post
title: "SVD-2026-1113: Vulnerabilities in PHP affecting Splunk Products - November 2026"
date: 2026-11-20 00:00:00 +0300
categories: [RSS]
tags: [php, cve, use-after-free, request-smuggling, splunk]
toc: true
---

Splunk published an advisory on seven PHP security vulnerabilities released on November 19, 2026, including CVE-2026-129289 (PHP-FPM request smuggling via unread request body), CVE-2026-129182/129474/129481 (use-after-free issues in fatal error backtraces, magic method backtraces, and session shutdown), CVE-2026-115560/126714 (session serialization and partial file overwrite issues), and CVE-2026-129496 (timezone cache use-after-free). Splunk investigated its product portfolio and confirmed that all major products—including Splunk Cloud Platform, Enterprise, Security, SOAR, Observability, and AppDynamics—are unaffected by these PHP vulnerabilities. This advisory demonstrates vendor transparency and may be relevant for organizations running PHP-dependent services outside Splunk's ecosystem.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1113){: .btn .btn-primary }
