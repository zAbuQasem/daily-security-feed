---
layout: post
title: "Bluetooth Relaying Attacks"
date: 2026-07-14 05:00:00 +0300
categories: [RSS]
tags: [bluetooth, relay-attack, iot, physical-security, proximity]
toc: true
---

Bluetooth relay attacks exploit the absence of strict physical proximity verification in keyless lock systems. An attacker positions two Bluetooth devices in a machine-in-the-middle position to intercept and forward signals between a victim's phone and lock in real-time, tricking both into believing they're in range when they may be kilometers apart. The article demonstrates a practical proof-of-concept on a bike lock using standard hardware (Bluetooth dongles, WHAD tool) and explains why this works: most lock manufacturers disable Bluetooth bonding to enable multi-device sharing, allowing device impersonation. Mitigation requires either disabling automatic proximity-based unlocking in favor of manual confirmation, or implementing latency measurements or UWB-based distance verification—though some circumventions of latency-based defenses have been reported.

[Read original article](https://blog.syss.com/posts/bluetooth-realying/){: .btn .btn-primary }
