---
layout: post
title: "HTB: Kobold"
date: 2026-08-01 13:45:00 +0300
categories: [RSS]
tags: [ctf, rce, lfi, docker, privilege-escalation]
toc: true
---

A HackTheBox writeup documenting exploitation of the Kobold machine, which chains multiple vulnerabilities: an unauthenticated RCE in MCPJam via binding to all interfaces and installing attacker-controlled MCP servers; a local file inclusion in PrivateBin's template-selection feature to write PHP webshells into mounted host directories; and privilege escalation through the Arcane Docker management panel by creating a container that mounts the host filesystem to install SSH keys for root access. The writeup demonstrates multi-stage exploitation across containerized services and credential reuse attacks.

[Read original article](https://0xdf.gitlab.io/2026/08/01/htb-kobold.html){: .btn .btn-primary }
