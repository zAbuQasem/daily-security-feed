---
layout: post
title: "Process Parameter Poisoning"
date: 2026-07-06 15:11:53 +0300
categories: [RSS]
tags: [edr-evasion, process-injection, windows, post-exploitation, detection-engineering]
toc: true
---

Process Parameter Poisoning (P³) is a novel Windows code injection technique that bypasses leading EDR solutions by transferring malicious payloads through process creation parameters (command line, environment variables, lpReserved STARTUPINFO field) rather than monitored APIs like WriteProcessMemory and VirtualAllocEx. The technique exploits the Process Environment Block (PEB) and RTL_USER_PROCESS_PARAMETERS structures, which EDRs don't typically instrument, enabling code injection without triggering detection on four market-leading EDR platforms. Developed by SensePost (Orange Cyberdefense), the technique includes a working public PoC (p3-loader) and represents a significant advancement in post-exploitation tradecraft for Windows environments by evading common defensive telemetry.

[Read original article](https://sensepost.com/blog/2026/process-parameter-poisoning/){: .btn .btn-primary }
