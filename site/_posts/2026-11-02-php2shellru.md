---
layout: post
title: "php2shell.ru"
date: 2026-11-02 00:00:00 +0300
categories: [RSS]
tags: [rce, memory-safety, php, cve, supply-chain]
toc: true
---

Two critical memory safety vulnerabilities (CVE-2026-109618, CVE-2026-109619) in PHP's core enable remote code execution without authentication. CVE-2026-109618 exploits out-of-memory (OOM) error handling to achieve code execution from the PHP-FPM worker context; CVE-2026-109619 is a use-after-free via stale global state between requests that leaks sensitive data (API keys, session tokens, passwords) from worker memory or enables code execution. Both carry CVSS 9.2 and affect all PHP versions below 8.2.35/8.3.36/8.4.27/8.5.12 (including legacy 5.4+) — vulnerability exists at the interpreter level regardless of application code quality. Patches released October 21, 2026; PHP 7.4–8.1 (EOL) receive source-only patches; PHP 7.3 and earlier receive no patches.

[Read original article](https://php2shell.ru){: .btn .btn-primary }
