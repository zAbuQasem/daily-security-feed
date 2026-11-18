---
layout: post
title: "The challenge of defending against bulletproof dead drops on public blockchains"
date: 2026-11-18 11:00:00 +0300
categories: [RSS]
tags: [malware, c2, blockchain, threat-intelligence, evasion]
toc: true
---

Threat actors are leveraging public blockchains (Bitcoin, Ethereum, Solana, TRON) as resilient command-and-control infrastructure by embedding encrypted malware configurations directly into immutable blockchain transactions. The article traces the evolution of C2 evasion techniques—from domain generation algorithms and CDN domain fronting through peer-to-peer networks and dead drop resolvers—culminating in blockchain-based hosting, which eliminates the single point of failure that traditional domain seizures exploit. Because blockchain transactions are globally replicated, cryptographically verified, and cannot be unilaterally deleted or altered, adversaries can persistently update C2 endpoints via RPC queries without exposing centralized infrastructure vulnerable to law enforcement or ISP takedowns. The article emphasizes that conventional defensive approaches (domain blocklists, registrar suspension, sinkholing) are ineffective against this architecture, requiring a fundamental shift toward monitoring anomalous blockchain RPC traffic and analyzing endpoint memory for configuration retrieval patterns. Talos provides technical depth on how threat actors abuse blockchain's immutability and decentralization properties, presented from an authoritative threat intelligence source.

[Read original article](https://blog.talosintelligence.com/the-challenge-of-defending-against-bulletproof-dead-drops-on-public-blockchains/){: .btn .btn-primary }
