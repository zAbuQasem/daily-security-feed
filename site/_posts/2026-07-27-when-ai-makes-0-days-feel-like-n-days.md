---
layout: post
title: "When AI Makes 0-Days Feel Like N-Days"
date: 2026-07-27 00:00:00 +0300
categories: [RSS]
tags: [kernel, race-condition, lpe, 0-day, uaf]
toc: true
---

A lock-mismatch vulnerability in the Linux kernel's net/sched subsystem creates a race condition in tcf_idr_check_alloc(): action lookup is performed under only RCU read-lock while actions are freed with rtnl_lock and idrinfo->lock without waiting for RCU grace period, enabling use-after-free. By exploiting the narrow race window between idr_find and refcount_inc_not_zero, an attacker can trigger the UAF through netlink operations (RTM_NEWTFILTER/RTM_DELTFILTER) without requiring CAP_NET_ADMIN in the init namespace. The author developed an LPE exploit optimized for CentOS 9 desktop using timerfd/epoll-based window-widening techniques to reliably hit the race. Additionally, two other exploitable bugs were discovered in kernel/events/core.c, demonstrating active 0-day research.

[Read original article](https://starlabs.sg/blog/2026/07-when-ai-makes-0-days-feel-like-n-days/){: .btn .btn-primary }
