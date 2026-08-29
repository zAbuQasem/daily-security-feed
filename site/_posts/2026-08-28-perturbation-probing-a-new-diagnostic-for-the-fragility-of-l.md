---
layout: post
title: "Perturbation Probing: A New Diagnostic for the Fragility of LLM Safety"
date: 2026-08-28 22:00:07 +0300
categories: [RSS]
tags: [llm-security, mechanistic-interpretability, ai-safety, adversarial-robustness, model-evaluation]
toc: true
---

Researchers from Palo Alto Networks Unit 42 introduce perturbation probing, a low-cost mechanistic interpretability technique that identifies the specific feed-forward neurons responsible for LLM safety behavior. Testing on open-source models reveals a critical fragility: just 50 neurons out of 350,208 (0.014%) in Qwen3-4B control the safety refusal template, and removing them circumvents safety on 80% of harmful-prompt benchmarks. They developed the FFN/Skip ratio, a quantitative metric that predicts safety fragility across models with 81% accuracy, enabling pre-deployment diagnostics. The finding demonstrates that current LLM alignment is not a thick, distributed defense but a thin layer—vulnerable to both adversarial attacks and normal optimization—requiring external content filters and runtime guardrails for true defense-in-depth. The research provides both diagnostic tooling to measure safety robustness and a path to repair fragile models through targeted neuron amplification.

[Read original article](https://unit42.paloaltonetworks.com/perturbation-probing-llm-safety/){: .btn .btn-primary }
