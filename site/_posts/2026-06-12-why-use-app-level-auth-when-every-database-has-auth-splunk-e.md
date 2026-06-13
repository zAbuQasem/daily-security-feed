---
layout: post
title: "Why Use App-Level Auth When Every Database Has Auth? (Splunk Enterprise CVE-2026-20253 Pre-Auth RCE)"
date: 2026-06-12 20:35:13 +0300
categories: [RSS]
tags: [splunk, rce, pre-auth, cve, cloud]
toc: true
---

CVE-2026-20253 is a pre-auth remote code execution vulnerability in Splunk Enterprise v10+ affecting the PostgreSQL Sidecar Service. The vulnerability allows unauthenticated attackers to reach the internal PostgreSQL sidecar API (normally bound to localhost:5435) by proxying requests through the main Splunk web application endpoint /en-US/splunkd/__raw/v1/postgres/recovery/backup. Splunk Enterprise deployments on AWS are vulnerable by default, and the sidecar service is enabled by default on AWS while being optional or disabled by default on on-premise Windows installations. The vulnerability enables file write and database manipulation through backup/restore endpoints accessible without authentication, resulting in a CVSS score of 9.8. This is a novel bypass technique leveraging internal service proxying to circumvent the localhost-only binding restriction.

[Read original article](https://labs.watchtowr.com/why-use-app-level-auth-when-every-database-has-auth-splunk-enterprise-cve-2026-20253-pre-auth-rce/){: .btn .btn-primary }
