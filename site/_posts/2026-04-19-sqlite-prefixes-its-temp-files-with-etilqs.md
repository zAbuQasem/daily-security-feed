---
layout: post
title: "SQLite prefixes its temp files with `etilqs_`"
date: 2026-04-19 03:12:14 +0300
categories: [RSS]
tags: [sqlite, internals, temp-files, vacuum]
toc: true
---

This post documents a small but concrete SQLite implementation detail: temporary files created during operations like `VACUUM` are prefixed with `etilqs_`, which is simply `sqlite_` spelled backwards. `VACUUM` rebuilds the database into a fresh temporary file to reclaim free space and defragment pages, so the prefix appears in SQLite's temp-file creation path rather than in user-visible database names. The article cites the upstream `src/os.h` comment explaining that SQLite changed the default prefix in 2006 after McAfee-created temp files with `sqlite` in the name caused Windows users to misattribute those files to SQLite and contact the developers. It is mainly useful as implementation and debugging context for anyone studying SQLite-compatible engines or filesystem artifacts produced during database maintenance.

[Read original article](https://avi.im/blag/2026/etilqs/){: .btn .btn-primary }
