---
layout: post
title: "State-sponsored threats: Different objectives, similar access paths"
date: 2026-04-15 03:12:23 +0300
categories: [RSS]
tags: [threat-intel, apt, initial-access, social-engineering, persistence]
toc: true
---

Cisco Talos' 2025 review argues that state-sponsored operations from China, Russia, North Korea, and Iran differ in mission but converge on the same access patterns: rapid exploitation of newly disclosed flaws, continued use of older unpatched edge-device vulnerabilities, credential theft, and stealthy long-term persistence. The China section highlights near-immediate exploitation of issues such as ToolShell, followed by web shells, custom backdoors, tunneling utilities, and credential harvesting to maintain access in compromised environments. Russia-linked activity is described as relying heavily on legacy networking-device vulnerabilities and commodity malware such as Dark Crystal RAT, Remcos RAT, and Smoke Loader for operations tied to the Ukraine conflict, while North Korean campaigns used recruiter-themed social engineering like Contagious Interview to trick targets into executing code or surrendering credentials. For Iran, Talos contrasts overt disruption such as DDoS and defacement campaigns with quieter telecom-focused intrusions by ShroudedSnooper using compact custom backdoors, reinforcing the defensive takeaway that identity controls, edge visibility, and hunting for long-dwell persistence remain more important than focusing only on the latest CVE.

[Read original article](https://blog.talosintelligence.com/state-sponsored-threats-different-objectives-similar-access-paths/){: .btn .btn-primary }
