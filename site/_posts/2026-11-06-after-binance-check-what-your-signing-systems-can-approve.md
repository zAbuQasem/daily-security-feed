---
layout: post
title: "After Binance, check what your signing systems can approve"
date: 2026-11-06 12:00:00 +0300
categories: [RSS]
tags: [supply-chain, wallet-security, blockchain, signing-infrastructure, devops]
toc: true
---

Trail of Bits analyzes the Binance October 2026 incident, where a compromised DevOps laptop and misused internal AI tool gave attackers access to the wallet-signing service, not the private key itself. The attacker obtained valid signatures to deploy an EIP-7702 delegation—a standing instruction allowing arbitrary code execution on the wallet—enabling repeated fund transfers without additional signatures. The article exposes a critical operational risk: signing services must monitor not just asset transfers but also authority changes (delegations, modules, ERC-4337 operations) that can persist across chains and enable future theft. Four concrete defensive controls are provided: restrict signing API access, treat delegations as administrative privileges requiring separate approval, enforce independent custody limits on the operational key, and detect all forms of wallet authority changes including EIP-7702 and ERC-4337 paths.

[Read original article](https://blog.trailofbits.com/2026/11/06/after-binance-check-what-your-signing-systems-can-approve/){: .btn .btn-primary }
