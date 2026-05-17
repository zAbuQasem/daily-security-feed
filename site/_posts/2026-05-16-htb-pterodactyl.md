---
layout: post
title: "HTB: Pterodactyl"
date: 2026-05-16 13:45:00 +0300
categories: [RSS]
tags: [ctf, directory-traversal, lfi, linux, privesc]
toc: true
---

This Hack The Box write-up chains multiple real-world style bugs, starting with an unauthenticated directory traversal in Pterodactyl Panel's locale endpoint that lets PHP include attacker-controlled files from disk. The author combines that with the PEAR `pearcmd` trick to write and execute a webshell, then pulls database credentials, cracks a bcrypt password hash, and pivots through password reuse to gain a stronger user foothold. For privilege escalation on openSUSE, the box abuses a PAM environment-variable issue to make Polkit treat the session as local console access, then leverages a libblockdev/udisks flaw to mount a crafted XFS image containing a SetUID-root shell. The Beyond Root section adds practical kernel exploitation notes by reproducing CopyFail and DirtyFrag page-cache privilege-escalation exploits, making the post useful as both a walkthrough and a survey of modern Linux exploitation primitives.

[Read original article](https://0xdf.gitlab.io/2026/05/16/htb-pterodactyl.html){: .btn .btn-primary }
