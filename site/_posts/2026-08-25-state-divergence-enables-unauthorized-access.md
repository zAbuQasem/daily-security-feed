---
layout: post
title: "State divergence enables unauthorized access"
date: 2026-08-25 11:00:00 +0300
categories: [RSS]
tags: [blockchain, authorization-bypass, cosmos, state-divergence]
toc: true
---

Trail of Bits disclosed a critical authorization bypass in Provenance Blockchain's marker module affecting 82 live financial asset markers. The bug exploits state divergence: the access control check compares a marker's stored supply field (always zero for non-fixed markers) against circulating supply, allowing any attacker to grant themselves admin permissions with zero tokens and subsequently mint arbitrary tokens or drain escrow balances. At discovery, vulnerable markers held ~$500k in nhash escrow across validator incentive funds and community grant programs. The fix (v1.29.0) corrected the authorization check to read live supply from the bank module instead of the stale marker struct field, eliminating the zero-equality bypass and restoring proper access control.

[Read original article](https://blog.trailofbits.com/2026/08/25/state-divergence-enables-unauthorized-access/){: .btn .btn-primary }
