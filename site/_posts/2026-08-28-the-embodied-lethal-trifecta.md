---
layout: post
title: "The Embodied Lethal Trifecta"
date: 2026-08-28 04:00:00 +0300
categories: [RSS]
tags: [prompt-injection, embodied-ai, robotics, safety]
toc: true
---

The article introduces the Embodied Lethal Trifecta, a novel architectural vulnerability pattern in AI-controlled robots where prompt injection can cause physical harm. It occurs when a single compromised reasoning path can: (1) ingest untrusted semantic content (attacker-controlled text, visual inputs, commands), (2) exercise consequential physical authority (locomotion, manipulation, equipment control), and (3) disable or bypass independent safety controls (collision avoidance, speed/force limits, emergency stops). Unlike conventional prompt injection that exposes data or misuses services, embodied systems create a direct path from malicious input to physical harm. The article includes a worked example using extracted firmware from a Unitree Go2 robot, demonstrating how commercial embodied AI systems integrate visual perception with safety override capabilities, materializing this threat model.

[Read original article](https://5stars217.github.io/2026-08-28-the-embodied-lethal-trifecta/){: .btn .btn-primary }
