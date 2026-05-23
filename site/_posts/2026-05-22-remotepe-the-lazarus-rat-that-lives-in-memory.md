---
layout: post
title: "RemotePE: The Lazarus RAT that lives in memory"
date: 2026-05-22 14:55:58 +0300
categories: [RSS]
tags: [lazarus, dpapi, rat, malware, edr-evasion]
toc: true
---

Fox-IT analyzes a Lazarus-linked three-stage Windows implant chain made up of DPAPILoader, RemotePELoader, and RemotePE, where the final RAT is executed entirely in memory and never written to disk. The first-stage DLL masquerades as a legitimate Windows service component (for example `C:\Windows\System32\Iassvc.dll` under the fake "Internet Authentication Service"), searches `C:\ProgramData\Microsoft\Windows\DeviceMetadataStore\en-US*.*` for non-`MSCF` files larger than 50 KiB, then decrypts the payload with Windows DPAPI and an additional XOR `0x8D` layer before reflective loading via libpeconv. That DPAPI-based environmental keying binds payloads to the victim machine, frustrates VirusTotal and static analysis, and produces per-victim ciphertext that defeats simple hash-based detection. The recovered second stage polls C2 for the in-memory RemotePE payload and applies syscall-based evasion using the TartarusGate variant of HellsGate, indicating a low-footprint, long-dwell intrusion set tailored for stealthy financial and cryptocurrency targeting.

[Read original article](https://blog.fox-it.com/2026/05/22/remotepe-the-lazarus-rat-that-lives-in-memory/){: .btn .btn-primary }
