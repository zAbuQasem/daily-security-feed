---
layout: post
title: "HTB: DevHub"
date: 2026-10-10 13:45:00 +0300
categories: [RSS]
tags: [ctf, rce, privilege-escalation, mcp]
toc: true
---

A HackTheBox exploitation chain demonstrating MCP server security vulnerabilities. The attack chain begins with an unauthenticated RCE endpoint on the MCPJam inspector service (port 6274) that spawns arbitrary processes from attacker-controlled commands. After gaining shell access, the attacker discovers a Jupyter Lab instance with its access token exposed in the systemd service file and process list, enabling lateral movement to a new user. Final privilege escalation involves accessing an internal MCP server running as root that exposes an undocumented tool capable of dumping the root user's private SSH key. The write-up illustrates practical security risks in AI agent infrastructure, including credential exposure in service configurations and insufficient API authentication.

[Read original article](https://0xdf.gitlab.io/2026/10/10/htb-devhub.html){: .btn .btn-primary }
