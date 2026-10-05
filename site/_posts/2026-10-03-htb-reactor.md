---
layout: post
title: "HTB: Reactor"
date: 2026-10-03 13:45:00 +0300
categories: [RSS]
tags: [ctf, rce, react, deserialization, privilege-escalation]
toc: true
---

HackTheBox write-up demonstrating React2Shell, a pre-authentication RCE vulnerability where NextJS React Server Components unsafely deserialize malicious data from server function requests, yielding immediate shell access. Post-exploitation involves cracking password hashes from an embedded SQLite database for lateral movement, then abusing a NodeJS monitoring script running as root with the inspector protocol enabled on localhost (via Chrome DevTools Protocol or direct node CLI) to execute arbitrary code in the privileged process. While CTF-focused, the techniques illustrate realistic attack chains against NextJS applications and Node.js inspector misconfigurations.

[Read original article](https://0xdf.gitlab.io/2026/10/03/htb-reactor.html){: .btn .btn-primary }
