---
layout: post
title: "Enterprise Tech In, Shell Out (Progress Kemp LoadMaster Uninitialized Heap to Pre-Auth RCE CVE-2026-8037)"
date: 2026-06-29 19:24:54 +0300
categories: [RSS]
tags: [rce, memory-safety, pre-auth, infrastructure]
toc: true
---

Watchtowr Labs details CVE-2026-8037, a pre-authentication remote code execution in Progress Kemp LoadMaster (versions 7.2.63.1 and older when API enabled). The vulnerability stems from an uninitialized heap buffer and missing null terminator in the escape_quotes() function, which fails to properly sanitize shell arguments, enabling command injection. The patch replaced malloc() with calloc() and added proper string termination. Edge appliances like Kemp LoadMaster are critical infrastructure targets, making this an immediately exploitable path into enterprise networks.

[Read original article](https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/){: .btn .btn-primary }
