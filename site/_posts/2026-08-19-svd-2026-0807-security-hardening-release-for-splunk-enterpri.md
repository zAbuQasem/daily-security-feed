---
layout: post
title: "SVD-2026-0807: Security Hardening Release for Splunk Enterprise Security - August 2026"
date: 2026-08-19 00:00:00 +0300
categories: [RSS]
tags: [injection, privilege-escalation, access-control, splunk]
toc: true
---

Splunk Enterprise Security 8.6.0 and below contain two high-severity vulnerabilities (CVSS 8.1): CVE-2026-76387 is an SPL injection flaw in the Analyst Queue REST API where unvalidated search filter field names are concatenated directly into SPL queries, allowing authenticated users with mc_investigation_read to access all data available to scheduled searches; CVE-2026-76388 is a privilege escalation via UEBA search macro permissions, where the UEBA app metadata incorrectly grants analyst roles write access to search macros executed with administrator privileges. Both require authentication but grant full confidentiality and integrity compromise. Fix: upgrade to Splunk Enterprise Security 8.6.1 or higher.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-0807){: .btn .btn-primary }
