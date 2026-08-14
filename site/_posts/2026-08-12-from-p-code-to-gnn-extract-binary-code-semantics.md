---
layout: post
title: "From P-Code to GNN: extract binary code semantics"
date: 2026-08-12 22:00:00 +0300
categories: [RSS]
tags: [reverse-engineering, binary-analysis, malware-analysis, tool-release]
toc: true
---

Quarkslab releases `pcode_graph`, a Python library for extracting semantic Control & Data Flow Graphs from binary code, abstracting away architecture and compilation differences. The tool translates assembly into Ghidra's P-Code intermediate representation (63 opcodes vs. thousands of x86 mnemonics) to enable architecture-agnostic function similarity detection via neural networks. Key use cases include deobfuscation, vulnerability detection, gadget identification, and binary versioning; the approach sidesteps limitations of statistical feature extraction and compiler-specific variations that defeat simpler comparison methods. Open-sourced and pip-installable, with application to the Cisco-Talos benchmark dataset and a published ESANN 2026 paper on deobfuscation.

[Read original article](http://blog.quarkslab.com/from-p-code-to-gnn-extract-binary-code-semantics.html){: .btn .btn-primary }
