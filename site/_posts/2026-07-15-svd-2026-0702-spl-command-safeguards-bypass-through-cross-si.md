---
layout: post
title: "SVD-2026-0702: SPL Command Safeguards Bypass through Cross-Site Request Forgery (CSRF) in Deployment Server in Splunk Enterprise"
date: 2026-07-15 00:00:00 +0300
categories: [RSS]
tags: [csrf, splunk, command-execution]
toc: true
---

A CSRF vulnerability in Splunk Enterprise and Cloud Platform's Deployment Server endpoints allows attackers to trick users into executing arbitrary SPL (Search Processing Language) searches as the `splunk-system-user` account. The vulnerability stems from missing CSRF token validation on GET requests combined with improper input sanitization, enabling command injection through the SPL search engine. An attacker must phish a victim with the `list_deployment_server` role to trigger the malicious request, but successful exploitation grants access to stored credentials and indexed data with CVSS 8.3 (High). Affected versions span Splunk Enterprise 9.4.0–9.4.12, 10.0.0–10.0.7, 10.2.0–10.2.4, and 10.4.0, plus multiple Splunk Cloud Platform releases. Patched versions are available for all affected branches (Enterprise 9.4.13, 10.0.8, 10.2.5, 10.4.1 and later).

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0702){: .btn .btn-primary }
