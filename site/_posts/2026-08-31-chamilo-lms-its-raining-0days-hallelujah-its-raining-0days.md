---
layout: post
title: "Chamilo LMS... It's raining 0days, hallelujah, it's raining 0days"
date: 2026-08-31 22:00:00 +0300
categories: [RSS]
tags: [sqli, rce, pre-auth, 0day, lms]
toc: true
---

Quarkslab identified 11 chained 0-day vulnerabilities in Chamilo LMS enabling unauthenticated remote code execution. The attack begins with an SQL injection in /main/inc/ajax/model.ajax.php where the `groupOp` parameter is concatenated directly into WHERE clauses without sanitization, accessible without authentication using only a valid `cidReq` course identifier. The SQLi is leveraged to extract password reset tokens, which are then used to reset the admin account. Subsequently, an email update vulnerability in user_manager.ajax.php allows the attacker to chain these primitives into a complete pre-authentication RCE. The write-up demonstrates how seemingly independent vulnerabilities combine to achieve full system compromise, with specific PoC requests and bypass techniques documented.

[Read original article](http://blog.quarkslab.com/chamilo-lms-its-raining-0days-hallelujah-its-raining-0days.html){: .btn .btn-primary }
