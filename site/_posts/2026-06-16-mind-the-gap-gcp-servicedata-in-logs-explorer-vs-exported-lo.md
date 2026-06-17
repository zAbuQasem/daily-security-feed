---
layout: post
title: "Mind the Gap: GCP serviceData in Logs Explorer vs. Exported Logs"
date: 2026-06-16 12:46:59 +0300
categories: [RSS]
tags: [cloud, gcp, detection, audit-logging]
toc: true
---

GCP's `serviceData` field in audit logs exhibits an undocumented inconsistency: the same log entry appears fully populated in GCP Logs Explorer but stripped of critical sub-properties (like `policyDelta`) when exported to downstream analytics platforms. The behavior is unpredictable—identical `SetIamPolicy` events on the same service sometimes retain `serviceData` and sometimes don't—yet detection rules for critical events like disabling audit logging (`action: REMOVE`, `service: allServices`) depend entirely on this field. This creates a blind spot in downstream detection pipelines where an attacker disabling audit logging would go undetected in analytics platforms, even though the same event would alert in Logs Explorer. Permiso's investigation reveals the field is still actively used despite deprecation claims, with the official service list actually expanding rather than contracting over time.

[Read original article](https://permiso.io/blog/gcp-servicedata-officially-deprecated-actively-dangerous){: .btn .btn-primary }
