---
layout: post
title: "StyleSmuggler: Magento and Adobe Commerce 0-day RCE under active attack"
date: 2026-09-05 00:00:00 +0300
categories: [RSS]
tags: [0-day, rce, magento, active-exploit, template-injection]
toc: true
---

StyleSmuggler is an unpatched 0-day remote code execution vulnerability in Magento Open Source and Adobe Commerce affecting all current versions (2.4.7 through 2.4.9+) with active exploitation ongoing since September 4th, 2026. The attack leverages Magento's template system by poisoning PHP code through the `styles` properties to bypass existing safeguards, then triggers execution when Magento renders failed payment reminder emails—no user interaction required. Sansec reproduced the full unauthenticated chain on clean installations and identified indicators of compromise including background process impersonation, C2 communications over WebSocket and custom NTP-shaped traffic, and specific file paths in user home directories. Emergency mitigation via Sansec Shield is active; temporary workarounds include disabling GraphQL until Adobe releases a patch (scheduled September 8th). Detection involves checking for malicious crontab entries, suspicious background processes, and payment failure email bursts.

[Read original article](https://sansec.io/research/stylesmuggler){: .btn .btn-primary }
