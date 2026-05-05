---
layout: post
title: "Evaluating our Threat Hunting Detection Rules (+ KQL Query Evaluation)"
date: 2026-05-04 09:26:32 +0300
categories: [RSS]
tags: [detection-engineering, threat-hunting, kql, microsoft-defender, siem]
toc: true
---

The article proposes a practical framework, DOVE (Detection Overlap & Value Evaluation), for reviewing whether custom threat-hunting and SIEM detections still add value or have become duplicate alert noise. It evaluates rules across detection type (IOC vs. IOA), platform coverage, threat recency, and provider/source, then applies that model with a KQL query that joins AlertInfo and AlertEvidence, bins alerts by hour, and groups on entities such as AccountUpn, DeviceName, RemoteIP, RemoteUrl, EmailSubject, and Application to spot multiple detections firing on the same activity. The query specifically highlights cases where more than one detection source is present and one is a custom rule, making it useful for finding overlap between custom detections and native Microsoft Defender/Sentinel analytics. The examples show three concrete outcomes: custom detections that enrich an EDR incident, rules that help reconstruct the full phishing or malicious-URL chain, and redundant detections that duplicate built-in coverage such as AAD Identity Protection and should likely be retired.

[Read original article](https://detect.fyi/evaluating-our-threat-hunting-detection-rules-kql-query-evaluation-5e8b6a77f2a2?source=rss----d5fd8f494f6a---4){: .btn .btn-primary }
