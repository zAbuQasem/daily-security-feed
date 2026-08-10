---
layout: post
title: "Solving an ORB mystery"
date: 2026-08-09 00:00:00 +0300
categories: [RSS]
tags: [xs-leak, browser, service-worker, orb, bypass]
toc: true
---

A service worker on xsleaks.dev unintentionally bypasses Opaque Response Blocking (ORB), enabling XS-Leak attacks that detect HTTP status codes via script load/error events on cross-origin resources. The bypass works because service workers intercept fetch requests before the browser's ORB algorithm can validate response content-type, allowing opaque cross-origin responses to trigger load events instead of error events. The attack normally fails due to ORB treating mismatched content-types as network errors, but the service worker passthrough circumvents this protection. The investigation reveals the attack's "randomness" stems from service worker activation timing—workers don't claim clients until page reload or navigation occurs. This demonstrates a practical browser security gap where legitimate service worker caching logic can inadvertently weaken ORB's XS-Leak mitigations.

[Read original article](https://lab.ctbb.show/research/solving-an-orb-mystery){: .btn .btn-primary }
