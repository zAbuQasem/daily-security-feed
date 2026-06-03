---
layout: post
title: "A deep dive into surfacing and fixing gaps in AWS data perimeter policies"
date: 2026-06-01 00:00:00 +0300
categories: [RSS]
tags: [aws, cloud, iam, defense-evasion, detection]
toc: true
---

This article examines AWS data perimeter implementation gaps and mitigation strategies using organization-level controls. It demonstrates how resource-level policies (bucket policies, IAM policies) create security gaps that attackers can exploit, then shows how Service Control Policies (SCPs) and Resource Control Policies (RCPs) enforce identity, network, and resource perimeters across entire AWS organizations. The research uses Stratus Red Team to simulate attacks like CloudTrail deletion (`cloudtrail:DeleteTrail`, `cloudtrail:StopLogging`) and validates defense-in-depth controls. Datadog's 2025 report found only 0.6% of organizations use recommended organization-level solutions despite 40% implementing data perimeters. The article provides concrete SCP examples denying CloudTrail modifications with conditional exceptions for privileged roles, and emphasizes that SCPs don't protect management accounts—a critical security consideration for AWS Organizations.

[Read original article](https://www.datadoghq.com/blog/aws-data-perimeters/){: .btn .btn-primary }
