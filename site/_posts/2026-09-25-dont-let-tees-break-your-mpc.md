---
layout: post
title: "Don't let TEEs break your MPC"
date: 2026-09-25 11:00:00 +0300
categories: [RSS]
tags: [tee, mpc, cryptography, attestation, threshold-signatures]
toc: true
---

Trail of Bits analyzes the security pitfalls of combining Trusted Execution Environments (TEEs) with multi-party computation (MPC) for threshold signature schemes. A malicious host can exploit TEE limitations by rolling back filesystem state after a signer deletes a pre-signature, forcing nonce reuse and private key disclosure — demonstrating how TEE confidentiality guarantees don't protect against stateful protocol attacks from an untrusted host. The article explains that TEE attestation can elevate semi-honest MPC protocols to malicious-security levels, but only if attestation verifies reproducible builds and binary transparency logs, not just cryptographic signatures. It clarifies the fundamental trust model clash: MPC distributes trust across participants while TEEs centralize trust in hardware manufacturers, creating an inversion of traditional security assumptions. Best practices include strong attestation verification, reproducible builds, and binding attestations to MPC participants' identities rather than treating TEEs as a substitute for sound protocol design.

[Read original article](https://blog.trailofbits.com/2026/09/25/dont-let-tees-break-your-mpc/){: .btn .btn-primary }
