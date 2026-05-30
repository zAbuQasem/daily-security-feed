---
layout: post
title: "ChatGPhish: The Page Is the Payload"
date: 2026-05-29 11:51:15 +0300
categories: [RSS]
tags: [prompt-injection, llm, phishing, markdown, ui-redress]
toc: true
---

Permiso researchers demonstrate a prompt injection attack against ChatGPT's browser-based page summarization feature (tested via Firefox), where attacker-controlled content embedded in any publicly accessible webpage — GitHub READMEs, blog posts, documentation — is passed to the model and rendered as trusted assistant output. The ChatGPT renderer auto-fetches Markdown image URLs from third-party origins, enabling passive IP/UA/Referer beaconing, while attacker-crafted Markdown links are displayed as live, unlabeled clickable elements inside the ChatGPT UI with no origin attribution. A demonstrated payload appends instruction-override text to a page that coerces the assistant to append a fake account security alert with an attacker-controlled phishing URL. A second variant abuses image auto-rendering to inject an inline QR code served from an attacker S3 bucket, bypassing desktop URL defenses (hover preview, blocklists, password manager domain checks) by moving the victim to a mobile context where the destination is hidden until after scanning.

[Read original article](https://permiso.io/blog/chatgpt-markdown-rendering-vulnerability){: .btn .btn-primary }
