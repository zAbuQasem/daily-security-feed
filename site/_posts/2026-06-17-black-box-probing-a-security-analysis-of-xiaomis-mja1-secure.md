---
layout: post
title: "Black Box Probing: a Security Analysis of Xiaomi's MJA1 Secure Chip"
date: 2026-06-17 22:00:00 +0300
categories: [RSS]
tags: [reverse-engineering, hardware, firmware, secure-chip]
toc: true
---

Quark's Lab presents the first public reverse engineering of Xiaomi's undocumented MJA1 secure chip, used in their recent cameras. The authors performed black-box hardware analysis to identify the I2C communication interface (at address 0x2A), extracted flash firmware via NAND dumping with a Raspberry Pi, and reverse-engineered the chip's command protocol by brute-forcing undocumented commands. The analysis covers hardware identification, sniffing, firmware extraction, and protocol reconstruction with detailed technical methodology including logic analyzer captures, SPI pinout mapping, and custom tooling. While specific vulnerabilities are not detailed in the preview, this is the first systematic security assessment of a proprietary security-critical component in consumer devices, enabling future vulnerability research.

[Read original article](http://blog.quarkslab.com/black-box-probing-a-security-analysis-of-xiaomis-mja1-secure-chip.html){: .btn .btn-primary }
