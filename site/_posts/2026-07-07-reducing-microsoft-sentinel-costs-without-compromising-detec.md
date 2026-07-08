---
layout: post
title: "Reducing Microsoft Sentinel Costs Without Compromising Detection – Part 2: The Firewall Quest"
date: 2026-07-07 09:00:41 +0300
categories: [RSS]
tags: [detection, cloud, network, siem, incident-response]
toc: true
---

NVISO details a cost-optimization technique for Microsoft Sentinel using Summary Rules to reduce firewall log ingestion expenses without sacrificing detection capability. Firewall traffic logs typically contribute the largest ingestion costs (~$8,500/month for 50GB/day at $5.59/GB in West Europe pricing). The article demonstrates detection of network scanning activity by parsing Windows Filtering Platform events (EID 5156 for permitted, 5157 for blocked connections) using KQL to identify vertical and horizontal scanning patterns—where an endpoint attempts connections to sequential ports or multiple hosts in short timeframes. Summary Rules aggregate raw traffic events into higher-level observations, reducing data volume while preserving detectable threat indicators for reconnaissance, malware C2 communication, and lateral movement analysis.

[Read original article](https://blog.nviso.eu/2026/07/07/reducing-microsoft-sentinel-costs-without-compromising-detection-part-2-the-firewall-quest/){: .btn .btn-primary }
