---
layout: post
title: "Sygnia Reveals New Activity by China-Nexus Threat Actor Fire Ant Targeting Trusted Infrastructure"
date: 2026-08-30 16:54:20 +0300
categories: [RSS]
tags: [apt, infrastructure, router, persistence, credential-theft]
toc: true
---

Sygnia's investigation of the China-nexus threat actor Fire Ant reveals a sophisticated campaign targeting critical infrastructure including Cisco IOS XR routers, TACACS authentication servers, and Linux management hosts. The adversary deployed two novel custom tools—BridgeAgent, a masquerading implant providing tunneling and root-level persistence via systemd, and TacTap, a TACACS credential-collection utility supporting library injection and Unix-socket file-descriptor handoff—to establish covert connectivity and intercept administrative authentication flows. Attack infrastructure was weaponized to collect traffic, suppress audit trails, and pivot to connected high-value environments through GRE tunnels and resilient persistence layers. The campaign demonstrates sophisticated defense evasion including log manipulation, SELinux disabling, and AAA request suppression, representing an evolution from prior 2025 hypervisor-focused activity into trusted infrastructure.

[Read original article](https://www.sygnia.co/press-release/sygnia-reveals-new-activity-by-china-nexus-threat-actor-fire-ant-targeting-trusted-infrastructure/){: .btn .btn-primary }
