---
layout: post
title: "Validating Browser Defences with Push Security and delivr.to"
date: 2026-04-13 03:13:44 +0300
categories: [RSS]
tags: [browser, phishing, aitm, detection, identity]
toc: true
---

delivr.to describes an integration with Push Security that correlates browser-layer detections from Push's extension with specific payload links used in delivr.to web campaigns. The workflow polls the Push API during an active campaign and maps detections back to individual download URLs or, for AiTM/BiTM flows, correlates events using the detected domain and click timestamp when the user is redirected to Evilginx or EvilnoVNC infrastructure. The post explains that Push's extension observes in-browser signals such as visited pages, DOM context, credential entry, and authentication flows, which makes it useful for detecting credential proxy attacks against Okta, Microsoft 365, and Amazon login flows. This is mainly an operational validation write-up rather than novel research, but it is technically relevant for teams testing browser-delivered phishing controls, download monitoring, and identity-focused browser defenses end to end.

[Read original article](https://medium.com/@delivrto/validating-browser-defences-with-push-security-and-delivr-to-51d4f5300074?source=rss-1242be189bc------2){: .btn .btn-primary }
