---
layout: post
title: "Dirty Cert: Cisco Smart Software Manager's Silently Patched RCE"
date: 2026-09-24 00:00:00 +0300
categories: [RSS]
tags: [rce, command-injection, cisco, nginx, enterprise]
toc: true
---

Cisco Smart Software Manager contained a post-authentication RCE vulnerability in its nginx certificate upload mechanism, where unsafe `childProcess.execSync()` calls in Node.js allowed command injection via TLS certificates. Attackers exploited RFC 7468's allowance for explanatory text before PEM headers to inject shell commands into intermediate certificate metadata, which persisted through backend processing and executed during certificate validation. The attack chain involved generating a CSR, crafting a malicious intermediate certificate with a command-injection payload in its explanatory text (e.g., `$(<COMMAND>)` before BEGIN CERTIFICATE), and uploading via `/backend/settings/csr/upload`. The vulnerability was silently patched in version 10-202608 (August 10, 2026), one week before disclosure.

[Read original article](https://starlabs.sg/blog/2026/09-dirty-cert-cisco-smart-software-managers-silently-patched-rce/){: .btn .btn-primary }
