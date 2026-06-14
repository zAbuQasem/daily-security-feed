---
layout: post
title: "HTB: VariaType"
date: 2026-06-13 13:45:00 +0300
categories: [RSS]
tags: [ctf, arbitrary-write, rce, path-traversal, filter-bypass]
toc: true
---

A detailed HackTheBox machine write-up demonstrating a multi-stage exploitation chain involving Git repository disclosure, single-pass filter bypass in a PHP validator's download feature, arbitrary file write via fontTools variable font generation (allowing PHP webshell injection), command injection through malicious archive filenames processed by FontForge, and finally path traversal in setuptools PackageIndex to achieve root via a sudo-allowed plugin installer. The chain showcases practical vulnerability chaining from information disclosure through privilege escalation.

[Read original article](https://0xdf.gitlab.io/2026/06/13/htb-variatype.html){: .btn .btn-primary }
