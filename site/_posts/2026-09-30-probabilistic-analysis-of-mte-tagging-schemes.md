---
layout: post
title: "Probabilistic analysis of MTE tagging schemes"
date: 2026-09-30 22:00:00 +0300
categories: [RSS]
tags: [memory-safety, use-after-free, defense, mobile, mte]
toc: true
---

This article analyzes probabilistic tag collision rates across different Memory Tagging Extension (MTE) schemes used in memory allocators. MTE, deployed on Android and iOS, associates 4-bit tags with memory allocations to detect use-after-free; when a stale pointer with a mismatched tag is dereferenced, access fails. The author performs probabilistic analysis comparing random tag assignment (7.1–8.3% per-reuse collision risk) against a proposed cyclic scheme (guaranteed 100% collision every 13–15 allocations), demonstrating mathematically why random selection is superior for hardened_malloc. The analysis factors in neighbor tag exclusions, quarantine behavior, and attacker-influenced allocation cycles, concluding that randomization is more robust than deterministic cycling for systems that cannot guarantee bounded allocation counts.

[Read original article](https://dustri.org/b/probabilistic-analysis-of-mte-tagging-schemes.html){: .btn .btn-primary }
