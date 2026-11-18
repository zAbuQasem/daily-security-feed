---
layout: post
title: "Why your software needs a CBOM"
date: 2026-11-17 14:00:00 +0300
categories: [RSS]
tags: [supply-chain, post-quantum, cryptography, compliance]
toc: true
---

A Cryptographic Bill of Materials (CBOM) is a machine-readable inventory of cryptographic algorithms, protocols, and certificates used in software—a critical step mandated by NIST, US government agencies (OMB M-26-15, Executive Order 14412), and the EU for quantum-safe migration. The article explains the quantum threat timeline (RSA-2048 breakable with <1 million qubits in days, with 28-49% probability within 10 years) and 'harvest now, decrypt later' attacks, which expose confidential data sent over quantum-vulnerable key exchange today. NIST IR 8547 (October 2026) requires deprecation of RSA and ECDSA after 2030 and bans them after 2035, with new post-quantum algorithms (ML-KEM, ML-DSA, SLH-DSA) already standardized. The challenge is visibility: cryptographic choices are scattered across codebases, configuration files, and dependencies, making inventory collection difficult without automated tooling. CycloneDX 1.7+ provides the open standard for CBOMs with shared algorithm registries to ensure consistent cryptographic asset tracking across the supply chain.

[Read original article](https://www.sonarsource.com/blog/why-you-need-a-cbom/){: .btn .btn-primary }
