---
layout: post
title: "A “proof” of Fermat’s Last Theorem that fits the margin"
date: 2026-09-09 11:00:00 +0300
categories: [RSS]
tags: [formal-verification, implementation-bug, string-handling, lean]
toc: true
---

Trail of Bits discovered a critical bug in Lean 4's `String.Pos.Raw.extract` where the logical specification and compiled native code diverge: extracting a slice at an astronomically large position returns an empty string in the logical definition but the entire original string in native code. This disagreement enables constructing a proof of contradiction (empty string = non-empty string), allowing provably false theorems to be verified. The bug affects all stable Lean versions through 4.33.1 and undermines trust in machine-checked proofs using the `native_decide` axiom, demonstrating how implementation/specification mismatches in trusted proof systems can compromise formal verification of critical software.

[Read original article](https://blog.trailofbits.com/2026/09/09/a-proof-of-fermats-last-theorem-that-fits-the-margin/){: .btn .btn-primary }
