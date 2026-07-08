---
layout: post
title: "HTB: Abducted"
date: 2026-07-07 09:00:00 +0300
categories: [RSS]
tags: [ctf, samba, rce, privilege-escalation, symlink]
toc: true
---

Abducted is an HTB machine that chains multiple Samba exploitation techniques. Initial foothold exploits command injection in Samba's printing subsystem where an unescaped print job name is passed directly to shell. Subsequent privilege escalation involves decoding obfuscated rclone credentials to access shared storage, exploiting a Samba share configured with wide links and alternate execution context to write SSH keys to a third user's home directory, then abusing a systemd drop-in directory writable by a privileged group combined with polkit rules to inject a SetUID bash creation command. The walkthrough demonstrates practical exploitation of realistic Samba misconfigurations across multiple privilege levels.

[Read original article](https://0xdf.gitlab.io/2026/07/07/htb-abducted.html){: .btn .btn-primary }
