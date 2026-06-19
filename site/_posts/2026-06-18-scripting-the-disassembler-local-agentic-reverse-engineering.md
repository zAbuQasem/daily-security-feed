---
layout: post
title: "Scripting the disassembler: Local agentic reverse engineering through vbdec’s live COM object model"
date: 2026-06-18 10:00:05 +0300
categories: [RSS]
tags: [reverse-engineering, tooling, automation, ai, malware-analysis]
toc: true
---

Talos Intelligence demonstrates a novel methodology for extending analysis tools with AI capabilities without modifying the tool itself: expose the tool's internal data model through Windows COM scripting interfaces. Using vbdec (a VB6 disassembler) as a case study, the authors show how local AI agents running Claude Code can access the live COM object model registered in the Windows Running Object Table, then iteratively script the tool to automate complex reverse-engineering tasks. Practical examples include P-code decompilation with reconstructed source code and inline comments, call graph generation in Graphviz format, bulk function metadata extraction to SQLite, and even coordinating multiple tools to synthesize comprehensive opcode reference databases. This approach keeps analyst data local, bypasses tool feature requests by letting users extend capabilities through prompts, and transforms interactive tools into queryable data servers.

[Read original article](https://blog.talosintelligence.com/scripting-the-disassembler/){: .btn .btn-primary }
