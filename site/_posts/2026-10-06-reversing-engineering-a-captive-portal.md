---
layout: post
title: "Reversing Engineering a Captive Portal"
date: 2026-10-06 16:00:00 +0300
categories: [RSS]
tags: [reverse-engineering, privacy, dns, iot]
toc: true
---

Binary Ninja reverse-engineered a StayFi Express captive portal (Raspberry Pi, three Go binaries) by dumping its SD card. The device implements DNS redirection to intercept unauthenticated HTTP requests, using MAC addresses for per-client access control. A critical privacy concern: the DNS server logs all queries (~11,801 in 3.5 hours) and forwards them via Datadog to StayFi's infrastructure, where they can be linked to guest personal data (email, phone, MAC, property IDs) collected during portal registration. StayFi's privacy policy permits sharing usage data with property managers and advertising partners. The captive portal can be bypassed by configuring a custom DNS server.

[Read original article](https://binary.ninja/2026/10/06/reverse-engineering-airbnb-captive-portal.html){: .btn .btn-primary }
