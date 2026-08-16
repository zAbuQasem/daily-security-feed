---
layout: post
title: "HTB: Cobblestone"
date: 2026-08-15 13:45:00 +0300
categories: [RSS]
tags: [ctf, sqli, xss, template-injection, rce]
toc: true
---

A detailed CTF write-up from 0xdf covering exploitation of HackTheBox's Cobblestone machine. The attack chain begins with a second-order SQL injection vulnerability in a PHP application hosting Minecraft-themed sites, used to extract application source code. Stored XSS then hijacks an admin session, escalating to Twig template injection for code execution as the web user. After bypassing AppArmor restrictions, database credentials are extracted, cracked for SSH access, and finally root is obtained through multiple exploitation methods against the Cobbler service running as root, including default credentials and authentication bypass.

[Read original article](https://0xdf.gitlab.io/2026/08/15/htb-cobblestone.html){: .btn .btn-primary }
