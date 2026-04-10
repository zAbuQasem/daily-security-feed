---
layout: post
title: "Edge Decay: How a Failing Perimeter Is Fueling Modern Intrusions"
date: 2026-04-10 03:12:58 +0300
categories: [RSS]
tags: [edge-devices, threat-intel, firmware, lateral-movement, vpn]
toc: true
---

SentinelOne analyzes a pattern they call 'edge decay' — the systematic exploitation of perimeter devices (firewalls, VPN concentrators, load balancers) as primary intrusion vectors. Key mechanisms include: compromised F5 BIG-IP devices pivoting directly into VMware vSphere environments, Check Point gateway CVEs used for initial access at scale, and the ArcaneDoor campaign chaining Cisco ASA zero-days to deploy RayInitiator (a firmware-level bootkit that survives reboots) alongside LINE VIPER (an in-memory payload suppressing logs and capturing auth traffic). State-sponsored actors are also building Operational Relay Box (ORB) networks from hijacked edge devices — clusters like PurpleHaze and groups like APT15/Hafnium use these to route attack traffic through legitimate infrastructure, complicating attribution. The core defensive gap is that most edge appliances cannot run EDR agents, have inconsistent logging, and slow patch cycles — making them structurally invisible to modern detection stacks.

---

[Read original article](https://www.sentinelone.com/blog/edge-decay-how-a-failing-perimeter-is-fueling-modern-intrusions/){: .btn .btn-primary }
