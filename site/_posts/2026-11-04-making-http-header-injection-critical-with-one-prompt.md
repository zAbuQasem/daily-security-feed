---
layout: post
title: "Making HTTP header injection critical with one prompt"
date: 2026-11-04 15:12:29 +0300
categories: [RSS]
tags: [request-smuggling, desync, crlf-injection, cache-poisoning]
toc: true
---

PortSwigger Research describes techniques for escalating HTTP header injection to critical CRLF-Powered Desync attacks by injecting carriage-return line-feed sequences that cause request splitting at upstream proxies. The new Burp AT skill automates exploitation through a four-phase methodology: identifying injection location in upstream headers, validating desync via fuzzing payloads to detect distinct status codes, discovering open-redirect gadgets, and injecting a second request to redirect users to an attacker-controlled server. The primitive enables full-site takeover when chained with cache poisoning.

[Read original article](https://portswigger.net/research/making-http-header-injection-critical-with-one-prompt){: .btn .btn-primary }
