---
layout: post
title: "PHP2Shell Operational Guidance"
date: 2026-10-23 14:44:06 +0300
categories: [RSS]
tags: [rce, php, cve, critical, patch-available]
toc: true
---

Two critical unauthenticated remote code execution vulnerabilities (CVE-2026-109618 and CVE-2026-109619, CVSS 9.2) in PHP affect all versions 8.2–8.5. CVE-2026-109618 exploits out-of-memory corruption during request handling, while CVE-2026-109619 leverages stale global state in the session handler—both enable RCE in PHP-FPM, Apache mod_php, and other SAPI implementations. Active exploitation has been observed by Cloudflare, Amazon, and WatchTowr; patches were released on 21 October for PHP 8.5.12, 8.4.27, 8.3.36, and 8.2.35. NVISO provides detailed vulnerability-specific mitigations including memory limits, post_max_size tuning, session handler disabling, and container resource isolation for environments unable to patch immediately.

[Read original article](https://blog.nviso.eu/2026/10/23/php2shell-operational-guidance/){: .btn .btn-primary }
