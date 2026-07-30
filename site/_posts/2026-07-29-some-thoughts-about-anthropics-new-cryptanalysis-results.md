---
layout: post
title: "Some thoughts about Anthropic’s new cryptanalysis results"
date: 2026-07-29 14:23:30 +0300
categories: [RSS]
tags: [cryptography, ai, post-quantum, attacks]
toc: true
---

Matthew Green analyzes two new cryptanalysis results from Anthropic using their Claude Mythos model. The HAWK attack performs key recovery on a proposed post-quantum signature scheme using the module Lattice Isomorphism Problem by extending known tools; while HAWK is not deployed, it was being evaluated for standardization and halving its security margin makes the scheme much harder to justify. The second result is an improved attack on 7-round AES requiring 2^89 operations and 2^105 chosen plaintexts—a modest constant-factor improvement over 2013 work but still entirely impractical. The core finding is that AI can now understand and synthesize existing cryptanalytic techniques into novel attacks with minimal human guidance, but the critical bottleneck has shifted to verification: distinguishing real results from misleading artifacts that appear plausible.

[Read original article](https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/){: .btn .btn-primary }
