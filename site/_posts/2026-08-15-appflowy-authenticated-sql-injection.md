---
layout: post
title: "AppFlowy Authenticated SQL Injection"
date: 2026-08-15 05:06:09 +0300
categories: [RSS]
tags: [sqli, rce]
toc: true
---

AppFlowy's quick-note search endpoint is vulnerable to authenticated SQL injection via the unsanitized `search_term` parameter, which is embedded directly into a JSON path query and appended raw to the SQL builder without sanitization. Any authenticated user can inject SQL payloads via `GET /api/workspace/{workspace-id}/quick-note?search_term={payload}` to dump, modify, or delete database contents; a proof-of-concept payload demonstrates extraction of database version information. The vulnerability (CVE-2026-16007) affects both the managed cloud offering and self-hosted deployments. AppFlowy indicated the issue was patched in their commercial cloud version but declined to patch the open-source codebase, creating a security gap for self-hosted users.

[Read original article](https://projectblack.io/blog/appflowy-authenticated-sql-injection/){: .btn .btn-primary }
