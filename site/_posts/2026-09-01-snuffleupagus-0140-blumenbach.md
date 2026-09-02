---
layout: post
title: "Snuffleupagus 0.14.0 - Blumenbach"
date: 2026-09-01 12:30:00 +0300
categories: [RSS]
tags: [php, defensive, tool-release, opcache, bypass]
toc: true
---

Snuffleupagus 0.14.0 release includes a critical fix for PHP 8.5's opcache optimizer, which inline-optimizes trivial constant-return functions, bypassing Snuffleupagus's `zend_execute_ex` hooks that enforce return-value security rules. The fix uses the `op_array_handler` callback during pre-optimization compilation to set `ZEND_ACC_HAS_TYPE_HINTS` on ruled functions, preventing inlining without runtime cost. The release also addresses a 2x WordPress slowdown caused by chained `disable_function` rules by moving them to per-function hashtables keyed by innermost function, plus multiple security fixes (type confusion, null-pointer dereference in cookie encryption, unserialization truncation), and improved PHP 8.5 compatibility.

[Read original article](https://dustri.org/b/snuffleupagus-0140-blumenbach.html){: .btn .btn-primary }
