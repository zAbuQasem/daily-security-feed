---
layout: post
title: "BOF Cocktails in Cobalt Strike"
date: 2026-06-05 12:03:42 +0300
categories: [RSS]
tags: [cobalt-strike, postex, evasion, red-team]
toc: true
---

Rastamouse documents how to use the new BEACON_INLINE_EXECUTE hook introduced in Cobalt Strike 4.13 to instrument and modify BOFs (Beacon Object Files) before execution. The approach leverages Crystal Palace to transform BOFs through a specification file, enabling operators to inject hooks into system calls (e.g., ADVAPI32$OpenProcessToken) without modifying the original agent/loader. This allows merging evasion tradecraft directly into postex BOFs, improving their ability to evade detection by instrumenting API calls and monitoring activity in real-time before Beacon receives the modified code.

[Read original article](https://rastamouse.me/bof-cocktails-in-cobalt-strike/){: .btn .btn-primary }
