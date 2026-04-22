---
layout: post
title: "Bad Apples: Weaponizing native macOS primitives for movement and execution"
date: 2026-04-22 03:12:37 +0300
categories: [RSS]
tags: [macos, lateral-movement, applescript, lotl, defense-evasion]
toc: true
---

Cisco Talos maps out macOS-native living-off-the-land techniques for execution, lateral movement, and payload staging, focusing on primitives that operate outside the SSH-centric telemetry many defenders rely on. The core technique abuses Remote Application Scripting over the eppc:// Apple Events channel: instead of failing through System Events with the -10016 handler restriction, the operator drives Terminal.app as an execution proxy, sending Base64-encoded payloads that are decoded to a temporary file, chmodded, and then launched via bash in a second stage. The research also shows how Apple Events can be used for remote reconnaissance such as querying Finder for mounted volumes, and highlights Spotlight metadata/Finder comments as a stealthy place to stage payload data that may evade static file scanning. The practical value is in showing that legitimate macOS administration features and binaries can provide remote orchestration, movement, and persistence paths with limited visibility unless defenders monitor AppleEvents IPC, process lineage, and tightly restrict services through MDM.

[Read original article](https://blog.talosintelligence.com/bad-apples-weaponizing-native-macos-primitives-for-movement-and-execution/){: .btn .btn-primary }
