---
layout: post
title: "Prioritize security findings with Datadog Crown Jewels"
date: 2026-11-27 00:00:00 +0300
categories: [RSS]
tags: [cloud-security, detection, tooling, finding-prioritization]
toc: true
---

Datadog Crown Jewels automatically identifies critical cloud resources by analyzing observability telemetry to detect services processing sensitive data, sensitive database columns, storage buckets containing sensitive information, and high-dependency services. The feature uses rule-based detection on APM spans, logs, sensitive data scanners, and service maps to build an inventory of business-critical assets, which is then used to prioritize security findings and reduce remediation queues. Teams can review detection evidence and customize the inventory through rule tuning, manual additions, or rule disabling to match their organization's definition of criticality. Findings associated with critical resources receive a `@risk.is_crown_jewel:true` tag for filtering and routing based on business impact rather than severity alone.

[Read original article](https://www.datadoghq.com/blog/prioritize-security-findings-crown-jewels/){: .btn .btn-primary }
