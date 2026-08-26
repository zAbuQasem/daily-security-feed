---
layout: post
title: "What's in a tag name? JavaScript, apparently"
date: 2026-08-25 14:24:32 +0300
categories: [RSS]
tags: [xss, waf-bypass, parser, browser, exploit]
toc: true
---

PortSwigger Research reveals novel XSS vectors by exploiting browser parsing of HTML tag names. Browsers treat tag names leniently, allowing characters that get transformed in unexpected ways (e.g., `localName` property returns lowercase version). Researchers chained this with event handlers and JavaScript constructors to create multiple XSS payloads that work across all browsers and bypass WAF signatures—e.g., `<alert(1) onfocus="attributes[0].value=localName,new onfocus" autofocus tabindex=1>`. The technique exploits seemingly harmless properties like `part`, `classList`, and `contenteditable` to hide and execute payloads, demonstrating that browsers remain more permissive with HTML parsing than security practitioners expect.

[Read original article](https://portswigger.net/research/whats-in-a-tag-name-javascript-apparently){: .btn .btn-primary }
