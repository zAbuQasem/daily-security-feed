---
layout: post
title: "From prompt to pwned: chaining LLM and web bugs to Admin"
date: 2026-06-04 22:00:00 +0300
categories: [RSS]
tags: [llm, xss, authentication, vulnerability-chain, web]
toc: true
---

Quarkslab demonstrates a real-world attack chain combining insecure LLM output handling with web vulnerabilities to achieve admin account takeover from a low-privileged account. By crafting prompts that trick the LLM into reflecting unsanitized JavaScript, the attacker injects XSS via markdown and iframe elements in the chat interface. The unprotected JWT cookie (missing HttpOnly, Secure, and SameSite flags) becomes accessible, enabling session hijacking. The attack exploits three distinct vulnerability classes—prompt manipulation, insecure output handling, and weak token implementation—to escalate from user to admin, and was validated on a real production system during a red team engagement.

[Read original article](http://blog.quarkslab.com/from-prompt-to-pwned-chaining-llm-and-web-bugs-to-admin.html){: .btn .btn-primary }
