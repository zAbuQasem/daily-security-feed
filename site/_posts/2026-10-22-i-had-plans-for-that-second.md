---
layout: post
title: "I had plans for that second"
date: 2026-10-22 18:04:32 +0300
categories: [RSS]
tags: [rce, php, unauthenticated, web]
toc: true
---

Two unauthenticated remote code execution (RCE) vulnerabilities dubbed 'php2shell' were discovered in PHP affecting all versions from 5.4 onwards, triggered via simple HTTP requests. The vulnerabilities impact the vast majority of the internet—WordPress, Drupal, Magento, Shopware, WooCommerce, and thousands of other applications—with approximately 50% of PHP deployments running end-of-life versions that will never receive patches. Exploitation attempts have already been reported in the wild. Organizations must immediately upgrade to PHP 8.2 or later; Cisco Talos provides detection signatures (67359, 67360) for network-based defense.

[Read original article](https://blog.talosintelligence.com/i-had-plans-for-that-second/){: .btn .btn-primary }
