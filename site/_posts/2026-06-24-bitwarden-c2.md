---
layout: post
title: "Bitwarden C2"
date: 2026-06-24 17:55:53 +0300
categories: [RSS]
tags: [supply-chain, c2, cloud, confused-deputy, metadata-exfil]
toc: true
---

A bidirectional C2 channel discovered in Bitwarden's icon proxy (icons.bitwarden.net) exploits a confused deputy vulnerability (CWE-441) to relay commands and exfiltrate data through trusted infrastructure. Attackers embed JSON commands in PNG tEXt metadata chunks; the unauthenticated proxy fetches and passes them through byte-identical to the agent. Results are hex-encoded into DNS subdomain labels, with lookups originating from Bitwarden's Azure IPs (20.42.70.x, 20.115.49.x). The attack achieves SOC evasion by masquerading as favicon requests to a whitelisted domain, bypassing network monitoring and egress filtering. Bitwarden patched the vulnerability (PR #7668, v2026.6.1) by stripping all metadata chunks and reconstructing PNG files to include only rendering-essential chunks (IHDR, PLTE, IDAT, IEND, tRNS, sRGB, gAMA, cHRM).

[Read original article](https://thecontractor.io/bitwarden-c2/){: .btn .btn-primary }
