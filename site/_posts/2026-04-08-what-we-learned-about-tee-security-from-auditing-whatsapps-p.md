---
layout: post
title: "What we learned about TEE security from auditing WhatsApp's Private Inference"
source_url: https://blog.trailofbits.com/2026/04/07/what-we-learned-about-tee-security-from-auditing-whatsapps-private-inference/
date: 2026-04-08
priority: 1
tags: [tee, attestation, cryptography, cloud, privacy, github-zabuqasem, linkedin-zeyad-abulaban]
feed: https://blog.trailofbits.com/feed/
---

Trail of Bits audited WhatsApp's Private Inference system — a TEE-based architecture using AMD SEV-SNP and Nvidia confidential GPUs to process encrypted messages for AI features without exposing plaintext to Meta. The audit found 28 issues, 8 high-severity, including: post-measurement config loading enabling LD_PRELOAD injection (TOB-WAPI-13), ACPI tables excluded from attestation allowing malicious hypervisors to map fake DMA devices for memory extraction (TOB-WAPI-17), patch level verification trusting self-reported firmware rather than AMD's VCEK X.509 certificate (TOB-WAPI-8), and missing attestation freshness (no client nonce), enabling replay of stolen TLS session keys as a permanent backdoor (TOB-WAPI-7). Meta resolved 16 issues before launch — fixes include strict env var allowlisting, a custom bootloader verifying ACPI signatures, VCEK certificate validation, and binding attestations to the TLS client_random. This is high-signal research from Trail of Bits documenting real-world TEE deployment pitfalls with broad applicability to any confidential computing system.
