---
layout: post
title: "What are Hardware Private Cubic Circuits?"
date: 2026-07-04 00:00:00 +0300
categories: [RSS]
tags: [hardware, cryptography, side-channel, aes]
toc: true
---

HPCC (Hardware Private Cubic Circuits) is a novel d-probing PINI-secure gadget that implements a 3-input AND gate with single-cycle latency for arbitrary security orders d>1, solving a longstanding gap in composable side-channel resistant circuit design. Previous work achieved 1-cycle 3-input AND gates only in the d=1 probing model; this paper extends it to higher orders while maintaining unit latency through formal proofs and validated simulations. The contribution directly improves AES S-Box implementations, reducing latency from 3 cycles to 2 cycles (33% improvement), and the gadget generalizes to arbitrary finite field multiplication. The work demonstrates how modular gadget-based design with formal composability enables practical hardware side-channel security without reproving entire implementations for each optimization.

[Read original article](https://frereit.de/hpcc/){: .btn .btn-primary }
