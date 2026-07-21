---
layout: post
title: "Defender's Remote Connections Blind Spot: FourToSixMapping"
date: 2026-07-20 11:27:04 +0300
categories: [RSS]
tags: [detection-engineering, microsoft-defender, threat-hunting, false-negatives, kql]
toc: true
---

Microsoft Defender XDR's DeviceNetworkEvents table logs external IPv4 connections via dual-stack sockets as 'FourToSixMapping' (IPv6-mapped format ::ffff:x.x.x.x) rather than 'Public', causing detection queries that filter on RemoteIPType == 'Public' to silently miss C2 and exfiltration traffic. The article demonstrates how standard KQL constructs like ipv4_is_private() return null for FourToSixMapping values, creating false negatives, and provides a normalization fix: either strip the ::ffff: prefix before filtering or explicitly include FourToSixMapping in RemoteIPType constraints. This is a practical detection gap affecting large-scale Defender deployments.

[Read original article](https://detect.fyi/defenders-remote-connections-blind-spot-fourtosixmapping-ce3f19658d05?source=rss----d5fd8f494f6a---4){: .btn .btn-primary }
