---
layout: post
title: "Business CTF 2022: Chaining Self XSS with Cache Poisoning - Felonious Forums"
date: 2026-04-16 03:12:30 +0300
categories: [RSS]
tags: [ctf, xss, self-xss, cache-poisoning, session-hijacking]
toc: true
---

This CTF write-up shows how a nominally low-impact self-XSS in a forum application can be turned into a real account-compromise issue by chaining it with web cache poisoning. The attack relies on getting attacker-controlled client-side content cached and then served to other users, which causes JavaScript that should only run in the attacker's own session to execute in a victim's browser instead. Once the poisoned response is replayed cross-user, the payload can exfiltrate the victim's session cookie and enable session hijacking. The technique is valuable beyond the challenge because it illustrates how cache behavior can upgrade a self-only bug into a broadly exploitable client-side vulnerability.

[Read original article](https://rayhan0x01.github.io/ctf/2022/11/18/felonious-forums-business-ctf-2022-web-writeup.html){: .btn .btn-primary }
