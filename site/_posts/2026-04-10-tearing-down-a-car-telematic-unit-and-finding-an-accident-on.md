---
layout: post
title: "Tearing down a car telematic unit (and finding an accident on Facebook)"
date: 2026-04-10 03:13:01 +0300
categories: [RSS]
tags: [hardware, automotive, firmware, forensics, osint]
toc: true
---

Quarkslab researchers performed a full hardware teardown of a BYD Seal telematic unit (TCU) built around a Qualcomm MDM9628 (Snapdragon X5 LTE) SoC with a Micron MCP combining NAND flash and LPDRAM. They performed a chip-off extraction of the MCP via micro-soldering to a FlashcatUSB Mach1 reader, then reconstructed the raw NAND dump by stripping Qualcomm-specific OOB metadata (BCH ECC + 0xFF padding) to produce a clean linear binary. From the binary they parsed the Qualcomm SMEM partition table (16 partitions, 512 MB total) and extracted UBI/UBIFS filesystems including a custapp and system partition. Forensic analysis of the filesystem contents — logs, configuration, and cached data — combined with OSINT led them to identify a real-world BYD vehicle accident documented publicly on Facebook, demonstrating how second-hand automotive hardware can leak sensitive personal and vehicle data.

[Read original article](http://blog.quarkslab.com/tearing-down-a-car-telematic-unit-and-finding-an-accident-on-facebook.html){: .btn .btn-primary }
