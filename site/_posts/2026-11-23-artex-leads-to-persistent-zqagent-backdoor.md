---
layout: post
title: "ARTEX leads to persistent ZQAgent backdoor"
date: 2026-11-23 15:43:13 +0300
categories: [RSS]
tags: [malware, backdoor, persistence, evasion, apt]
toc: true
---

NVISO researchers discovered ZQAgent, a novel persistent Linux backdoor deployed by ARTEX (an LLM-driven intrusion tool) during incident response in Belgium and Asia. Unlike prior ARTEX operations focused on smash-and-grab credential theft, ZQAgent represents an escalation to operator-controlled persistent access via systemd services and cron jobs, with time-stomping. The backdoor achieves evasion through in-memory migration to anonymous files (`/memfd:a (deleted)`), process spoofing as `dbus-daemon`, and dynamic configuration encryption with multi-layer ChaCha20 variants. ZQAgent provides extensive capabilities: arbitrary code execution, file/filesystem operations, shell management, process control, and both blocking and non-blocking TCP/UDP tunneling. Infrastructure attribution to FOG0003 and targeting of government and human-rights organizations in Asia indicate state-level operational evolution in LLM-driven attack sophistication.

[Read original article](https://blog.nviso.eu/2026/11/23/artex-fog0003-zqagent-backdoor/){: .btn .btn-primary }
