---
layout: post
title: "How to detect HTTP/2 abuse in Apache web server logs"
date: 2026-05-27 00:00:00 +0300
categories: [RSS]
tags: [detection, http2, apache, rce, dos]
toc: true
---

CVE-2026-23918 is a high-severity double-free vulnerability in Apache 2.4.66's mod_http2 module, triggered by a HEADERS frame followed immediately by an RST_STREAM frame with a non-zero error code — if the RST arrives before the multiplexer finishes registering the stream, a double-free corrupts worker memory, enabling crash or RCE (non-prefork configs). The article also covers CVE-2023-44487 (HTTP/2 Rapid Reset DoS) and CVE-2023-45802 (memory leak on stream reset). It explains how to enable `LogLevel http2:debug` to surface stream-level events invisible in default access logs, and describes two detection patterns: high-volume RST_STREAM bursts from a single IP (AH03067 with error=0) and HEADERS+RST_STREAM pairs followed by segfault (AH00052). Practical guidance for Apache operators on log configuration and detection with Datadog is included.

[Read original article](https://www.datadoghq.com/blog/detect-http2-abuse-apache-web-server-logs/){: .btn .btn-primary }
