---
layout: post
title: "Keystrokes in Disguise: Forensic Analysis of a Digispark HID Device"
date: 2026-10-16 19:50:34 +0300
categories: [RSS]
tags: [badusb, hid, forensics, incident-response, hardware]
toc: true
---

The Digispark ATtiny85 microcontroller board can be reprogrammed to emulate a USB keyboard and inject arbitrary keystrokes upon connection, enabling attacks such as downloading and executing payloads via hidden PowerShell or launching applications. Unlike the USB Rubber Ducky (which stores payloads on removable media), Digispark firmware is burned directly to the microcontroller, complicating forensic analysis and requiring hardware-level extraction via ICSP using a USBasp programmer (~€14 in equipment). The article provides practical incident-response methodology for safely extracting and analyzing Digispark firmware, demonstrating how to identify attack payloads and reconstruct attacker intent from extracted binaries. This is relevant for organizations responding to physical USB device implants and defensive teams building detection methods for HID-based attacks.

[Read original article](https://blog.nviso.eu/2026/10/16/keystrokes-in-disguise-forensic-analysis-of-a-digispark-hid-device/){: .btn .btn-primary }
