---
layout: post
title: "HDGfx Infector"
date: 2026-11-17 00:00:00 +0300
categories: [RSS]
tags: [malware, worm, file-infector, polymorphic, evasion]
toc: true
---

HDGfx Infector is a Windows x86 file infector and USB worm active since mid-2026, infecting 32-bit executables in-place by overwriting the entry point with junk code and appending an RC4-encrypted, UPX-packed payload; each infection regenerates unique encryption keys and junk code for polymorphic evasion. The malware spreads via autorun.inf on removable drives and infected systems, with two confirmed builds (July and August 2026) still in active development. Infected hosts include Adobe, Java, Firefox, and Google Update components, with Authenticode signatures removed, plus deliberate targeting of antivirus installers (Bitdefender, Kaspersky). The worm polls a No-IP dynamic-DNS host for updates and was still spreading as of 2026-11-17, with earliest samples from 2026-10-22.

[Read original article](https://research.openanalysis.net/hdgfx/fileinfector/worm/usb/polymorphic/config/2026/11/17/hdgfx-infector.html){: .btn .btn-primary }
