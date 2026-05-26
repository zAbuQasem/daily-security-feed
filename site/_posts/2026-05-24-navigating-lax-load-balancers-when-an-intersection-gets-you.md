---
layout: post
title: "Navigating Lax Load Balancers: When an Intersection Gets You Inside"
date: 2026-05-24 22:00:00 +0300
categories: [RSS]
tags: [cloud, aws, load-balancer, auth-bypass, misconfiguration]
toc: true
---

This Doyensec post analyzes AWS Application Load Balancer (ALB) misconfigurations that create unintended access paths. Three concrete bug classes are detailed: (1) CloudFront/WAF bypass when the origin ALB remains internet-facing with an open security group; (2) rule shadowing where a broad low-priority-number rule (e.g., `path /*` at priority 10) matches before a more restrictive auth rule at higher priority, causing the `authenticate-oidc` action to never fire; (3) IP gate bypass when the same target group or EC2 instances are registered in a second ALB or listener without the `source-ip` condition. The key insight is that CSPM tools check attribute hygiene (TLS, logging, WAF attachment) but cannot trace whether a given backend endpoint is actually protected end-to-end across all routing paths. The post provides an auditor checklist covering rule ordering analysis, XFF trust, and multi-path target group enumeration.

[Read original article](https://blog.doyensec.com/2026/05/25/cloudsectidbits-elbaph-alb.html){: .btn .btn-primary }
