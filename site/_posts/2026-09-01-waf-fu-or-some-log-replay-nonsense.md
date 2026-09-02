---
layout: post
title: "waf-fu, or Some Log Replay Nonsense"
date: 2026-09-01 04:00:00 +0300
categories: [RSS]
tags: [aws, cloud, iam, credential-exposure, log-analysis]
toc: true
---

AWS WAF logs capture all HTTP request metadata including headers, query parameters, URIs, and client IPs without automatic redaction — exposing Authorization, Cookie, X-API-Key, and session tokens by default, even though redaction best practices exist outside main AWS documentation. The article demonstrates three IAM-permissive paths to extract these logs: CloudWatch Logs Groups (logs:DescribeLogGroups, logs:FilterLogEvents), S3 buckets (s3:ListAllMyBuckets, s3:ListBucket, s3:GetObject), and WAF direct sampling via wafv2 actions (which bypass RedactedFields configuration). The authors release waf-fu, a tool that automates WAF log extraction and replay at scale to hunt for credential access and privilege escalation. This highlights a significant information disclosure risk in misconfigured AWS deployments where overly-permissive IAM principals can directly exfiltrate sensitive authentication data from firewall logs.

[Read original article](https://trustedsec.com/blog/waf-fu-or-some-log-replay-nonsense){: .btn .btn-primary }
