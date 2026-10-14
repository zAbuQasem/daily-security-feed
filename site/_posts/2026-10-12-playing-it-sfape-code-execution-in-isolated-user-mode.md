---
layout: post
title: "Playing It SFAPE: Code Execution in Isolated User Mode"
date: 2026-10-12 22:00:00 +0300
categories: [RSS]
tags: [windows, vbs, enclave, memory-corruption, cve]
toc: true
---

Doyensec research on code execution vulnerabilities in Windows VBS (Virtualization-Based Security) enclaves, specifically Isolated User Mode (IUM). The article demonstrates how memory corruption bugs in enclave DLLs—particularly improper pointer validation and TOCTOU conditions—can be chained to achieve arbitrary read/write primitives within VTL1 isolated memory. Using Edge's prefs_enclave_x64.dll as a case study, the research shows how vulnerabilities CVE-2023-36880 and CVE-2024-21423 enabled full enclave compromise despite attempted patches, and how reusing vulnerable enclave DLLs from VirusTotal archives enables exploration of VTL1/Secure Kernel attack surface. The memory model asymmetry (VTL1 code reads/writes VTL0 memory freely, but not vice versa) creates a novel attack class leveraging the host-enclave interface.

[Read original article](https://blog.doyensec.com/2026/10/13/Sfape.html){: .btn .btn-primary }
