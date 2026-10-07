---
layout: post
title: "How to fix a bug in a fix"
date: 2026-10-06 07:00:00 +0300
categories: [RSS]
tags: [patch-management, supply-chain, infrastructure, defense]
toc: true
---

Google Project Zero dissects emergency patching strategies used by major vendors to bypass normal patch delivery delays when remediating critical vulnerabilities. The core challenge is the testing–speed tradeoff: rigorous testing prevents data corruption and device bricking, but slows delivery; emergency patches compress this timeline to hours or days. The article details two proven approaches: (1) feature flags—remote-controlled conditional code paths that allow instant disable of vulnerable features (e.g., Apple's 2019 FaceTime disable) without shipping untested code; and (2) dual-stack libraries—compiling multiple versions of the same library (or different implementations) into one binary with runtime switchability via flags, enabling rapid version rollback if functional issues emerge. This post provides a reference architecture for vendors designing or enhancing emergency response infrastructure, bridging the gap between security urgency and deployment safety.

[Read original article](https://projectzero.google/2026/10/emergency-patching.html){: .btn .btn-primary }
