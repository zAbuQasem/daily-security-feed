---
layout: post
title: "Go fuzzing was missing half the toolkit. We forked the toolchain to fix it."
date: 2026-05-12 11:00:00 +0300
categories: [RSS]
tags: [go, fuzzing, libafl, grammar-based, tooling]
toc: true
---

Trail of Bits introduces gosentry, a fuzzing-focused fork of the Go toolchain that preserves the standard `testing.F` and `go test -fuzz` workflow while replacing the native engine with a LibAFL-backed runner. The main technical improvements are structure-aware fuzzing for composite Go types, grammar-based fuzzing via Nautilus, and additional bug detectors for integer overflows, truncation issues, data races, goroutine leaks, panic-on-log conditions, and execution timeouts that vanilla Go fuzzing often misses. Under the hood, gosentry captures the Go fuzz callback, builds a Go archive with libFuzzer-style entry points, and executes it in-process through a Rust-based runner, so existing harnesses can be reused with new CLI flags instead of being rewritten. The post also shows practical impact: differential and grammar-based campaigns using gosentry reportedly found real bugs in Optimism and Revm, including parser mismatches, denial-of-service panics, and state-root divergence issues.

[Read original article](https://blog.trailofbits.com/2026/05/12/go-fuzzing-was-missing-half-the-toolkit.-we-forked-the-toolchain-to-fix-it./){: .btn .btn-primary }
