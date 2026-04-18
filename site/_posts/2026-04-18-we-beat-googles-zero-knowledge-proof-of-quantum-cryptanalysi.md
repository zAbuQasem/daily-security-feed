---
layout: post
title: "We beat Google’s zero-knowledge proof of quantum cryptanalysis"
date: 2026-04-18 03:10:50 +0300
categories: [RSS]
tags: [zero-knowledge, zkvm, rust, cryptography, memory-safety]
toc: true
---

Trail of Bits shows that Google’s published zero-knowledge proof for optimized quantum cryptanalysis was forgeable because the Rust-based zkVM prover pipeline contained multiple memory-safety and logic bugs, not because the underlying quantum circuit improved. Google’s setup used Succinct Labs’ SP1 zkVM to verify a private kickmix quantum circuit by deserializing the circuit, simulating elliptic-curve point addition over 9,024 sampled inputs, and committing public bounds for total operations, qubits, and Toffoli gates. By crafting malicious private input that exploits flaws in the simulator and circuit-handling logic, Trail of Bits produced a proof accepted by Google’s original unpatched verifier with the same verification key while falsely claiming dramatically better metrics, including zero Toffoli gates and fewer qubits. The practical takeaway is that zk proofs inherit a real application-security attack surface: bugs in guest code, parsing, or metric accounting can make cryptographically valid proofs attest to false performance claims even when the math of the proving system itself remains sound.

[Read original article](https://blog.trailofbits.com/2026/04/17/we-beat-googles-zero-knowledge-proof-of-quantum-cryptanalysis/){: .btn .btn-primary }
