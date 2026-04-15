---
layout: post
title: "Authenticated Arbitrary File Read via Race Condition leads to 0-Click Account Take Over on n8n"
date: 2026-04-15 03:12:35 +0300
categories: [RSS]
tags: [toctou, file-read, symlink, n8n, account-takeover]
toc: true
---

The write-up describes an authenticated arbitrary file read in n8n's Read/Write File node caused by a time-of-check/time-of-use race around symlink resolution. Even after a prior symlink-traversal fix replaced path.resolve() with fs.realpath(), the code still performs fsAccess(), path validation, and createReadStream() as separate operations, so an attacker can flip a symlink between an allowed path and a restricted path in the gap between checks. The author demonstrates this by rapidly switching a symlink target between /home/node and /etc, then weaponizing n8n's Git nodes and branch checkouts to perform the flip entirely from workflows until protected files are opened. Because the primitive yields reads of arbitrary files accessible to the n8n process, it can expose high-value secrets and be chained into zero-click account takeover, making it a strong technical bug chain against both self-hosted and cloud deployments.

[Read original article](https://lab.ctbb.show/writeups/toctou-leads-to-ato-on-n8n){: .btn .btn-primary }
