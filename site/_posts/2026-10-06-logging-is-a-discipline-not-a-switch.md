---
layout: post
title: "Logging is a Discipline, Not a Switch"
date: 2026-10-06 04:00:00 +0300
categories: [RSS]
tags: [active-directory, detection, logging, auditing]
toc: true
---

TrustedSec provides a structured approach to implementing comprehensive logging in Active Directory environments by treating logging as a discipline rather than a one-time configuration. The methodology covers four sequential steps: sizing event logs appropriately (192MB for Security logs, 32MB for Application/Setup/System), enabling Advanced Audit Policy subcategories through Group Policy, defining detection use cases, and testing detection capabilities. The article reconciles TrustedSec and CIS Benchmark recommendations for audit subcategories including Credential Validation, Kerberos Authentication Service, account management, and detailed tracking, noting that neither standard alone provides full coverage. The approach emphasizes balancing log volume against retention windows to ensure detection data isn't overwritten before collection systems can ingest it, particularly accounting for collector maintenance windows. This guidance is essential for organizations looking to improve their ability to detect AD-based intrusions and lateral movement.

[Read original article](https://trustedsec.com/blog/logging-is-a-discipline-not-a-switch){: .btn .btn-primary }
