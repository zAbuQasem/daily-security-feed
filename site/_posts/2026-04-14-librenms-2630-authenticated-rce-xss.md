---
layout: post
title: "LibreNMS < 26.3.0 Authenticated RCE & XSS"
date: 2026-04-14 03:12:05 +0300
categories: [RSS]
tags: [rce, xss, librenms, php, authenticated]
toc: true
---

The write-up describes two admin-to-admin vulnerabilities in LibreNMS before 26.3.0: a stored XSS on the `showconfig` page and an authenticated RCE via configurable troubleshooting binaries. The XSS stems from `includes/html/pages/device/showconfig.inc.php`, where `rancid_repo_url` is concatenated into an `<a href>` and only partially escaped, allowing an attacker-controlled payload such as `"><img/src/onerror=alert(1)><a x="` to execute when another admin visits `/device/<id>/showconfig` under valid RANCID Git settings. The RCE comes from `NetCommand.php`, which executes admin-configurable binary paths for commands like `whois`; combined with the weak `ip_or_hostname` validator in `AppServiceProvider.php` that accepts data after a `/`, an admin can repoint `whois` to `wget` to drop a script and then to `/bin/bash` to run it. Impact is limited to authenticated administrators, but the bug chain still yields code execution as the LibreNMS service user and shows how trusted configuration fields can become dangerous command-execution primitives.

[Read original article](https://projectblack.io/blog/librenms-authenticated-rce-and-xss/){: .btn .btn-primary }
