---
layout: post
title: "You Assume Your Logs Are Flowing."
date: 2026-07-17 16:21:31 +0300
categories: [RSS]
tags: [detection, monitoring, azure-sentinel, logging, defense]
toc: true
---

Detection engineering article on identifying silent log pipeline failures in Azure Sentinel—a critical blind spot where data stops arriving but looks indistinguishable from a quiet, healthy environment. The piece addresses the migration from the deprecated HTTP Data Collector API to the Logs Ingestion API with Data Collection Rules (DCRs), where old health checks become ineffective. Provides practical KQL queries to detect failures at four points: source silence (machines that stopped heartbeating after weeks of consistent reporting), DCR transformation errors, pipeline latency, and data landing in wrong destinations. The key insight: you need health checks for your health checks—monitoring ingestion volume day-over-day and reliability patterns prevents detections from going blind when the pipeline fails.

[Read original article](https://detect.fyi/you-assume-your-logs-are-flowing-a6e8971b676c?source=rss----d5fd8f494f6a---4){: .btn .btn-primary }
