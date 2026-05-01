---
layout: post
title: "That AI Extension Helping You Write Emails? It’s Reading Them First"
date: 2026-04-30 22:00:57 +0300
categories: [RSS]
tags: [browser-extensions, genai, infostealer, mitm, threat-intel]
toc: true
---

Unit 42 analyzed 18 malicious browser extensions posing as AI productivity tools and found they abused extension privileges to steal sensitive data, including email drafts, ChatGPT prompts, passwords, and browser session material. The samples used several technically meaningful mechanisms: hooking page-level APIs such as window.fetch and XMLHttpRequest before encryption, passively scraping rendered DOM content from sites like Gmail or Notion, reconfiguring traffic through attacker-controlled proxy infrastructure, and attaching to the Chrome Debugger Protocol to access decrypted HTTPS responses. The report also highlights persistence and control tradecraft specific to extensions, including WebSocket-based C2, identifier replication across chrome.storage.sync, cookies, and localStorage, and payload execution via chrome.runtime.onInstalled. The practical takeaway is that AI-branded extensions meaningfully expand the client-side attack surface because broad browser permissions let attackers capture higher-value data than normal browsing telemetry, especially prompts, proprietary text, and authenticated session context.

[Read original article](https://unit42.paloaltonetworks.com/high-risk-gen-ai-browser-extensions/){: .btn .btn-primary }
