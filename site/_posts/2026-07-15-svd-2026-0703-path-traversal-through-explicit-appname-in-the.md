---
layout: post
title: "SVD-2026-0703: Path Traversal through 'explicit_appname' in the App Install REST Endpoint in Splunk Enterprise"
date: 2026-07-15 00:00:00 +0300
categories: [RSS]
tags: [path-traversal, splunk, cve, file-write]
toc: true
---

A path traversal vulnerability (CVE-2026-20297) in Splunk Enterprise and Cloud Platform's app installation REST endpoint allows authenticated users with edit_local_apps and install_apps capabilities to write files outside the intended app directory, directly into $SPLUNK_HOME/etc/ and its subdirectories. The vulnerability exists because the app installation workflow fails to restrict installation paths, enabling privilege escalation through arbitrary file write. Affects Splunk Enterprise versions before 10.4.1, 10.2.5, 10.0.8, 9.4.13, and 9.3.14; fixes are available.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0703){: .btn .btn-primary }
