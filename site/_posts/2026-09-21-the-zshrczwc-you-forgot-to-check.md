---
layout: post
title: "The .zshrc.zwc You Forgot to Check"
date: 2026-09-21 23:03:20 +0300
categories: [RSS]
tags: [macos, persistence, dfir, malware, detection]
toc: true
---

zsh on macOS compiles shell startup files into wordcode binaries (`.zshrc.zwc`), and prioritizes loading the compiled version if it's newer than the plaintext source. This creates a critical forensic blind spot: investigators checking `.zshrc` may find it clean while malicious code in `.zshrc.zwc` executes silently at shell startup, as documented in MacSync Stealer intrusions. The compiled format provides obscurity through timestamp manipulation rather than encryption. The article demonstrates triage via `strings` and `zcompile -t`, and introduces `zwc-decompile.py`, a static parser that reconstructs shell semantics from wordcode without execution, enabling forensic teams to detect shell startup persistence that standard macOS investigation procedures miss.

[Read original article](https://dfir.ch/posts/compiled_zsh/){: .btn .btn-primary }
