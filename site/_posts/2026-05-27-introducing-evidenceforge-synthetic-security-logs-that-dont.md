---
layout: post
title: "Introducing EvidenceForge: Synthetic security logs that don’t look (as) fake"
date: 2026-05-27 10:00:47 +0300
categories: [RSS]
tags: [detection, threat-hunting, synthetic-data, blue-team, tooling]
toc: true
---

EvidenceForge is a new open-source tool from Cisco Talos that generates correlated synthetic security logs across 20+ formats (Windows Security Events, Sysmon, EDR/XDR, Zeek, Snort, Linux syslog, etc.) using a single canonical event model to ensure causal and temporal consistency across log sources. Unlike existing generators that emit events independently per format, EvidenceForge uses shared context objects (ProcessContext, NetworkContext, AuthContext, etc.) so cross-source artifacts like PIDs, LogonIDs, and Zeek UIDs are always consistent. A composable rule engine auto-inserts prerequisite events (e.g., Kerberos TGT before a domain logon, DNS resolution before a named-host connection) with realistic timing offsets. The tool also models sensor placement (SPAN/TAP, monitored segments) to simulate realistic network visibility gaps. Primary use cases are training threat hunters and detection engineers with ground-truth-labeled datasets, validating detection logic, and generating labeled training data for ML models.

[Read original article](https://blog.talosintelligence.com/introducing-evidenceforge-synthetic-security-logs-that-dont-look-as-fake/){: .btn .btn-primary }
