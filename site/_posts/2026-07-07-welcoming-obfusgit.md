---
layout: post
title: "Welcoming ObfusGit"
date: 2026-07-07 04:00:00 +0300
categories: [RSS]
tags: [obfuscation, git, tool, code-protection, anti-scraping]
toc: true
---

ObfusGit is a Python tool that uses Git hooks to automatically encrypt and encode repository contents before pushing to public platforms, preventing AI scraping and unauthorized model training data harvesting. The workflow involves initializing the tool in a local repo, then running obfusgit sync to encrypt each commit; downstream users clone the encrypted repo and decrypt locally using a shared encryption key. The tool loses commit history across clone/decrypt cycles and is designed for static, read-only code distribution rather than active development tracking. It addresses the emerging concern of protecting proprietary source code from unauthorized AI training data harvesting on public repositories.

[Read original article](https://trustedsec.com/blog/welcoming-obfusgit){: .btn .btn-primary }
