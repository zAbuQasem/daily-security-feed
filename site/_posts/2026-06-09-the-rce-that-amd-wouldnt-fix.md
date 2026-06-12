---
layout: post
title: "The RCE that AMD wouldn’t fix!"
date: 2026-06-09 00:00:00 +0300
categories: [RSS]
tags: [rce, supply-chain, mitm, disclosure]
toc: true
---

A man-in-the-middle RCE vulnerability in AMD's AutoUpdate and Ryzen Master tools exploits the use of unencrypted HTTP URLs in the software update XML feed—while the metadata server itself uses HTTPS. The vulnerability requires no authentication or exploitation complexity: the AutoUpdater downloads executable files without signature validation and immediately executes them, allowing network-level attackers (corporate networks, public WiFi, ISP) to inject arbitrary code. AMD initially rejected the report as out of scope (claiming MITM attacks don't count), then requested the researcher suppress the disclosure for an extended 124-day embargo to patch multiple affected tools. The patch involved migrating update communications to HTTPS and adding signature verification, highlighting poor baseline security practices in critical software delivery infrastructure.

[Read original article](https://mrbruh.com/amd2/){: .btn .btn-primary }
