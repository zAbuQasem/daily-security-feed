---
layout: post
title: "Mutation testing comes to DAML"
date: 2026-07-08 11:00:00 +0300
categories: [RSS]
tags: [mutation-testing, smart-contract, authorization, daml, testing]
toc: true
---

Trail of Bits extended Mewt, their open-source mutation-testing engine, to support DAML smart contracts by parsing DAML via a modified Haskell tree-sitter grammar and applying standard mutations (operator flips, branch removal) plus two DAML-specific mutations: Controller Party Swap (CPS, replacing one authorized party with another in scope) and Controller Party Removal (CPR, dropping a party from multi-party controller lists). The article demonstrates how DAML's built-in test coverage—which only reports whether templates and choices were exercised—lies about test quality, allowing 100% coverage while missing critical authorization bugs that happy-path tests never verify. Mutation testing closes this gap by deliberately sabotaging code and counting how many mutants the test suite catches, turning each surviving mutant into a specific missing test case. Setup requires only a brief `mewt.toml` pointing at the project and test command (`dpm test`), making it practical for production DAML development teams to quantify test effectiveness and surface high-severity authorization logic errors.

[Read original article](https://blog.trailofbits.com/2026/07/08/mutation-testing-comes-to-daml/){: .btn .btn-primary }
