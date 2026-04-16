---
layout: post
title: "Uni CTF 2022: UNIX socket injection to custom RCE POP chain - Spell Orsterra"
date: 2026-04-16 03:12:30 +0300
categories: [RSS]
tags: [ctf, nginx, deserialization, php, rce]
toc: true
---

This CTF write-up presents a multi-stage web exploit chain that starts with Nginx UNIX socket injection to reach an internal application surface that was not intended to be exposed directly. The next step abuses queued message handling and unsafe deserialization, turning attacker-controlled data into execution of a custom PHP POP chain. The final payload is a PHP backdoor that survives image processing by bypassing PHP-GD compression constraints, with the post specifically calling out image-format manipulation around IDAT chunks as part of the technique. Although framed as a challenge, the chain is technically useful because it combines internal socket abuse, message-bus deserialization, and file-upload/image-processing tricks into a realistic path to RCE.

[Read original article](https://rayhan0x01.github.io/ctf/2022/12/30/spell-orsterra-uni-ctf-2022-web-writeup.html){: .btn .btn-primary }
