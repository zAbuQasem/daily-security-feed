---
layout: post
title: "Dissecting the JWR phishing framework"
date: 2026-08-13 10:00:35 +0300
categories: [RSS]
tags: [phishing, malware, c2, threat-intelligence, web]
toc: true
---

Cisco Talos identified JWR, an advanced phishing framework that impersonates checkout and login pages for Shopify, PayPal, Apple, Klarna, and banks with real-time operator control via AES-CTR encrypted WebSocket channels. The client engine uses a Host Bridge module relaying commands through a Vue.js application across 44 phishing pages, capturing keystrokes, payment card data, identity documents, SSNs, passport images, 2FA codes, and device fingerprints in real time. The framework employs Web Workers to maintain persistent WebSocket connections across page navigation and includes anti-analysis checks to evade debuggers. Talos assesses JWR as a likely variant of "The Outsider" PhaaS platform operated by Chinese-speaking threat actors. Active campaigns deliver the client via SMS lures impersonating toll authorities, postal services, and couriers targeting victims in Southeast Asia and the Middle East.

[Read original article](https://blog.talosintelligence.com/dissecting-the-jwr-phishing-framework/){: .btn .btn-primary }
