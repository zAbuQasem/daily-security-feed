---
layout: post
title: "Adobe Acrobat Reader Escript.api Use-After-Free Remote Code Execution"
date: 2026-06-01 13:42:27 +0300
categories: [RSS]
tags: [use-after-free, rce, adobe, memory-corruption, javascript]
toc: true
---

A use-after-free vulnerability in Adobe Acrobat Reader's Escript.api module (CVE-2026-34621/34626/34622, patched April 2026) allows remote code execution through JavaScript prototype pollution. By using __defineGetter__() to install a getter on a non-configurable property of a built-in object like Collab.toString, an attacker can trigger recursive native code execution that exhausts the C++ stack without hitting JavaScript recursion limits. The exception handler in push_event_scope_and_resolve() fails to synchronize two independent bookkeeping mechanisms: the reference counting system decrements to zero and frees the object, but the event scope stack entry is never popped, leaving a dangling pointer. Accessing the freed object through the stale scope stack entry triggers the use-after-free, enabling exploitation on a widely-deployed PDF reader.

[Read original article](https://blog.exodusintel.com/2026/06/01/adobe-acrobat-reader-escript-api-use-after-free-remote-code-execution/){: .btn .btn-primary }
