---
layout: post
title: "AMSI Memory Patching Refrain"
date: 2026-11-23 15:06:18 +0300
categories: [RSS]
tags: [amsi, evasion, windows, edr-bypass, malware]
toc: true
---

This article provides a technical deep-dive into AMSI memory patching as a bypass technique against Microsoft's Antimalware Scan Interface. The author explains the AMSI architecture (amsi.dll client and Windows Defender provider), the critical AmsiScanBuffer() function, and how attackers can patch machine code at the function prologue to return controlled HRESULT values (like S_OK or E_INVALIDARG) using simple x64 assembly (MOV RAX, 0x00 and RET instructions). The article discusses EDR detection risks when modifying memory protections (Read/Write/Execute pages) and addresses how to select appropriate return codes to avoid suspicion by calling processes. While focused on established bypass methodology rather than novel techniques, it provides hands-on implementation guidance useful for offensive operators and defensive engineers understanding common AMSI evasion tactics.

[Read original article](https://whiteknightlabs.com/2026/11/23/amsi-memory-patching-refrain/){: .btn .btn-primary }
