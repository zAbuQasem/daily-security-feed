---
layout: post
title: "ARM64 stack internals and obfuscation on Apple Silicon"
date: 2026-08-14 12:21:52 +0300
categories: [RSS]
tags: [evasion, arm64, apple-silicon, reverse-engineering, post-exploitation]
toc: true
---

MDSec reverse-engineers how major EDR vendors detect malicious activity on macOS by walking call stacks using the `spindump` utility, then explores call-stack obfuscation techniques adapted for ARM64 architecture. The article provides deep technical foundation on ARM64 stack mechanics—register roles (sp, x29/FP, x30/LR), branch instructions (bl/blr vs b/br), and prologue/epilogue patterns using stp/ldp paired instructions—as groundwork for demonstrating how adversaries can corrupt or synthesize stack frames to evade detection. This is relevant for red teamers targeting Apple Silicon systems and defenders understanding ARM64-specific post-exploitation evasion vectors.

[Read original article](https://www.mdsec.co.uk/2026/08/arm64-stack-internals-and-obfuscation-on-apple-silicon/){: .btn .btn-primary }
