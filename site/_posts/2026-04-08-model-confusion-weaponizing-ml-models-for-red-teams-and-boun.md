---
layout: post
title: "Model Confusion - Weaponizing ML models for red teams and bounty hunters"
source_url: https://5stars217.github.io/2023-08-08-red-teaming-with-ml-models/
date: 2026-04-08
priority: 1
tags: [supply-chain, ml-security, malware, hugging-face, red-team, github-zabuqasem, linkedin-zeyad-abulaban]
feed: https://5stars217.github.io/feed.xml
---

This DEFCON31 talk write-up details supply chain attack techniques targeting ML pipelines via Hugging Face, analogous to Alex Birsan's dependency confusion but applied to ML models. Three primary vectors are covered: Model Confusion (publishing malicious models under names that shadow legitimate ones), Organization Confusion (tricking engineers into joining attacker-controlled orgs to gain read/write on their repositories), and typosquatting/watering holes. The post includes a PoC for injecting C2 implants directly into Keras/TensorFlow model architectures (leveraging pickle deserialization and protobuf formats), and notes that ML environments are high-value targets because they run with privileged access to sensitive training data, lack mature supply chain tooling (no Snyk/Artifactory equivalent), and have low detection probability. Detection evasion is compounded by the large binary format of model files making VirusTotal and static analysis difficult.
