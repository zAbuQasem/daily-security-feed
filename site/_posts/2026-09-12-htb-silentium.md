---
layout: post
title: "HTB: Silentium"
date: 2026-09-12 13:45:00 +0300
categories: [RSS]
tags: [ctf, rce, privilege-escalation, authentication]
toc: true
---

A HTB machine write-up demonstrating exploitation of Flowise (visual AI agent builder) and internal services. The attack chain starts with an unauthenticated forgot password endpoint that returns reset tokens directly in the API response, enabling account takeover. Remote code execution is achieved by exploiting a node that passes user-supplied configuration to the JavaScript Function constructor, gaining execution as root inside a Docker container. Container escape leverages environment variable leakage of SSH credentials, followed by privilege escalation via symlink handling in a Gogs instance running as root to plant authorized keys for SSH access. The write-up includes reverse engineering of the Flowise frontend Vite application.

[Read original article](https://0xdf.gitlab.io/2026/09/12/htb-silentium.html){: .btn .btn-primary }
