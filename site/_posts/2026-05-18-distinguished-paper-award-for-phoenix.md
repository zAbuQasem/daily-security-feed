---
layout: post
title: "Distinguished paper award for Phoenix!"
date: 2026-05-18 20:44:45 +0300
categories: [RSS]
tags: [rowhammer, ddr5, dram, hardware, privilege-escalation]
toc: true
---

ETH Zurich’s Phoenix research demonstrates the first successful Rowhammer-induced bit flips on DDR5 DRAM protected by modern Target Row Refresh (TRR) mitigations, showing that DDR5 is not immune to practical disturbance attacks. The work required reverse engineering both memory-controller behavior and in-DRAM mitigation logic, then developing much longer hammering patterns than prior DDR4 attacks plus a self-correcting refresh-synchronization technique to land flips reliably. The researchers report that bypassing these defenses is substantially harder on DDR5 than DDR4, but still feasible on real hardware from a major vendor. The result is practically significant because the team also shows a reliable privilege-escalation attack using the induced DDR5 bit flips in under two minutes, making this a high-signal advance in hardware fault exploitation.

[Read original article](https://comsec.ethz.ch/distinguished-paper-award-for-phoenix/){: .btn .btn-primary }
