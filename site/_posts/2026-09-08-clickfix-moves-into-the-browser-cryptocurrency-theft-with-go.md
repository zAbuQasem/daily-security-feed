---
layout: post
title: "ClickFix moves into the browser: Cryptocurrency theft with Google-hosted C2"
date: 2026-09-08 10:00:38 +0300
categories: [RSS]
tags: [malware, web-skimming, c2, social-engineering, cloud-abuse]
toc: true
---

Cisco Talos discovered a cryptocurrency-stealing campaign exploiting the Google Visualization API to deliver obfuscated JavaScript injected into victim browsers via ClickFix social engineering (convincing users to paste code into Chrome's address bar or Tampermonkey extension). The attackers host malicious scripts in publicly published Google Sheets documents, queried via the Visualization API's read-only query language, providing a persistent C2 channel within HTTPS traffic to a trusted domain. Once injected, the web skimmer hooks the browser's fetch API to intercept and replace cryptocurrency deposit addresses in server responses and the clipboard while displaying counterfeit bonus interfaces. The social engineering lure poses as a leaked vulnerability report for cryptocurrency swap services, targeting fraud-minded users through Telegram, dark forums, and paste sites. While targeting a specific niche, the techniques—legitimate service abuse combined with browser-based injection—could scale to supply-chain and e-commerce threats.

[Read original article](https://blog.talosintelligence.com/clickfix-moves-into-the-browser/){: .btn .btn-primary }
