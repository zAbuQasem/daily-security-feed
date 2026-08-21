---
layout: post
title: "UAT-10147: Chinese-speaking adversary integrates agentic AI into post-compromise operations"
date: 2026-08-20 10:00:32 +0300
categories: [RSS]
tags: [malware, post-compromise, ai-assisted, threat-intelligence, evasion]
toc: true
---

Cisco Talos identified UAT-10147, a Chinese-speaking cybercrime group, deploying agentic AI systems to orchestrate complex post-compromise operations against 170,000+ web servers globally in government, education, media, technology, and gaming sectors. The actor uses AI-generated exploitation guidance, payload generation, and troubleshooting workflows to automate attack chains at scale, representing a transition from simple AI-assisted scripting to semi-autonomous offensive orchestration. Initial access leverages publicly disclosed web server vulnerabilities to achieve RCE; post-compromise tactics employ multi-stage batch scripts deploying QuasarRAT and SPECTRE implants via privilege escalation tools like EfsPotato, with Windows Defender evasion via registry modifications and IIS directory exclusions. This research demonstrates how AI-driven tooling reduces expertise barriers and enables threat actors to efficiently scale sophisticated intrusions while maintaining operational resilience through automated validation and troubleshooting workflows.

[Read original article](https://blog.talosintelligence.com/uat-10147-chinese-speaking-adversary-integrates-agentic-ai-into-post-compromise-operations/){: .btn .btn-primary }
