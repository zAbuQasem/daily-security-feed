---
layout: post
title: "HestiaCP Admin Takeover & RCE"
date: 2026-07-04 12:00:26 +0300
categories: [RSS]
tags: [authorization-bypass, privilege-escalation, rce, cve, hosting-panel]
toc: true
---

HestiaCP contains a critical authorization bypass (CVE-2026-12196) in the panel cron job editor. An undefined `$ROOT_USER` variable causes the permission check to always evaluate false, allowing low-privileged users to create/modify panel cron jobs that execute as a privileged panel account. By injecting a cron job calling `sudo /usr/local/hestia/bin/v-change-user-password admin [password]`, an attacker can reset the admin account password within one minute and achieve complete account takeover. The vulnerability is compounded by missing CSRF validation, enabling exploitation via a single HTTP request from an attacker-controlled context.

[Read original article](https://projectblack.io/blog/hestiacp-admin-takeover-rce/){: .btn .btn-primary }
