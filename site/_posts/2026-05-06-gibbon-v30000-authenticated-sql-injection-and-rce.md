---
layout: post
title: "Gibbon v30.0.00: Authenticated SQL Injection and RCE"
date: 2026-05-06 23:12:32 +0300
categories: [RSS]
tags: [sqli, rce, lfi, php, authenticated]
toc: true
---

Project Black describes an authenticated exploit chain in the Gibbon school management platform v30.0.00 that starts with SQL injection in `modules/Tracking/graphing.php` and ends in code execution. The SQLi comes from building `WHERE` clauses by concatenating user-controlled `gibbonDepartmentIDs`/related fields into the query string, letting a teacher-level user inject arbitrary SQL fragments despite some parameter binding elsewhere in the statement. The RCE path relies on `index.php?q=...` including attacker-controlled paths after weak validation in `Page::isAddressValid()`, which only enforces the presence of `.php` and a small blacklist, making local file inclusion possible. The write-up then chains this with the report archive import workflow to place crafted files outside the intended `/uploads` path and include them through the `q` parameter, yielding LFI-to-RCE and also enabling denial-of-service impacts; the issues were patched in v30.0.01.

[Read original article](https://projectblack.io/blog/gibbon-v30-authenticated-sql-injection-and-rce/){: .btn .btn-primary }
