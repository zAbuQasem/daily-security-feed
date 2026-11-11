---
layout: post
title: "Blind trust: stealing credentials through CSP"
date: 2026-11-11 14:26:01 +0300
categories: [RSS]
tags: [csp, xss, credential-theft, bypass]
toc: true
---

PortSwigger Research demonstrates two CSP bypass techniques via automated detection: first, finding known gadgets (JSONP endpoints, AngularJS) in allow-listed domains using a dataset of 350+ gadgets from cspbypass.com; second, a novel form-action exploitation vector that steals credentials even when JavaScript is fully blocked (default-src 'none'). The form-action attack exploits reflected HTML injection by injecting a self-posting form that submits data back to the same page (allowed by form-action 'self'), then uses <meta> tags with unsafe-url referrer policy to exfiltrate credentials in the Referer header via a second-stage redirect. The technique bypasses CSP entirely because no script executes and the form submits to an allowed origin. PortSwigger's Burp AT skill automates detection and PoC generation for both vectors, including a working lab demonstration, making CSP bypass discovery and exploitation practical.

[Read original article](https://portswigger.net/research/blind-trust-stealing-credentials-through-csp){: .btn .btn-primary }
