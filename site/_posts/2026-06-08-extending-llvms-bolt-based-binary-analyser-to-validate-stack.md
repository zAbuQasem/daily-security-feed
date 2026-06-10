---
layout: post
title: "Extending LLVM's BOLT-based Binary Analyser to Validate Stack Variable Initialisation"
date: 2026-06-08 22:00:00 +0300
categories: [RSS]
tags: [binary-analysis, compiler-hardening, llvm, detection, memory-safety]
toc: true
---

Quarkslab extended LLVM's BOLT binary analyzer to validate the `-ftrivial-auto-var-init` compiler hardening flag through two complementary static analysis approaches: a load-oracle method that identifies automatic variables on the stack via memory loads, and a store-witness method that traces whether bytes are initialized before reads across control-flow paths. The resulting x86-64 scanner detects uninitialized stack variable reads by recovering direct and derived stack accesses, recognizing block initialization patterns, and verifying initialization both within and across function boundaries. Testing on GNU coreutils revealed the approach works in principle but generates false positives at scale, suggesting future work with symbolic execution or DWARF-assisted analysis could improve precision. This defensive tooling contribution enables security teams to verify that compiled binaries correctly implement the compiler's auto-initialization hardening guarantees.

[Read original article](http://blog.quarkslab.com/extending-llvms-bolt-based-binary-analyser-to-validate-stack-variable-initialisation.html){: .btn .btn-primary }
