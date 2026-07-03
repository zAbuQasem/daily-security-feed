---
layout: post
title: "It’s 37oC, And All We Can Think About Is ColdFusion (Adobe ColdFusion Security Bulletin APSB26-68 CVE Bonanza)"
date: 2026-07-02 16:38:28 +0300
categories: [RSS]
tags: [rce, coldfusion, cve, file-access]
toc: true
---

Adobe's APSB26-68 bulletin fixes 11 critical CVEs in ColdFusion 2025 and 2023, including multiple arbitrary code execution flaws. The core vulnerability chain exploits the RDS (Remote Development Services) module, which exposes a length-prefixed RPC protocol over HTTP at `/CFIDE/main/ide.cfm`. When RDS is enabled (non-default) and authentication disabled, attackers can send crafted RDS requests to read/write arbitrary files or execute code via the FileServlet, DbFuncsServlet, and AdminApiServlet command handlers. The RDS protocol itself is trivial to reverse—each request encodes fields as `[4-byte-pad][decimal-length]:[bytes]` enabling straightforward construction of malicious payloads. WatchTowr confirms exposure validation and remediation tooling is available to clients.

[Read original article](https://labs.watchtowr.com/its-37oc-and-all-we-can-think-about-is-coldfusion-adobe-coldfusion-security-bulletin-apsb26-68-cve-bonanza/){: .btn .btn-primary }
