---
layout: post
title: "ARTEX führt zu einer dauerhaften ZQAgent-Backdoor"
date: 2026-11-23 15:41:27 +0300
categories: [RSS]
tags: [malware, backdoor, persistence, evasion, threat-intelligence]
toc: true
---

NVISO reports ZQAgent, a new Linux backdoor deployed via ARTEX (an LLM-based offensive tool), representing a novel shift from smash-and-grab attacks toward persistent compromise. ZQAgent evades detection by relocating to anonymous memory mappings (memfd:a) and spoofing its process name as dbus-daemon, while encrypting configuration with ChaCha20 and implementing dynamic runtime encryption. The backdoor provides extensive capabilities including arbitrary command execution, file operations, network tunneling, and dual persistence mechanisms via systemd services or cron jobs with timestamp manipulation. Attributed to threat actor FOG0003, ZQAgent infrastructure (37.122.150[.]15, bloonspace[.]com) has been observed targeting government agencies and human rights organizations across Belgium, Taiwan, and Asia—signaling a concerning tactic expansion where LLM tools automate initial access and subsequently install persistent backdoors.

[Read original article](https://blog.nviso.eu/2026/11/23/https-blog-nviso-eu-2026-11-20-artex-fog0003-zqagent-backdoor-de/){: .btn .btn-primary }
