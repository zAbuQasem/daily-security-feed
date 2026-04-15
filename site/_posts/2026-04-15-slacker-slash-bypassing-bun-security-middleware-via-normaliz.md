---
layout: post
title: "Slacker Slash: Bypassing Bun Security Middleware via Normalization Desync"
date: 2026-04-15 03:12:36 +0300
categories: [RSS]
tags: [bun, path-traversal, middleware-bypass, url-parsing, filesystem]
toc: true
---

The article describes a path validation bypass in Bun applications caused by a normalization desync between WHATWG URL parsing and Node/POSIX path utilities. Bun preserves multiple leading slashes in `new URL(req.url).pathname` and converts backslashes to forward slashes, so middleware checks like `path.startsWith("/admin")` can miss inputs such as `//admin_secret.txt` or `\admin_secret.txt` even though `path.join()` later collapses them into a valid filesystem path and serves the protected file. It also highlights a second bug pattern where developers validate access with `normalized.startsWith(ROOT)`, allowing sibling-directory escapes like `../public_backup/config.txt` because the resulting absolute path still shares the `public` prefix as a raw string. The practical impact is file disclosure or authorization bypass in Bun handlers that rely on string-based path guards instead of segment-aware checks such as `path.relative()` or root paths terminated with a separator.

[Read original article](https://lab.ctbb.show/research/bun-slacker-slash){: .btn .btn-primary }
