---
layout: post
title: "We've got one word for it, and it's usually the wrong one"
date: 2026-09-10 18:00:15 +0300
categories: [RSS]
tags: [malware, evasion, credential-theft, delivery-chain, windows]
toc: true
---

Cisco Talos analyzed a complex WebDAV-based infection chain attributed to Russian threat actor UAT-10820 that delivers the Amatera stealer alongside ZigCryptoStealer and NetSupport Manager. The campaign leverages fake CAPTCHA prompts and BNB Smart Chain–hosted infrastructure to bypass web filters, with rundll32.exe used to load disguised DLL payloads. A notable evasion technique involves deploying a vulnerable driver to terminate EDR software, followed by memory-resident malware execution to evade detection. While discovered after targeting a Ukrainian government organization, Talos assesses this as an opportunistic, broad-based credential and cryptocurrency theft operation with practical implications for defenders monitoring WebDAV abuse, suspicious DLL loading patterns, and endpoint memory scanning.

[Read original article](https://blog.talosintelligence.com/weve-got-one-word-for-it-and-its-usually-the-wrong-one/){: .btn .btn-primary }
