---
layout: post
title: "Anatomy of a Deno-Based Proxy & RAT"
date: 2026-06-15 08:03:20 +0300
categories: [RSS]
tags: [malware, rat, evasion, social-engineering, detection-engineering]
toc: true
---

A detailed forensic analysis of a sophisticated Deno-based remote access trojan delivered via mailbombing and fake IT support social engineering. The modular malware consists of four JavaScript files (dropper, C2 bridge, command execution engine, and TCP proxy) deployed with minimal permission flags to avoid triggering behavior-based defenses. Despite active EDR, the malware evaded detection through string array obfuscation and loopback-based local services; detection only occurred during subsequent reconnaissance activities. The analysis highlights the need to monitor scripting runtimes launched with elevated permissions, unusual loopback services, and collaboration platform impersonation rather than relying solely on binary analysis.

[Read original article](https://dfir.ch/posts/deno/){: .btn .btn-primary }
