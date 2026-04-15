---
layout: post
title: "BSIM explained once and for all!"
date: 2026-04-15 03:12:31 +0300
categories: [RSS]
tags: [ghidra, reverse-engineering, binary-analysis, decompiler, similarity]
toc: true
---

Quarkslab reverse-engineers Ghidra's BSIM pipeline and explains how the tool fingerprints functions for cross-compiler, cross-optimization, and cross-architecture similarity matching. The post shows that BSIM operates on Ghidra's normalized High P-code rather than raw lifted instructions: functions are decompiled into SSA form, dead flag computations are stripped, stack-pointer mechanics are abstracted away, and the resulting P-code ops are incrementally hashed into a feature vector. It traces the implementation to the decompiler's C++ code, including the generateSignatures path in signature_ghidra.cc and the normalize action passes that produce the canonicalized representation used for matching. The article is valuable because it turns an underdocumented feature into a concrete, implementation-level explanation of how BSIM combines normalized IR features with locality-sensitive hashing and cosine-style vector comparison to identify semantically equivalent binary functions.

[Read original article](http://blog.quarkslab.com/bsim-explained-once-and-for-all.html){: .btn .btn-primary }
