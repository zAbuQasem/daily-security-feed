---
layout: post
title: "Inside Agentic Offensive Frameworks: Intent IDs"
date: 2026-11-25 14:27:03 +0300
categories: [RSS]
tags: [cloud, ai-attack, detection, threat-intelligence]
toc: true
---

Agentic offensive frameworks like ARTEX and Cairn use sequential Intent ID counters (iNNNN) to track operations, and these identifiers are leaking into victim logs during cloud intrusions. By analyzing the counter mechanics in framework code, defenders can correlate multiple attacks from the same operator, pace analysis of attacker activity, and deconflict overlapping operations in high-volume automated attack scenarios. The research demonstrates how to extract signal from these leaks but also identifies where the detection methodology breaks down, highlighting the need for defense-in-depth approaches against machine-speed, agentic attacks.

[Read original article](https://www.wiz.io/blog/agentic-offensive-frameworks-intent-ids-artex-cairn){: .btn .btn-primary }
