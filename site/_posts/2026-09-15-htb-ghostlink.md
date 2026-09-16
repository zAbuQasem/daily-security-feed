---
layout: post
title: "HTB: Ghostlink"
date: 2026-09-15 09:00:00 +0300
categories: [RSS]
tags: [ctf, ntlm-relay, kerberos, symlink, active-directory]
toc: true
---

A comprehensive HackTheBox write-up of Windows domain controller compromise combining multiple attack vectors. The exploit chain begins with anonymous MQTT subscription to discover internal infrastructure, then leverages NTLM relay of coerced authentication to access a restricted file sharing site. An unchecked path parameter in the download endpoint enables arbitrary file read, exposing a user's registry hive and password database. Credentials unlock a Gogs Git instance where a symlink flaw in the content API allows Git config overwriting for shell access. Password hash cracking yields domain account credentials, escalated via Kerberos certificate service abuse and machine account relay to the certificate authority, ultimately enabling domain dumping from the domain controller.

[Read original article](https://0xdf.gitlab.io/2026/09/15/htb-ghostlink.html){: .btn .btn-primary }
