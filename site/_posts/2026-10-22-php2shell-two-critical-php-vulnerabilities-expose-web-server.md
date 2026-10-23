---
layout: post
title: "php2shell: Two Critical PHP Vulnerabilities Expose Web Servers to Remote Code Execution"
date: 2026-10-22 15:04:18 +0300
categories: [RSS]
tags: [rce, php, critical, memory-safety, unauthenticated]
toc: true
---

Two critical PHP runtime vulnerabilities (CVE-2026-109618 and CVE-2026-109619, CVSS 9.2) enable unauthenticated remote code execution affecting all PHP deployments. CVE-2026-109618 involves memory corruption during out-of-memory conditions with improper cleanup; CVE-2026-109619 exploits stale global state accessible after memory deallocation in subsequent requests. Since PHP affects ~69% of websites and operates at the runtime level (not individual applications), all vulnerable installations require patching regardless of application-level security. Emergency patches were released October 21, 2026 (PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35), and exploitation attempts are already active in the wild with public proof-of-concept code available.

[Read original article](https://www.sygnia.co/threat-reports-and-advisories/php2shell-two-critical-php-vulnerabilities-expose-web-servers-to-remote-code-execution/){: .btn .btn-primary }
