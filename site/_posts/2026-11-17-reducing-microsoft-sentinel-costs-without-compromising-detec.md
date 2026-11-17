---
layout: post
title: "Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 3: The DNS Quest"
date: 2026-11-17 13:25:03 +0300
categories: [RSS]
tags: [dns, detection, c2, cloud, threat-hunting]
toc: true
---

This article demonstrates detecting DNS tunneling attacks (a DNS-based C2 and data exfiltration technique) within Microsoft Sentinel while optimizing ingestion costs. The technique leverages base32-encoded subdomains to bypass network restrictions, exemplified by tools like Sliver C2. The article provides a practical PowerShell proof-of-concept and shows how to use Sentinel's Summary Rules to aggregate DNS events in the Data Lake, identify suspicious patterns in Microsoft DNS Analytical events, and trigger alerts on anomalous DNS behavior without full log ingestion. By filtering high-volume DNS telemetry through intelligent aggregation rules, organizations maintain detection capabilities for DNS-based threats while reducing per-event costs.

[Read original article](https://blog.nviso.eu/2026/11/17/reducing-microsoft-sentinel-costs-without-compromising-detection-part-3-the-dns-quest/){: .btn .btn-primary }
