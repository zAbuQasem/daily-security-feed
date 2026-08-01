---
layout: post
title: "The Xcode Assassin Returns: A Deep Dive Into the Latest XCSSET Version"
date: 2026-07-31 10:00:18 +0300
categories: [RSS]
tags: [malware, supply-chain, macos, evasion, backdoor]
toc: true
---

XCSSET v40 is an advanced macOS malware targeting developers through trojanized Xcode projects on GitHub, spreading via supply chain compromise since April 2026. The malware employs polymorphic payload generation with multi-layered cipher shifts, achieves fileless persistence through staged in-memory execution, and eliminates disk artifacts after installation. Its four-stage infection chain progresses from initial C2 loader to a memory-resident core module (boot orchestrator) that dynamically loads 17 specialized modules including browser hijacking via Chrome DevTools Protocol, clipboard monitoring, credential theft, and Telegram trojanization. The Chrome hijacking module wraps the legitimate Chrome binary to redirect user interaction, activate CDP on a predefined local port, and maintain persistence by restarting the malware orchestrator on each browser launch.

[Read original article](https://unit42.paloaltonetworks.com/xcsset-v40-malware-analysis/){: .btn .btn-primary }
