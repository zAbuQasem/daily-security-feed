---
layout: post
title: "CSS:the bomb inside your inbox"
date: 2026-08-06 22:00:00 +0300
categories: [RSS]
tags: [css, prompt-injection, webmail, xss, authentication]
toc: true
---

Gareth Heyes (PortSwigger Research) demonstrates CSS and HTML sanitization bypasses in major webmail clients (Gmail, Outlook, Fastmail, ProtonMail, Yahoo, AOL) that enable UI spoofing, token exfiltration, and account compromise. The research exploits discrepancies between what sanitizers permit and what browsers render—including abusing HTML `<label>` elements with `for` attributes to invoke hidden UI actions (with an unfixed Outlook bug allowing message pinning from email), and leveraging `:before`/`:after` pseudo-elements combined with opacity to create hidden content visible to LLMs but not users, enabling indirect prompt injection attacks against AI browsers like OpenAI's Atlas. The technique extracts recipient names and constructs URLs character-by-character to exfiltrate data during AI-assisted operations, demonstrating how trusted UI contexts can be broken through CSS alone.

[Read original article](https://portswigger.net/research/css-the-bomb-inside-your-inbox){: .btn .btn-primary }
