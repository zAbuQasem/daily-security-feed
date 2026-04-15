---
layout: post
title: "Intercepting WCF Traffic with wcfproxy"
date: 2026-04-15 03:12:21 +0300
categories: [RSS]
tags: [wcf, net-tcp, soap, proxy, protocol-analysis]
toc: true
---

SySS introduces `wcfproxy`, a Go-based interception proxy for analyzing Windows Communication Foundation services that use Net.TCP, where SOAP envelopes are encoded in WCF's binary NBFX format instead of readable XML. The tool sits between client and server, forwards the TCP connection, rewrites the `To` endpoint via a `retarget` setting when needed, and converts binary WCF messages into a textual SOAP-like representation that can be logged or modified by interceptors. The article walks through how a simple `Health()` call appears on the wire over HTTP versus Net.TCP, showing that the opaque binary traffic is still the same SOAP message structure underneath, just encoded differently. This is practically useful for security assessments of legacy .NET client-server products because it lowers the barrier to inspecting, tampering with, and debugging Net.TCP WCF traffic that standard web testing tools cannot easily handle.

[Read original article](https://blog.syss.com/posts/wcfproxy/){: .btn .btn-primary }
