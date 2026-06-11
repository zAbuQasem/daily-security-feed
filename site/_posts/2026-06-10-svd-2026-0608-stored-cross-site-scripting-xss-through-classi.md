---
layout: post
title: "SVD-2026-0608: Stored Cross-Site Scripting (XSS) through Classic Dashboard in Splunk Enterprise"
date: 2026-06-10 00:00:00 +0300
categories: [RSS]
tags: [xss, stored-xss, splunk, cve]
toc: true
---

A stored XSS vulnerability (CVE-2026-20258, CVSS 7.1) in Splunk Enterprise and Cloud Platform allows low-privileged users to inject malicious JavaScript into classic dashboard HTML panels, executing arbitrary code in other users' browsers when they click a phishing link. Affects Splunk Enterprise 10.2.3 and below, 10.0.6 and below, 9.4.11 and below, and 9.3.12 and below; patched in 10.2.4, 10.0.7, 9.4.12, and 9.3.13. The attack surface is minimal due to default Splunk Web configuration (dashboard_html_allow_embeddable_content defaults to false, which blocks the exploit) and the requirement for social engineering.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0608){: .btn .btn-primary }
