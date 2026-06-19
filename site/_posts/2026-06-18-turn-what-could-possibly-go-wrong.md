---
layout: post
title: "TURN! - What could possibly go wrong?"
date: 2026-06-18 05:00:00 +0300
categories: [RSS]
tags: [network-security, cloud, tunnel, c2, tool]
toc: true
---

TURN (Traversal Using Relays around NAT) servers relay UDP traffic for WebRTC-based communication platforms including Microsoft Teams and Zoom, but commonly misconfigured to forward traffic to unauthorized networks or internal systems. The article details attack vectors including XOR-MAPPED-ADDRESS information leaks that reveal internal NAT addresses, UDP-based relay abuse enabling blind forwarding to arbitrary targets, and demonstrates how public TURN services can be weaponized as covert C2 channels—a technique presented at Black Hat USA 2025 and DEF CON 33. TURNado, a new open-source tool suite, fills a practical gap by enabling reliable UDP relay testing, SOCKS5-over-TURN tunneling, mass allocation attacks, and red team bypass scenarios, with built-in security assessment modes that probe for common misconfigurations on production services.

[Read original article](https://blog.syss.com/posts/turnado/){: .btn .btn-primary }
