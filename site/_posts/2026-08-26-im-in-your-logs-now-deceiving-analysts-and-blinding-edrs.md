---
layout: post
title: "I’m in your logs now: deceiving analysts and blinding EDRs"
date: 2026-08-26 08:01:09 +0300
categories: [RSS]
tags: [edr, detection-evasion, etw, blue-team, telemetry]
toc: true
---

This article explores how to manipulate Event Tracing for Windows (ETW) to generate fake telemetry and blind EDR products like Microsoft Defender for Endpoint. The research demonstrates that unelevated attackers can create sufficient legitimate or malformed telemetry to overflow ETW buffer pools, causing real activity to be dropped or missed by cloud EDRs that rely on ETW and implement event capping. By understanding ETW's architecture (sessions, providers, buffers) and the tradeoffs EDRs make between coverage and bandwidth, attackers can inject enough noise to fragment or suppress legitimate security signals. The analysis reveals fundamental design issues: ETW was built for performance monitoring, not security, yet EDRs depend on it as a core telemetry source—making telemetry reliability inseparable from detection reliability.

[Read original article](https://falconforce.nl/in-your-logs-now/){: .btn .btn-primary }
