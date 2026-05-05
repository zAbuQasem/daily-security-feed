---
layout: post
title: "Redis array type: short story of a long development"
date: 2026-05-04 14:21:45 +0300
categories: [RSS]
tags: [redis, regex, dos, data-structures, performance]
toc: true
---

Antirez describes the four-month design and implementation of a new Redis Array type, focusing on a sparse array representation that can handle very large numeric indexes without huge allocations. The final design uses a shape-shifting hierarchy of super-directories, dense directories, and 4096-element slices so operations like ARSET, ARSCAN, and ARPOP scale with existing elements rather than the span of the index space. The post also covers ARGREP, a new array-search capability built around the TRE regex library specifically because it avoids pathological time and space behavior from hostile regular expressions; Antirez says he then optimized TRE for common alternation cases like `foo|bar|zap` and fixed some potential security issues. It is primarily an implementation deep dive rather than a vuln write-up, but it is technically useful for readers interested in safe regex handling, memory-efficient data structures, and Redis internals.

[Read original article](http://antirez.com/news/164){: .btn .btn-primary }
