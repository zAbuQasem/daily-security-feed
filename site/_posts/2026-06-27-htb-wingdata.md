---
layout: post
title: "HTB: WingData"
date: 2026-06-27 13:45:00 +0300
categories: [RSS]
tags: [ctf, rce, privilege-escalation, path-traversal]
toc: true
---

A Hack The Box write-up detailing exploitation of Wing FTP Server's web interface via null-byte injection to smuggle Lua code into session files, achieving remote code execution. The attack chain continues through password hash cracking against Wing FTP's account files, privilege escalation via a Python backup-restore script that mishandles tarfile extraction, and exploitation of the tarfile module's 'data' filter path-validation bypass to write files outside the intended extraction directory and gain root access.

[Read original article](https://0xdf.gitlab.io/2026/06/27/htb-wingdata.html){: .btn .btn-primary }
