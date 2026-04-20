---
layout: post
title: "CFITSIO Fuzzing: Memory Corruptions and a Codex-Assisted Pipeline"
date: 2026-04-20 03:13:10 +0300
categories: [RSS]
tags: [fuzzing, memory-corruption, parser, file-format, afl]
toc: true
---

Doyensec describes fuzzing the widely used CFITSIO FITS-parsing library and finding multiple memory-corruption issues, first with a generic AFL++ campaign and then by targeting the library's Extended Filename Syntax (EFS) parser. The key attack surface is that functions like `fits_open_file` do more than open a path: bracketed filename expressions can trigger extension lookup, image slicing, arithmetic on columns, filters, and temporary file creation before the application reads any data, so untrusted filenames can reach a large parser/evaluator stack. The write-up says triage reduced many crashes to a small set of root causes including operator-precedence bugs, unchecked token lengths, and unbounded concatenations, with AFLtriage used to cluster crashes and ASAN-instrumented rebuilds used to verify fixes. The novel angle is the workflow automation: Codex was used to generate harnesses and dictionaries, analyze crash reports to the function/offset/control-flow level, propose patches, and drive a rebuild-and-regression loop that let fuzzing continue past shallow crash states.

[Read original article](https://blog.doyensec.com/2026/04/20/cfitsio-fuzzing.html){: .btn .btn-primary }
