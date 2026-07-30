---
layout: post
title: "From your doorbell to your home network"
date: 2026-07-28 00:00:00 +0300
categories: [RSS]
tags: [iot, hardware, wifi, reverse-engineering, network]
toc: true
---

A detailed reverse engineering of the Eufy Security Video Doorbell ecosystem, demonstrating multiple attack vectors including WiFi deauth jamming to disable video streaming and interrupt device connectivity. The Homebase Station 2 hub creates a hidden WPA2 network named OCEAN_XXXXXX (last 24 bits derived from MAC prefix 90:bf:d9) that can be discovered via probe requests and flooded with deauth packets using commodity tools (Raspberry Pi + Alfa antenna). Successfully jamming the WiFi allows physical access to devices while disabling remote monitoring, and gaining network access to the hidden OCEAN network grants access to the entire home network including router interfaces. The article references prior 2023 USENIX research on Eufy PSK entropy and expands the attack surface with practical exploitation tooling and threat modeling.

[Read original article](https://adepts.of0x.cc/Eufy-DoorBell-hacking/){: .btn .btn-primary }
