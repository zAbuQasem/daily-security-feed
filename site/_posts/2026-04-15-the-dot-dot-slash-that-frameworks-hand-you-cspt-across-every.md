---
layout: post
title: "The Dot-Dot-Slash That Frameworks Hand You: CSPT Across Every Major Frontend Framework"
date: 2026-04-15 03:12:33 +0300
categories: [RSS]
tags: [path-traversal, frontend, csrf, xss, routing]
toc: true
---

This research maps the URL-decoding pipeline in eight major frontend frameworks and shows that dynamic route parameters can be transformed into client-side path traversal primitives before developers use them in `fetch()` calls. The core issue is that routers decode attacker-controlled path segments such as `%2F`, `%5C`, `%2E%2E`, and in some cases even double-encoded variants like `%252F`, then hand the application values like `../../admin` that are later interpolated into API endpoints. The React Router example highlights the pattern clearly: `decodePath()` percent-decodes segments and later `matchPath()` restores `%2F` to `/`, so a route like `/users/%2E%2E%2F%2E%2E%2Fadmin` can become `../../admin` inside `useParams()`, and a subsequent `fetch(`/api/users/${userId}/profile`)` is normalized by the browser into a different request path. The article is valuable because it goes beyond one bug instance and shows framework-specific exploitation paths across React, Next.js, Vue, Angular, SvelteKit, Nuxt, Ember, and SolidStart, making CSPT a reusable primitive for bypassing frontend route assumptions and chaining into CSRF, open redirect, upload-to-XSS, or secondary server-side traversal scenarios.

[Read original article](https://lab.ctbb.show/research/the-dot-dot-slash-that-frameworks-hand-you){: .btn .btn-primary }
