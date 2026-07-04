---
layout: post
title: "The Blind Spot in the Watchtower: Detections for When Someone Attacks Your Sentinel"
date: 2026-07-03 08:16:23 +0300
categories: [RSS]
tags: [detection, threat-hunting, azure, siem, blue-team]
toc: true
---

Detectify publishes practical KQL detection queries for identifying attacker tampering with Microsoft Sentinel SIEM controls. The article covers detection engineering for four attack patterns: disabling/deleting analytic rules, reducing log retention or removing tables, disabling data connectors/collection rules, and granting unauthorized admin roles. Provides ready-to-run queries leveraging AzureActivity, SentinelAudit, and SentinelHealth logs, emphasizing the importance of SIEM self-monitoring since attackers typically disable detection rules before executing their actual attack. Includes watchlist-based filtering to reduce false positives from legitimate admin activity.

[Read original article](https://detect.fyi/the-blind-spot-in-the-watchtower-detections-for-when-someone-attacks-your-sentinel-897709f0dcd9?source=rss----d5fd8f494f6a---4){: .btn .btn-primary }
