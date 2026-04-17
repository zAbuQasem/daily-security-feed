---
layout: post
title: "PowMix botnet targets Czech workforce"
date: 2026-04-17 03:12:24 +0300
categories: [RSS]
tags: [malware, powershell, phishing, c2, amsi-bypass]
toc: true
---

Cisco Talos documents a previously unreported PowerShell botnet, "PowMix," used in phishing campaigns against Czech organizations and job seekers, delivered through malicious ZIP archives containing an LNK-triggered loader. The first-stage script copies the archive into ProgramData, locates an embedded payload inside the ZIP via a hardcoded marker such as `zAswKoK`, reconstructs it with string substitutions, and uses `Invoke-Expression` to run the second stage entirely in memory after disabling AMSI by setting `AmsiUtils.amsiInitFailed` to true through .NET reflection. PowMix then hides its console window with `Win32ShowWindowAsync`, decrypts its C2 domain and config using a hardcoded XOR routine, derives a bot identifier from the Windows `ProductID` registry value via a CRC32-style checksum, and establishes scheduled-task persistence. Talos also notes evasive C2 behavior, including randomized beacon intervals, encrypted heartbeat data embedded in REST-like URL paths, and dynamic C2 domain updates, along with tradecraft overlaps with the earlier ZipLine/MixShell activity and Heroku-hosted infrastructure.

[Read original article](https://blog.talosintelligence.com/powmix-botnet-targets-czech-workforce/){: .btn .btn-primary }
