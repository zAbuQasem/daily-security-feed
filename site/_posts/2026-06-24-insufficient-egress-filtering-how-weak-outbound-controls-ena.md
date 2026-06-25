---
layout: post
title: "Insufficient Egress Filtering: How Weak Outbound Controls Enable Attacks"
date: 2026-06-24 14:00:00 +0300
categories: [RSS]
tags: [egress-filtering, c2, blue-team, network-controls, ssh]
toc: true
---

This article examines insufficient egress filtering as a common vulnerability that enables command and control (C2) communication, credential theft, and lateral movement. It outlines a methodical approach to implementing egress controls: profile legitimate outbound connections, establish a default-deny posture, and iteratively authorize specific destination IPs and ports. The article provides practical attack techniques that exploit weak egress filtering, including SSH remote port forwarding for reverse tunnels, ICMP and DNS tunneling for covert communication, and proxychains/proxifier for tool execution through compromised hosts. It also includes testing utilities (letmeoutofyour.net, outbound port scans) to identify open egress paths, making this a valuable reference for both penetration testers and defenders implementing perimeter controls.

[Read original article](https://www.blackhillsinfosec.com/insufficient-egress-filtering/){: .btn .btn-primary }
