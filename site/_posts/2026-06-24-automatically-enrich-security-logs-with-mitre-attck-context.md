---
layout: post
title: "Automatically enrich security logs with MITRE ATT&CK context before they reach your SIEM"
date: 2026-06-24 00:00:00 +0300
categories: [RSS]
tags: [detection, mitre, logging, siem]
toc: true
---

Datadog's Observability Pipelines now includes preconfigured MITRE ATT&CK Enrichment Packs that automatically map vendor-specific security events (Okta, Palo Alto, FortiGate, AWS WAF, CloudTrail, Windows) to MITRE tactics and techniques before logs reach the SIEM. The enrichment normalizes heterogeneous log formats into a common framework, enabling detection rules and dashboards to operate on unified fields like @mitre.tactic rather than vendor-specific event schemas, reducing investigation overhead and enabling cross-source correlation without manual translation.

[Read original article](https://www.datadoghq.com/blog/mitre-attack-enrichment-packs-observability-pipelines/){: .btn .btn-primary }
