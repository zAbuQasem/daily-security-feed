---
layout: post
title: "Introducing the Offsec ML Playbook v0.1"
source_url: https://5stars217.github.io/2023-10-26-introducing-offsec-ml-framework/
date: 2026-04-08
priority: 2
tags: [supply-chain, ml-security, adversarial-ml, llm, ttp, github-zabuqasem, linkedin-zeyad-abulaban]
feed: https://5stars217.github.io/feed.xml
---

The Offsec ML Playbook v0.1 is a structured wiki of offensive ML TTPs organized into three domains: supply chain attacks, offensive ML techniques, and adversarial ML. Supply chain coverage includes embedding malware in models via Keras Lambda layers, poisoning LLM ground truths through model registry access, and watering-hole attacks via public Hugging Face model repositories. Adversarial ML entries include prompt injection via repeated character sequences against LLM API endpoints. The offensive ML section covers ML-assisted flywheels (e.g., Nemesis), sandbox detection using process ratios, and Markov-chain-based obfuscation. Each TTP includes metadata such as transferability — whether the technique generalizes across other ML models — making this a practical decision-support tool for red teamers targeting ML infrastructure.
