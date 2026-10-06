---
layout: post
title: "Smashing the token limit with overlapping fragments"
date: 2026-10-05 15:04:55 +0300
categories: [RSS]
tags: [css, token-exfiltration, graph-theory, web-security]
toc: true
---

PortSwigger Research demonstrates a significant advance in CSS-based token exfiltration by reconstructing tokens hundreds of characters long using overlapping fragment reconstruction. The technique models token recovery as a graph traversal problem: CSS selectors extract overlapping 2–6 character chunks from a target token, and a reconstruction algorithm finds valid paths from start to end fragments by checking which chunks appeared together in the URL. By strategically grouping CSS rules (using two-character checks for high-frequency patterns, three-character checks for medium, and selective four-character checks for confirmation), the authors reduced payload size from Gareth Heyes's original 257 MB down to 1.3 MB for 12-character tokens while achieving 640+ character extraction with the same budget — roughly 200× efficiency gain. This advance directly escalates the practical threat of CSS-based CSRF and email-based token theft attacks.

[Read original article](https://portswigger.net/research/smashing-the-token-limit){: .btn .btn-primary }
