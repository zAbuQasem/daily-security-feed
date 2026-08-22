---
layout: post
title: "Connecting the Dots: Securing the Overlooked Corners of the Software Development Lifecycle (SDLC) Supply Chain"
date: 2026-08-21 23:00:21 +0300
categories: [RSS]
tags: [supply-chain, ci-cd, malware, npm, cloud]
toc: true
---

Unit 42 documents escalating SDLC supply chain attacks targeting developer tools and CI/CD pipelines rather than finished applications. The ChainDrop npm worm exemplifies this threat: it uses preinstall script hooks to download obfuscated payloads that scrape unencrypted OIDC tokens and credentials directly from GitHub Actions runner memory, then self-propagates via stolen npm/GitHub tokens while establishing persistence through VS Code and IDE configuration hijacking, with C2 managed through Ethereum blockchain transactions. The attack surface spans three overlooked domains—developer endpoints (sandboxless package managers and extensions), automated CI/CD pipelines (access to temporary secrets and build infrastructure), and cloud runtimes (container images with embedded system libraries)—requiring continuous cross-domain telemetry correlation rather than point-in-time static scans to detect malicious propagation chains.

[Read original article](https://unit42.paloaltonetworks.com/sdlc-supply-chain/){: .btn .btn-primary }
