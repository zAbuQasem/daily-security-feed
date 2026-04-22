---
layout: post
title: "Some notes on the security properties of the pipe_buffer kernel object"
date: 2026-04-22 03:12:33 +0300
categories: [RSS]
tags: [linux-kernel, kernel-exploitation, pipe-buffer, dirty-pipe, heap-spray]
toc: true
---

This post analyzes how Linux's `pipe_buffer` object can be turned into multiple kernel exploit primitives by corrupting specific fields: `flags` for Dirty Pipe-style writes to read-only files, `ops` for kernel control-flow hijacking, and `page`/`offset`/`len` for arbitrary kernel read-write. The author also notes that partially overwriting the `page` pointer can retarget a pipe to another pipe's page and enable page-level use-after-free patterns similar to PageJack. A key practical finding is that large-scale pipe spraying changes behavior after roughly 1024 pipes, where `alloc_pipe_info()` starts creating new pipes with a default capacity of 8192 bytes instead of 65536 because of the per-user soft pipe-buffer quota enforced by `too_many_pipe_buffers_soft()`. That quota-driven size reduction changes which slab caches the `pipe_buffer` arrays land in, which matters directly for heap hole-filling, cross-cache attacks, and reliable Linux kernel LPE exploit development.

[Read original article](https://a13xp0p0v.tech/2026/04/20/pipe-buffer-experiments.html){: .btn .btn-primary }
