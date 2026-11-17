---
layout: post
title: "OAuth 2.0 Browser Swapping Attacks Revisited: Response Mode Fragment"
date: 2026-11-17 05:00:00 +0300
categories: [RSS]
tags: [oauth, csrf, browser-swapping, authentication]
toc: true
---

SySS extends their OAuth 2.0 browser swapping attack research to show that using 'fragment' response mode (URI hash) does not prevent the attack. While fragments are not transmitted to servers, they survive browser redirects and persist in error page URLs shown to victims. Attackers can still extract authorization codes and state from these error URLs via social engineering, then replay them to their own session. The attack relies on the same mechanism as the original browser swapping technique but is slightly harder to execute since fragments are rarely logged. Recommended mitigations include short authorization code lifetimes (10 seconds) and explicitly clearing fragments on error redirects with a trailing hash.

[Read original article](https://blog.syss.com/posts/browser-swapping-fragment/){: .btn .btn-primary }
