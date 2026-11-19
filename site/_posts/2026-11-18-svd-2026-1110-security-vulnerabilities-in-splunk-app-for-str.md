---
layout: post
title: "SVD-2026-1110: Security Vulnerabilities in Splunk App for Stream - November 2026"
date: 2026-11-18 00:00:00 +0300
categories: [RSS]
tags: [xxe, splunk, info-disclosure, authz-bypass, cve]
toc: true
---

Splunk released a security advisory (SVD-2026-1110) addressing three vulnerabilities in Splunk App for Stream below version 8.1.7. CVE-2026-131299 (CVSS 7.5) is an XML External Entity (XXE) injection in the vocabulary upload REST API endpoint that allows unauthenticated attackers to read local files or send outbound requests by uploading malicious XML due to missing external entity resolution policy. CVE-2026-131300 (CVSS 6.5) enables authenticated users to recover the Stream forwarder authentication key from splunkd_access.log, allowing impersonation of trusted forwarders. CVE-2026-131301 (CVSS 5.3) is a missing authorization check permitting unauthenticated users to reset the in-memory indexer cache. Mitigation requires upgrading to version 8.1.7 or higher.

[Read original article](https://advisory.splunk.com/advisories/SVD-2026-1110){: .btn .btn-primary }
