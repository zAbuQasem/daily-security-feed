---
layout: post
title: "pyghidra-mcp Meets Ghidra GUI: Drive Project-Wide RE with Local AI"
date: 2026-05-05 07:00:00 +0300
categories: [RSS]
tags: [reverse-engineering, ghidra, firmware, ai, mcp]
toc: true
---

The post introduces pyghidra-mcp v0.2.0, which adds a `--gui` mode that lets the same MCP server controlling project-wide Ghidra analysis also drive a live CodeBrowser window. Instead of fighting Ghidra's project lock with separate processes, the server and `ghidra.GhidraRun` run inside the same JVM and share the same `Program` objects, so MCP actions like `rename_function`, `set_comment`, `rename_variable`, `goto`, and `import_binary` immediately update the GUI and land in undo history. The author demonstrates the workflow on D-Link DNS-320L firmware for CVE-2024-3273, using a local Gemma model through OpenWebUI to pivot across two binaries and annotate the RCE chain end to end. It is essentially a reverse-engineering tooling write-up rather than a new vulnerability disclosure, but it provides concrete implementation details that matter for analysts building AI-assisted firmware RE workflows.

[Read original article](https://clearbluejar.github.io/posts/pyghidra-mcp-meets-ghidra-gui-drive-project-wide-re-with-local-ai/){: .btn .btn-primary }
