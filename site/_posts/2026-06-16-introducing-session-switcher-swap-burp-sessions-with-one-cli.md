---
layout: post
title: "Introducing Session Switcher. Swap Burp Sessions with One Click!"
date: 2026-06-16 22:00:00 +0300
categories: [RSS]
tags: [burp, authorization, idors, web-security]
toc: true
---

Doyensec released Session Switcher, a Burp Suite extension that streamlines authorization testing by allowing testers to save and swap HTTP sessions (cookies and headers) with a single click rather than manual copying and pasting. The extension includes auto-update rules that automatically monitor Burp Proxy traffic and keep stored sessions current when JWTs refresh or cookies update in the browser, reducing manual overhead during IDOR and privilege escalation testing. It integrates into Burp's request editor with domain-based session filtering and plans to add auto-inject rules for transparent session switching, smarter automatic session tracking, and macro-based session refresh to maintain sessions indefinitely without manual re-authentication.

[Read original article](https://blog.doyensec.com/2026/06/17/session-switcher.html){: .btn .btn-primary }
