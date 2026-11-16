---
layout: post
title: "How to check if your EC2 workloads are ready for IMDSv2"
date: 2026-11-16 00:00:00 +0300
categories: [RSS]
tags: [cloud, aws, iam, ssrf, detection]
toc: true
---

IMDSv2 (Instance Metadata Service Version 2) requires session tokens for EC2 metadata access, mitigating SSRF attacks that could steal instance IAM credentials—but legacy workloads still using IMDSv1 lose access when enforcement is enabled. The article covers identifying instances and processes making IMDSv1 requests via CloudWatch metrics (MetadataNoToken, MetadataNoTokenRejected) and Datadog monitoring, then testing enforcement on small instance groups before fleet-wide deployment. Datadog's real-world migration experience shows how to use metrics and workload protection to trace requests to individual containers/processes and coordinate fixes with service owners before requiring IMDSv2.

[Read original article](https://www.datadoghq.com/blog/check-ec2-workloads-imdsv2-readiness/){: .btn .btn-primary }
