---
layout: post
title: "SVD-2026-0613: Insecure Default Domain Allowlist in Splunk AI Toolkit"
date: 2026-06-17 00:00:00 +0300
categories: [RSS]
tags: [cve, splunk, data-exfiltration, configuration]
toc: true
---

Splunk AI Toolkit versions below 5.7.4 contain an insecure default domain allowlist that allows low-privileged users to trigger outbound HTTP requests to attacker-controlled servers, enabling data exfiltration. The vulnerability (CWE-1188) stems from the toolkit failing to restrict AI agent requests to approved external domains when the default configuration is used. Mitigation requires explicitly configuring `allowed_domains` in `local/mlspl.conf` and enabling `enforce_domain_validation=true`, or disabling the toolkit entirely. The fix is available in version 5.7.4 and later.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0613){: .btn .btn-primary }
