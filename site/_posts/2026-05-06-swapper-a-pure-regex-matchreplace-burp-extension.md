---
layout: post
title: "Swapper – A Pure Regex Match/Replace Burp Extension"
date: 2026-05-06 14:00:00 +0300
categories: [RSS]
tags: [burp-suite, regex, session-management, csrf, webapp]
toc: true
---

This post introduces Swapper, a lightweight Burp Suite extension that solves a common testing problem in stateful applications: requests that invalidate a session or anti-CSRF token after each use. The extension lets the tester define a response-side regex to extract fresh values such as JWTs, session IDs, or CSRF tokens, then applies a request-side regex replacement so Burp tools like Intruder and Scanner can keep sending valid requests. It is aimed at edge cases such as SOAP/XML workflows where Burp's built-in Match and Replace and some existing extensions do not reliably handle dynamic token rotation. The write-up also covers practical behavior such as per-request token exchange, timed auto-refresh, support for multiple regex pairs, and in-extension testing of extraction rules, making it a useful workflow tool for web app assessments rather than a pure product announcement.

[Read original article](https://www.blackhillsinfosec.com/swapper/){: .btn .btn-primary }
