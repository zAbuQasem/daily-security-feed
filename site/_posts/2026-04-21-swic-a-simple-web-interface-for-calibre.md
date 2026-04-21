---
layout: post
title: "swic: a simple web interface for calibre"
date: 2026-04-21 03:12:30 +0300
categories: [RSS]
tags: [tooling, hardening, go, path-traversal, attack-surface]
toc: true
---

The post introduces `swic`, a minimal Go-based replacement for calibre-web that the author wrote after submitting 17 security-related pull requests to calibre-web and deciding its feature set created too much audit and maintenance burden. The security angle is attack-surface reduction: `swic` only lists ebooks, supports search, and serves downloads, with no user-management layer, no write access requirements, no JavaScript frontend, and just one direct dependency (`modernc.org/sqlite`) to read Calibre's SQLite database. The author explicitly uses Go's `os.Root` API to constrain filesystem access and mitigate path traversal when handling user-provided URLs. This is not a vulnerability write-up, but it is a technically relevant secure-by-design tool release showing how aggressively removing features and dependencies can reduce the likelihood of web-exposed RCE and related bugs in self-hosted ebook services.

[Read original article](https://dustri.org/b/swic-a-simple-web-interface-for-calibre.html){: .btn .btn-primary }
