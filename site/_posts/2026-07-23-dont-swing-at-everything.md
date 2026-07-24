---
layout: post
title: "Don’t swing at everything"
date: 2026-07-23 18:00:46 +0300
categories: [RSS]
tags: [malware, threat-intel, c2, evasion, detection]
toc: true
---

Cisco Talos intelligence digest covering Q2 2026 CVE trends (49% YoY growth, ~200 CVEs/day) with analysis showing EPSS scoring is more effective than CVSS for prioritization—95% of CVSS 9+ CVEs have <5% real-world exploit probability. Primary focus: msaRAT, a Rust-based RAT deployed by Chaos ransomware group that establishes covert C2 channels by hijacking Chrome/Edge browsers via Chrome DevTools Protocol, bypassing network detection through living-off-browser techniques. Malware delivered via MSI files impersonating Windows updates, loaded directly into memory, and uses Tokio async runtime for efficient parallel execution. Detection guidance includes monitoring for unusual curl commands to ProgramData, MSI file masquerading, and unauthorized CDP protocol activity.

[Read original article](https://blog.talosintelligence.com/dont-swing-at-everything/){: .btn .btn-primary }
