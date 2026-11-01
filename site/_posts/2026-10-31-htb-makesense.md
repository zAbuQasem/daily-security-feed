---
layout: post
title: "HTB: MakeSense"
date: 2026-10-31 14:45:00 +0300
categories: [RSS]
tags: [ctf, wordpress, xss, rce, password-reuse]
toc: true
---

A HackTheBox medium-difficulty write-up demonstrating a chained exploitation workflow on a WordPress site. Initial compromise via audio file in a publicly-accessible uploads directory containing a user's password read aloud. Secondary privilege escalation by reverse-engineering an encrypted voice transcription channel to inject arbitrary transcriptions, then exploiting XSS against an administrator bot to create an admin account and achieve code execution through the WordPress plugin editor. Final root compromise abuses an OCR web application running with root privileges that writes recognized text to an attacker-controlled filename, allowing arbitrary PHP file creation and execution.

[Read original article](https://0xdf.gitlab.io/2026/10/31/htb-makesense.html){: .btn .btn-primary }
