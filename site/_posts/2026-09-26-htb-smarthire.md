---
layout: post
title: "HTB: SmartHire"
date: 2026-09-26 13:45:00 +0300
categories: [RSS]
tags: [ctf, deserialization, rce, privilege-escalation, python]
toc: true
---

A CTF write-up of the HackTheBox SmartHire machine. The attack chain exploits MLflow's PyFunc model deserialization vulnerability: after gaining access to an MLflow instance via default credentials, the attacker overwrites pickled model artifacts through the artifacts API, achieving remote code execution when the AI HR platform scores resumes. Privilege escalation leverages a sudo script that adds a writable directory to Python's path, allowing execution of malicious configuration files as code during Python startup.

[Read original article](https://0xdf.gitlab.io/2026/09/26/htb-smarthire.html){: .btn .btn-primary }
