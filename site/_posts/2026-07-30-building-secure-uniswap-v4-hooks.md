---
layout: post
title: "Building secure Uniswap v4 hooks"
date: 2026-07-30 11:00:00 +0300
categories: [RSS]
tags: [defi, smart-contracts, accounting, authorization, exploit-analysis]
toc: true
---

Trail of Bits analyzes seven recurring security failure patterns in Uniswap v4 hook implementations, which account for >$20M in losses (Cork ~$12M, Bunni). The core issue is that v4 inverts the pool model into a singleton PoolManager with hooks as independent contracts executing custom logic—shifting security responsibility from protocol to application code. Key failure patterns include: missing caller checks allowing direct callback invocation with malicious parameters; treating permissionlessly-created pools as legitimate, enabling attackers to route logic through custom pools with attacker-controlled currencies; and custom accounting bugs (sign errors, rounding, delta leaks) that succeed settlement checks but silently leak value. The analysis provides a secure-development checklist covering PoolKey validation, delta conservation, fee bounds, and token-specific behaviors (fee-on-transfer, rebasing, callbacks, pausable tokens).

[Read original article](https://blog.trailofbits.com/2026/07/30/building-secure-uniswap-v4-hooks/){: .btn .btn-primary }
