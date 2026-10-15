---
layout: post
title: "Critical Vulnerabilities Discovered in Google Chrome and Arm GPU Drivers"
date: 2026-10-14 04:30:00 +0300
categories: [RSS]
tags: [gpu, sandbox-escape, rce, cve, chrome]
toc: true
---

Two critical use-after-free vulnerabilities (CVE-2026-9034 in Arm Mali GPU driver, CVE-2026-93374 in Chrome WebGPU/Dawn) allow remote code execution and sandbox escape when triggered via WebGL or WebGPU JavaScript payloads. The Arm Mali vulnerability affects 5th-generation GPU drivers used across smartphones, tablets, and IoT devices; the Chrome variant is exploitable via crafted HTML pages on Android. Researcher Florian Schweitzer employed AI-assisted fuzzing and reverse engineering of proprietary GPU firmware to discover these, demonstrating a research methodology that sidesteps traditional fuzzing limitations by targeting stateful GPU behavior at system boundaries. The article highlights a broader trend: external researchers contributed 34 critical Chrome CVE findings in 2026 (vs. only 3 in 2025) coinciding with Google's massive expansion of AI-driven automated vulnerability discovery.

[Read original article](https://certitude.consulting/blog/en/critical-vulnerabilities-discovered-in-google-chrome-and-arm-gpu-drivers/){: .btn .btn-primary }
