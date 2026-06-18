---
layout: post
title: "Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 1: The Summary Rules Quest"
date: 2026-06-17 08:49:40 +0300
categories: [RSS]
tags: [siem, detection, logging, azure, cost-optimization]
toc: true
---

Microsoft Sentinel cost optimization guide using Summary Rules—scheduled KQL aggregation queries that pre-aggregate log data before storage. Summary Rules combined with cheaper storage tiers (Auxiliary, Data Lake) maintain detection capabilities while reducing ingestion costs by aggregating high-volume logs (e.g., 545 firewall events → 1 summarized event). The approach leverages Sentinel's multi-tier strategy (Analytics for hot data, Data Lake for cold storage) and split transformation rules to route data efficiently while preserving investigative power. Part 1 explains tier characteristics and rule mechanics; subsequent parts will cover implementation.

[Read original article](https://blog.nviso.eu/2026/06/17/reducing-microsoft-sentinel-costs-without-compromising-detection-part-1-the-summary-rules-quest/){: .btn .btn-primary }
