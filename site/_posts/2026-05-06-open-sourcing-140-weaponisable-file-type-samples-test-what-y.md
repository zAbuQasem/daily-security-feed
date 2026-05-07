---
layout: post
title: "Open-Sourcing 140+ Weaponisable File Type Samples: Test What Your Defences Actually Block"
date: 2026-05-06 20:17:50 +0300
categories: [RSS]
tags: [email-security, file-formats, defense-evasion, phishing, detection]
toc: true
---

This post releases a public corpus of 140+ benign weaponizable file samples intended to validate whether mail gateways, web proxies, and endpoint controls block risky formats in practice rather than just on paper. The sample set covers alternate executable and script delivery formats such as .pif, .hta, .jnlp, ClickOnce .application, AutoIt, and AutoHotKey, plus obscure Office execution paths like .wll, .xll, .dotm, .xla, and a renamed .xlsm-to-.xls case to test header inspection versus extension-only filtering. It also includes evasion-focused containers and encrypted documents, including password-protected Office/PDF files and an Excel file leveraging the hardcoded VelvetSweatshop password, as well as ISO/IMG and concatenated ZIP variants that exercise Mark-of-the-Web loss and parser differentials between 7-Zip, WinRAR, and Explorer. The article is most useful as defensive validation guidance: it maps concrete file types to delivery and credential-coercion behaviors such as SMB/NTLM leakage via .theme files and remote connection prompts via .udl, helping defenders identify gaps in block lists and content inspection policies.

[Read original article](https://medium.com/@delivrto/open-sourcing-140-weaponisable-file-type-samples-test-what-your-defences-actually-block-f682e345af3c?source=rss-1242be189bc------2){: .btn .btn-primary }
