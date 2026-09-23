---
layout: post
title: "How One Twitch Chat Message Became Code Execution on a Streamer’s PC"
date: 2026-09-22 07:06:37 +0300
categories: [RSS]
tags: [rce, xss, v8, chromium, cve-2024-7971]
toc: true
---

A complete exploit chain converts a single Twitch chat message into arbitrary code execution on a streamer's PC. The vulnerability combines three elements: unsanitized HTML rendering of viewer messages in a chat overlay (XSS), OBS's default disabling of the Chromium sandbox in its embedded CEF browser, and CVE-2024-7971, a V8 type confusion bug already exploited in the wild by North Korean threat actor Citrine Sleet. The researcher built a working proof of concept targeting OBS 32.2.2 with Chromium 127.0.6533.120, demonstrating how JavaScript execution from XSS escalates via V8 exploitation to native code execution without user interaction or configuration changes. The attack surface is broad: any OBS Browser Source rendering untrusted web content (chat overlays, donation alerts, widgets) becomes an entry point.

[Read original article](https://blog.scrt.ch/2026/09/22/how-one-twitch-chat-message-became-code-execution-on-a-streamers-pc/){: .btn .btn-primary }
