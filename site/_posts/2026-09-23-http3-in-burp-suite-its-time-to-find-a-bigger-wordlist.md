---
layout: post
title: "HTTP/3 in Burp Suite - it’s time to find a bigger wordlist"
date: 2026-09-23 14:00:00 +0300
categories: [RSS]
tags: [race-condition, http3, downgrade-attack, web-security]
toc: true
---

PortSwigger Research introduces HTTP/3 support in Burp Suite's Turbo Intruder, enabling fuzzing speeds exceeding 100,000 requests per second. The article details two novel HTTP/3-specific race condition techniques: Single Datagram Attack and QPACK Blocked Streams (Server-Side Race Orchestration), which achieve better timing synchronization than HTTP/1.1's single-packet approach. A new HTTP/3 Adapter extension enables testing of HTTP/3-only targets and HTTP/3 downgrade attacks via header injection. The toolkit also supports kettled request syntax for testing protocol downgrade vulnerabilities and includes automatic engine tuning for maximizing throughput across different network conditions.

[Read original article](https://portswigger.net/research/http3-in-burp-suite){: .btn .btn-primary }
