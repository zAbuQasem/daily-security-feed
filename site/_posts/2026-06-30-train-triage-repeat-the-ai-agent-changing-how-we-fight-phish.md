---
layout: post
title: "Train, triage, repeat: The AI agent changing how we fight phishing"
date: 2026-06-30 12:33:22 +0300
categories: [RSS]
tags: [detection, phishing, ai, ml, automation]
toc: true
---

Red Canary describes a multi-agent phishing triage system achieving 94% accuracy through orchestrated subagents: email parsing/enrichment, hybrid feature extraction combining traditional rules with NLP-powered sentiment/intent analysis, a deterministic rules engine, and hybrid AI/ML classification. The rules engine pairs atomic email metadata with extracted features to detect TTP patterns and emerging campaigns, while a reasoning subagent generates final classifications with full explainability. Critically, the ML model trains only on true/false feature values—never raw email content—then adds feature importance weights to guide AI decision-making, maintaining transparency. Analyst-driven feedback loops continuously refine detection logic while automation handles bulk triage, enabling human expertise to focus on nuanced phishing variants at 3.8M+ annual attack volumes.

[Read original article](https://redcanary.com/blog/threat-detection/phishing-ai-agent/){: .btn .btn-primary }
