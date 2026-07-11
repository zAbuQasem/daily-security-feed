---
layout: post
title: "Bluetooth Low Energy Security Testing, Consolidated: Introducing Caeruleus"
date: 2026-07-10 20:27:03 +0300
categories: [RSS]
tags: [ble, wireless, tooling, assessment]
toc: true
---

Caeruleus is a consolidated Go-based Bluetooth Low Energy testing tool that unifies fragmented Linux workflows across deprecated tools (hcitool, gatttool, bettercap) into a single binary built on the BlueZ stack. It consolidates scanning, GATT enumeration, handle read/write, characteristic fuzzing, and secrets detection (via Praetorian's titus library) with structured JSON/JSONL output and daemon mode for low-latency scripting. The tool addresses real friction in BLE assessments: non-interoperable tools, manual handle transcription, and poor automation support. Caeruleus includes a portable agent skill for LLM-based testing workflows, demonstrating significant efficiency gains (62% faster, 70% fewer tokens) compared to free-form tool selection.

[Read original article](https://www.praetorian.com/blog/ble-testing-caeruleus/){: .btn .btn-primary }
