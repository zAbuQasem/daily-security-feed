---
layout: post
title: "WAF Bypasses via h2 framing"
date: 2026-06-01 00:00:00 +0300
categories: [RSS]
tags: [http2, waf, bypass, reverse-proxy, infrastructure]
toc: true
---

HTTP/2 splits requests into separate binary frames (HEADERS, DATA) that can arrive at different times, allowing WAF bypasses when reverse proxies make security decisions before receiving complete request data. The research documents black-box methodologies for exploiting this timing gap across six popular proxies (Nginx, Apache, HAProxy, Envoy, Traefik, Caddy), finding five of six vulnerable due to architectural differences in h2-to-h1 translation and when WAF inspection occurs. Out-of-process WAFs are particularly vulnerable when proxies forward headers for inspection before bodies arrive, while ForwardAuth architectures never inspect bodies by design. Additional bypasses stem from Extended CONNECT method translation (RFC 8441) and ModSecurity/Coraza REQUEST_BODY variable only parsing form-urlencoded content (not JSON) in certain engine versions, though libmodsecurity3 on Nginx is immune.

[Read original article](https://lab.ctbb.show/research/h2-WAF-Bypasses){: .btn .btn-primary }
