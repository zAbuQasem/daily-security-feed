---
layout: post
title: "Sansec adds support for Sylius 1 & 2"
date: 2026-06-01 00:00:00 +0300
categories: [RSS]
tags: [ecommerce, sylius, xss, malware, scanning]
toc: true
---

Sansec eComscan now supports server-side malware and vulnerability scanning for Sylius 1 and 2 eCommerce platforms. The article contextualizes the need by highlighting recent Sylius XSS vulnerabilities, including CVE-2026-31822 (XSS in checkout login form), CVE-2024-34349 (stored XSS in admin panel Name fields), and CVE-2024-29376 (XSS through Province field in address book). The scanner detects payment skimmers in templates and JavaScript, webshells and backdoors in writable directories, vulnerable plugins and dependencies, tampered core files, and persistence mechanisms. While Sylius ships with Symfony security features, breaches typically exploit stolen credentials, outdated dependencies, or custom third-party code that framework-level protections don't cover.

[Read original article](https://sansec.io/research/ecomscan-sylius){: .btn .btn-primary }
