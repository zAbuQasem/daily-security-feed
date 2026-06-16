---
layout: post
title: "Pi.Alert - Unauthenticated SQL Injection"
date: 2026-06-14 07:32:24 +0300
categories: [RSS]
tags: [sqli, auth-bypass, cve, data-exfiltration]
toc: true
---

Pi.Alert versions from 2024-06-29 onward contain an unauthenticated SQL injection in the `/pialert/php/server/devices.php` endpoint. The vulnerability bypasses authentication when `action=getDevicesTotals` is set, then concatenates the untrusted `scansource` URL parameter directly into a SQL WHERE clause via the `getDeviceCondition()` function without sanitization. An attacker can inject arbitrary SQL operators (e.g., `OR "1"="1`) to enumerate or dump the entire SQLite database. The article includes complete code flow analysis showing how input flows from request to query execution, plus working PoC commands for detection and exploitation with sqlmap.

[Read original article](https://projectblack.io/blog/pi-alert-unauthenticated-sql-injection/){: .btn .btn-primary }
