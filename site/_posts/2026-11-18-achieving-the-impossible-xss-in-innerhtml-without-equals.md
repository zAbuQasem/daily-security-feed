---
layout: post
title: "Achieving the impossible: XSS in innerHTML without equals"
date: 2026-11-18 14:39:45 +0300
categories: [RSS]
tags: [xss, html-parser, dom-based, bypass]
toc: true
---

Masato Kinugawa (PortSwigger Research) discovered a novel XSS vector that solves the previously "impossible" challenge of executing JavaScript in innerHTML assignments without using equals signs. The technique exploits the `<selectedcontent>` HTML element—which automatically clones the content of selected `<option>` elements into itself—combined with SVG `<script>` tag parsing to bypass the browser's prohibition on executing injected scripts. By nesting an SVG `<script>` tag within an `<option>` inside a `<select>`, attackers execute code without whitespace, forward slashes, or equals signs, constraints that made such attacks previously impossible. The vector works in Chrome 157 and Safari 27.2, demonstrating a genuinely novel attack primitive with broad applicability across modern web applications.

[Read original article](https://portswigger.net/research/achieving-the-impossible-xss-in-innerhtml-without-equals){: .btn .btn-primary }
