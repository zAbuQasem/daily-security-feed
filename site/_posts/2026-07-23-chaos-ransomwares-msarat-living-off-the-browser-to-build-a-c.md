---
layout: post
title: "Chaos ransomware's msaRAT: Living off the browser to build a covert C2 channel"
date: 2026-07-23 10:00:38 +0300
categories: [RSS]
tags: [malware, c2, ransomware, evasion, browser-hijacking]
toc: true
---

msaRAT is a Rust-based remote access trojan attributed to the Chaos ransomware group that employs a novel C2 evasion technique: the malware hijacks Chrome or Edge, launches it in headless mode, and tunnels all command-and-control traffic exclusively through the Chrome DevTools Protocol (CDP) and WebRTC DataChannels via Cloudflare Workers and Twilio TURN relays—never making direct network connections itself. This allows the RAT to evade network monitoring and firewall rules that rely on port-based filtering without protocol inspection. The malware is deployed via an MSI installer masquerading as a Windows update, uses the Tokio async runtime to manage concurrent operations (ECDH key exchange, C2 frame processing), and provides remote code execution and covert tunneling capabilities. The browser-as-proxy technique represents a meaningful evolution in C2 infrastructure hiding.

[Read original article](https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/){: .btn .btn-primary }
