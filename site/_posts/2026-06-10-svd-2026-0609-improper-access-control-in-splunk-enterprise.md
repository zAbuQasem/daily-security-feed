---
layout: post
title: "SVD-2026-0609: Improper Access Control in Splunk Enterprise"
date: 2026-06-10 00:00:00 +0300
categories: [RSS]
tags: [access-control, cve, splunk, privilege-escalation]
toc: true
---

CVE-2026-20259 is an improper access control vulnerability in Splunk Enterprise and Cloud Platform where users holding the high-privilege `edit_saved_search_owner` capability can reassign saved search ownership to users outside their authorized scope due to missing access control on the ownership reassignment endpoint. The vulnerability affects Enterprise versions 10.2.0–10.2.3 and 10.0.0–10.0.6, plus multiple Splunk Cloud Platform versions. With a CVSS score of 5.5 (Medium), successful exploitation requires existing high privileges but allows lateral privilege escalation and scope-boundary bypass. Patch versions 10.2.4, 10.0.7, and corresponding Cloud Platform updates are available.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0609){: .btn .btn-primary }
