---
layout: post
title: "Unauthenticated remote code execution in JTL Shop"
date: 2026-06-17 00:00:00 +0300
categories: [RSS]
tags: [ssti, rce, ecommerce, credentials]
toc: true
---

A server-side template injection vulnerability in JTL Shop (introduced in version 5.2.0) allows unauthenticated attackers to read sensitive configuration data and execute arbitrary code. In JTL Shop 5.2.0–5.3.x, the SSTI grants read access to the Blowfish encryption key, database credentials, SMTP settings, and stored OAuth secrets. In version 5.4.0 and later, attackers can leverage registered Smarty modifiers (unserialize and file_get_contents) to write webshells to the web root and execute commands as the web server user. Sansec coordinated disclosure with JTL, which released patches for versions 5.5.4, 5.6.2, and 5.7.2, plus a back-patch for 5.0.0–5.7.0. All JTL Shop 5.2.0+ users should upgrade immediately and rotate compromised credentials.

[Read original article](https://sansec.io/research/jtl-shop-ssti-rce){: .btn .btn-primary }
