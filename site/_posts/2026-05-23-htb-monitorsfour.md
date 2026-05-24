---
layout: post
title: "HTB: MonitorsFour"
date: 2026-05-23 13:45:00 +0300
categories: [RSS]
tags: [ctf, php-type-juggling, docker-escape, cve, rce]
toc: true
---

HTB MonitorsFour write-up chaining multiple vulnerabilities on a Windows host. PHP type juggling (loose comparison flaw) bypasses authentication on an API endpoint, leaking crackable password hashes. Credentials unlock a Cacti instance exploited via CVE-2025-24367 (command injection into rrdtool) to drop a webshell inside a Docker container. The container has direct access to the Docker Engine API (CVE-2025-9074) running on a Docker Desktop/WSL2 backend, enabling creation of a new container that mounts the Windows host filesystem for privilege escalation to root. The Beyond Root section details converting filesystem access into a Windows shell via scheduled task and dissects the PHP type juggling bug.

[Read original article](https://0xdf.gitlab.io/2026/05/23/htb-monitorsfour.html){: .btn .btn-primary }
