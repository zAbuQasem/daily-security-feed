---
layout: post
title: "Dissecting WerFault"
date: 2026-11-06 13:21:50 +0300
categories: [RSS]
tags: [reverse-engineering, windows, binary-analysis, detection-engineering, incident-response]
toc: true
---

FalconForce reverse-engineered WerFault.exe (Windows error reporting binary) using IDA and Microsoft symbols to document its command-line parameters and internal behavior. WerFault is security-relevant both offensively—attackers leverage it for LSASS dumping via silentprocessexit—and defensively, where sparse documentation impedes detection engineering and incident response. The analysis combines prior work (Windows Internals, Helge Klein, Hexacorn) with original reverse engineering, using wmain function analysis and symbol-guided binary inspection to clarify previously undocumented functionality and operational modes.

[Read original article](https://falconforce.nl/dissecting-werfault/){: .btn .btn-primary }
