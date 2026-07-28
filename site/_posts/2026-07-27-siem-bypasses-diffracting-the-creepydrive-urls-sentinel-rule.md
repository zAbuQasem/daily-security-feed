---
layout: post
title: "SIEM Bypasses: Diffracting the “CreepyDrive URLs” Sentinel Rule"
date: 2026-07-27 08:59:00 +0300
categories: [RSS]
tags: [detection, siem, evasion, microsoft-sentinel, defense]
toc: true
---

Deep analysis of logic bugs in Microsoft's Sentinel rule for detecting POLONIUM's CreepyDrive OneDrive-based C2. Using Adversarial Detection Engineering methodology, the post systematically identifies six evasion paths: case-sensitive regex patterns can be bypassed with lowercase folder names (graph.microsoft.com/v1.0/me/drive/root:/uploaded/...), URL percent-encoding evades pattern matching, all path components (Documents, Uploaded, Downloaded, data.txt, response.json) are threat-actor-configurable making the rule easily evadable, alternative Graph API addressing schemes (item-ID direct access, children enumeration, special folders) bypass the root:/.../content pattern entirely, hardcoded API version /v1.0/ misses beta endpoints, and structural gaps underlie the entire approach. Includes concrete bypass examples and remediation guidance for detection engineers building behavioral rules for SaaS-based C2.

[Read original article](https://detect.fyi/siem-bypasses-diffracting-the-creepydrive-urls-sentinel-rule-82e066b00f8c?source=rss----d5fd8f494f6a---4){: .btn .btn-primary }
