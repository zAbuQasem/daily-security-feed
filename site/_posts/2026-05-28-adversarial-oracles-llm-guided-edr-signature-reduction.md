---
layout: post
title: "Adversarial Oracles: LLM-Guided EDR Signature Reduction"
date: 2026-05-28 17:51:55 +0300
categories: [RSS]
tags: [evasion, malware, llm, edr, red-team]
toc: true
---

Praetorian demonstrates using a Claude-based agentic workflow with VirusTotal as a feedback oracle to iteratively reduce EDR/AV detections on Go offensive tooling (specifically goffloader). The technique treats VirusTotal's detection count as a TDD-style pass/fail signal, allowing the LLM to propose and validate source-level changes without human-in-the-loop iteration. Key findings include that naive approaches (symbol stripping via -trimpath/-ldflags, garble obfuscation) can increase detections due to structural anomalies triggering ML-based heuristics. The skill targets Go-specific signatures (package import strings, reflection metadata) and guards against LLM hallucination by requiring VirusTotal confirmation before accepting a change. A working Claude skill is released at github.com/praetorian-inc/reduce-golang-detections-skill.

[Read original article](https://www.praetorian.com/blog/llm-edr-signature-reduction/){: .btn .btn-primary }
