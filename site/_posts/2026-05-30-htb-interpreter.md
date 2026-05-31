---
layout: post
title: "HTB: Interpreter"
date: 2026-05-30 13:45:00 +0300
categories: [RSS]
tags: [deserialization, rce, ctf, java, python]
toc: true
---

HTB Interpreter write-up covering a Medium-rated Linux box running Mirth Connect, a Java-based healthcare integration engine. Initial foothold exploits an unauthenticated XStream deserialization vulnerability in the Mirth Connect REST API to achieve RCE as the mirth service account — a known critical vulnerability class in Java applications using XStream. Lateral movement uses database credentials extracted from the Mirth config to dump a MariaDB password hash, which is then cracked offline. Privilege escalation to root abuses a localhost Flask notification server that unsafely embeds XML-supplied user-controlled fields directly into Python f-strings and evaluates them, constituting a server-side template injection / code injection primitive.

[Read original article](https://0xdf.gitlab.io/2026/05/30/htb-interpreter.html){: .btn .btn-primary }
