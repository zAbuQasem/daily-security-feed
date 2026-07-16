---
layout: post
title: "SVD-2026-0704: Sensitive Information Disclosure through the storage/passwords REST Endpoint in Splunk Enterprise"
date: 2026-07-15 00:00:00 +0300
categories: [RSS]
tags: [cve, splunk, information-disclosure, rest-api, credentials]
toc: true
---

CVE-2026-20298 is a sensitive information disclosure in Splunk Enterprise and Cloud Platform where low-privileged users without admin/power roles can extract encrypted credential hashes by accessing the `/servicesNS/-/-/storage/passwords` REST endpoint through the `|rest` SPL command. The vulnerability stems from the REST API returning the `encr_password` field in response data without proper field masking or access controls. Affects Enterprise versions below 10.4.1, 10.2.5, 10.0.8, 9.4.13 and multiple Cloud Platform branches; patched versions add a `mask_encr_password` configuration option in `limits.conf`. CVSS 5.3 (Medium) with high confidentiality impact requiring authentication.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0704){: .btn .btn-primary }
