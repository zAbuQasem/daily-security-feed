---
layout: post
title: "Two critical RCEs in PHP core"
date: 2026-10-21 15:10:53 +0300
categories: [RSS]
tags: [rce, php, critical, memory-corruption]
toc: true
---

Two critical unauthenticated RCEs (CVE-2026-109618 and CVE-2026-109619, CVSS 9.2) in PHP core are exploitable via plain HTTP requests before application code executes, affecting every PHP build since 5.4. CVE-2026-109618 stems from out-of-memory handling that leaves request data partially initialized, which cleanup then treats as valid; CVE-2026-109619 is a use-after-free with stale internal state reused after backing memory is freed. The blast radius encompasses WordPress, Drupal, Magento, Laravel, and all PHP applications on cPanel/Plesk. Approximately 50% of PHP systems won't receive patches as PHP 8.1 and older are EOL; no active exploitation observed as of October 21, 2026.

[Read original article](https://blog.talosintelligence.com/two-critical-rces-in-php-core/){: .btn .btn-primary }
