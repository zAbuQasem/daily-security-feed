---
layout: post
title: "GorgonAgora: 4,800+ fake storefronts skim cards across hundreds of impersonated brands"
date: 2026-06-02 00:00:00 +0300
categories: [RSS]
tags: [card-skimming, threat-intelligence, phishing, malware, ioc]
toc: true
---

Independent researcher Hunter Heaivilin discovered GorgonAgora, a large-scale card skimming operation running 4,800+ fake .shop storefronts impersonating hundreds of major brands (Starbucks, Ford, Sony, Lego, Toyota, etc.). All sites use Medusa.js commerce framework with a custom PaymentVanilla SDK that injects a pixel-perfect fake Stripe iframe, exfiltrating card data via AES-256-GCM encrypted WebSocket to a single C2 server in Moldova (80.97.160.51). The skimmer includes real-time 3D Secure relay to complete fraudulent transactions invisibly, contains Chinese-language error strings, and has been active since August 2025 with continuous expansion. Comprehensive IOCs provided including file hashes, CSS fingerprints, domains, and infrastructure details.

[Read original article](https://sansec.io/research/gorgonagora-fake-storefront-skimming-network){: .btn .btn-primary }
