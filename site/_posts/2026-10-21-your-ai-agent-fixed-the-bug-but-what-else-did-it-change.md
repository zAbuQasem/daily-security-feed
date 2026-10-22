---
layout: post
title: "Your AI agent fixed the bug, but what else did it change?"
date: 2026-10-21 15:00:00 +0300
categories: [RSS]
tags: [tool-release, regression-detection, ai-agents, supply-chain, patch-analysis]
toc: true
---

Trail of Bits released patching-bugs and regression-hunt plugins that delegate bug reproduction, patch development, and regression detection to AI agents, built through their Patch the Planet initiative with OpenAI. The regression-hunt plugin traces changed code through its callers to real interfaces, reproduces candidates on live deployments, replays proofs on isolated agents, and applies strict burden-of-proof validation to distinguish real regressions from false positives—achieving 25% fewer false-positive findings than baseline agents. Analysis of 130+ merged upstream patches identified 21 confirmed regressions (16 functional, one performance, four build/test), with agents providing live proof-of-concept evidence before and after changes. The design prioritizes modular, repeatable workflows with strict input/output schemas and threat-model incorporation to improve patch quality and reduce noise in vulnerability fixing at scale.

[Read original article](https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/){: .btn .btn-primary }
