---
layout: post
title: "Introducing MacNoise!"
date: 2026-04-08 00:00:00 +0300
categories: [RSS]
tags: [detection, edr, macos, threat-hunting, telemetry]
toc: true
---

MacNoise is a modular macOS telemetry noise generator written in Go, designed to help defenders audit EDR, SIEM, and firewall coverage by generating real system events: process spawns, network connections, file writes, plist mutations, and TCC permission probes. It addresses a gap in the macOS security tooling ecosystem (historically dominated by Windows-focused tools) by enabling security teams to validate whether their stack actually captures what it claims to. The tool supports YAML-based scenarios for adversary emulation, allowing teams to chain modules that map to MITRE ATT&CK techniques and correlate results via audit log job IDs in a SIEM. Output adheres to OCSF (Open Cybersecurity Schema Framework) JSONL format, making it compatible with structured logging pipelines. Particularly useful for pre-incident visibility gap analysis and coverage RFIs.

---

[Read original article](https://0xv1n.github.io/posts/macnoise/)
