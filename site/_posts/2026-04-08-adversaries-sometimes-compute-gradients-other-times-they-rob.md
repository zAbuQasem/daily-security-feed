---
layout: post
title: "Adversaries sometimes compute gradients. Other times, they rob you."
date: 2026-04-08 00:00:00 +0300
categories: [Research]
tags: [offensive-ml, evasion, red-team, phishing, malware]
toc: true
---

The article introduces the 'adversary flywheel' — a framework for red team operators to systematically collect attack telemetry and apply ML offensively, mirroring the data flywheel that defensive vendors use to improve detection models. The core technique involves using open-source defensive ML models (e.g., phishing webpage detectors, AV engines like Elastic's EMBER) adversarially: extracting feature importance to understand why payloads are flagged, then iteratively modifying them to survive ML-based detection layers. The author frames ML evasion as a natural extension of existing C2 evasion tradecraft (symbol obfuscation, polymorphic payloads), arguing attackers should address ML detection systematically alongside signature and static analysis bypasses. APT behavior is cited as evidence of the threat model — nation-state actors steal defensive ML systems outright rather than computing gradients, underscoring the value of this telemetry. Projects like Nemesis, RedELK, and red_team_telemetry are highlighted as building blocks for attacker-side data pipelines that enable evidence-driven offensive operations.

---

[Read original article](https://5stars217.github.io/2024-04-23-adversaries-sometimes-compute-gradients/)

> Source: `5stars217.github.io`
