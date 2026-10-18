---
layout: post
title: "HTB: Eloquia"
date: 2026-10-17 14:45:00 +0300
categories: [RSS]
tags: [ctf, template-injection, csp-bypass, oauth, privilege-escalation]
toc: true
---

A Hack The Box Windows machine demonstrating a multi-stage exploitation chain against a Django blogging platform. An AngularJS template injection vulnerability in article bodies allows bypassing Content Security Policy using AngularJS directives to steal the admin bot's session cookie; alternatively, the OAuth flow is abused to link the admin account to a controlled account. As admin, a malicious SQLite extension is uploaded via the Django admin panel and loaded from the SQL Explorer to achieve code execution. From there, the attack leverages DPAPI-encrypted Edge passwords, pivots to another user with write access to a .NET service directory, and achieves SYSTEM privileges through AppDomainManager injection in the service config, DLL hijacking, or service executable overwriting.

[Read original article](https://0xdf.gitlab.io/2026/10/17/htb-eloquia.html){: .btn .btn-primary }
