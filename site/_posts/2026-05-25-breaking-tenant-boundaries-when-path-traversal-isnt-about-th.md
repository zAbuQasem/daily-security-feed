---
layout: post
title: "Breaking Tenant Boundaries, When Path Traversal Isn't About the Filesystem"
date: 2026-05-25 14:50:00 +0300
categories: [RSS]
tags: [path-traversal, idor, multi-tenant, api-security, data-exposure]
toc: true
---

A pentest engagement against a multi-tenant social media monitoring/PR platform uncovered a cross-tenant data exposure via an atypical path traversal. The asset library download endpoint accepted `filename` and `folderPath` query parameters — but rather than resolving to a filesystem path, `folderPath` was used to construct an internal API backend URL, making this a server-side request forgery / SSRF-style path traversal rather than a classic file read. By manipulating `folderPath`, an authenticated user in Organisation A could enumerate and download files belonging to every other organisation on the platform, bypassing the intended tenant-scoped RBAC entirely. The case study illustrates how path traversal primitives can manifest in API URL construction rather than disk I/O, with IDOR-like cross-tenant consequences that are easy to overlook during standard testing.

[Read original article](https://labs.cognisys.group/posts/Breaking-Tenant-Boundaries-When-Path-Traversal-Isn't-About-the-Filesystem/){: .btn .btn-primary }
