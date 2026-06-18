---
layout: post
title: "SVD-2026-0614: OS Command Injection in the btool Configuration Helper in Splunk AI Toolkit"
date: 2026-06-17 00:00:00 +0300
categories: [RSS]
tags: [rce, splunk, cve, command-injection]
toc: true
---

Splunk AI Toolkit versions below 5.7.4 are vulnerable to OS command injection in the btool configuration helper (CVE-2026-20266, CVSS 9.1 Critical). The vulnerability results from unsafe shell execution patterns where OS command strings are constructed from dynamic parameters without disabling shell interpretation or proper escaping. An attacker with admin role can execute arbitrary OS commands on the Splunk Enterprise host with full system compromise (C/I/A) and scope change impact. Mitigation requires upgrade to version 5.7.4 or uninstallation of the affected toolkit component.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0614){: .btn .btn-primary }
