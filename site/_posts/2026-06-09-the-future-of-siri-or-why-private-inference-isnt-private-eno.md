---
layout: post
title: "The future of Siri, or: why private inference isn’t private enough"
date: 2026-06-09 19:00:02 +0300
categories: [RSS]
tags: [cloud, privacy, architecture, ai-agent]
toc: true
---

Matthew Green analyzes Apple's integration of AI-enhanced Siri using Google Gemini via Private Cloud Compute (PCC), which encrypts inference end-to-end on Apple silicon and Google's confidential compute hardware, preventing both Apple and Google from accessing raw data. The article identifies a fundamental architectural tension: while PCC protects inference-only operations (reading contacts, calendars, messages locally), agentic AI requires external access—to search engines, calendar services, messaging APIs—creating new data exposure vectors. Green argues that true utility in personal AI agents (scheduling, booking, notifications) necessitates unrestricted access to sensitive private data, and the perimeter protection of PCC may be insufficient once agents begin orchestrating external service calls. The piece raises critical infrastructure security questions about how privacy-preserving inference scales to real-world agentic workflows.

[Read original article](https://blog.cryptographyengineering.com/2026/06/09/apples-siri-ai-or-more-shouting-into-the-void-about-private-agents/){: .btn .btn-primary }
