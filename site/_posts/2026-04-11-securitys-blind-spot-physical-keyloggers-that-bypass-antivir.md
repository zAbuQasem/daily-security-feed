---
layout: post
title: "Security’s Blind Spot: Physical Keyloggers That Bypass Antivirus Entirely"
date: 2026-04-11 03:10:12 +0300
categories: [RSS]
tags: [keylogger, usb, edr-evasion, dfir, physical-access]
toc: true
---

The article analyzes a hardware USB keylogger that evades traditional antivirus and EDR by operating entirely outside the host OS as a USB HID passthrough device. Using the AirDrive Forensic Keylogger Cable Pro as a case study, the authors show that the implant can log keystrokes while appearing to the operating system as a normal keyboard path, leaving no suspicious processes, hooks, registry changes, memory artifacts, or host-based exfiltration telemetry. In testing, the device exposed a 2.4 GHz soft-AP with a default SSID pattern like `AIR_XXYYZZ` and a local admin interface at `192.168.4.1` where captured keystrokes could be viewed and downloaded, with additional options for keyboard layout and wireless configuration. The practical takeaway is that compromise evidence shifts from host logs to physical security signals such as unauthorized device swaps, USB inventory changes, access-control records, and RF/network discovery of rogue hotspots, making this a useful DFIR-focused write-up on a blind spot in endpoint detection.

---

[Read original article](https://blog.nviso.eu/2026/04/10/securitys-blind-spot-physical-keyloggers-that-bypass-antivirus-entirely/){: .btn .btn-primary }
