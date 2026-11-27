---
layout: post
title: "How to Bypass Readout Protection on a Microcontroller"
date: 2026-11-27 07:00:00 +0300
categories: [RSS]
tags: [hardware-security, microcontroller, firmware-extraction, side-channel, readout-protection]
toc: true
---

This paper presents a technique for bypassing STM32L051 readout protection (RDP-1) by leaking cryptographic CRC values and register contents captured during the microcontroller's boot sequence via triggered HardFaults. Unlike prior voltage-glitching approaches that risk unintended flash erasure or instability on the STM32L051, this method exploits the fact that SRAM and scratch registers remain accessible even when readout protection is enabled, allowing reliable firmware extraction through precise timing-based side-channel observation. The researchers demonstrate the attack using a Pico Glitcher configured as a CMSIS-DAP debug probe with custom firmware, repeatedly power-cycling the target while sampling registers at different boot delays to build a dataset for correlation analysis. The technique successfully extracted firmware from an STM32L051 inside a Corsair Padlock 3 encrypted USB stick, raising questions about the security of hardware-protected cryptographic devices when attackers have direct physical access.

[Read original article](https://blog.syss.com/posts/tracerip/){: .btn .btn-primary }
