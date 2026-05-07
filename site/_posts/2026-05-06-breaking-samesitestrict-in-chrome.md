---
layout: post
title: "Breaking SameSite=Strict in Chrome"
date: 2026-05-06 00:00:00 +0300
categories: [RSS]
tags: [chrome, csrf, samesite, service-worker, browser-security]
toc: true
---

The article describes a Chrome bug that bypassed `SameSite=Strict` by abusing how DevTools re-fetched a cross-site POST response when a service worker was registered on the target origin. Opening DevTools caused the Inspector Resource Content Loader to issue a request with the invalid combination `RequestMode=kNoCors` and `FetchCacheMode=kOnlyIfCached`; when a service worker intercepted that fetch, the cache-only restriction was not enforced through the SW path. A bare `fetch(event.request)` from the service worker then replayed the original POST from the target origin’s context, causing authenticated `SameSite=Strict` cookies to attach and turning the flow into a working CSRF. Chromium fixed the issue in `inspector_resource_content_loader.cc` by forcing `kSameOrigin` with `kOnlyIfCached`, preventing the service worker from converting the refetch into a real network request with credentials.

[Read original article](https://lab.ctbb.show/writeups/breaking-samesite-strict-in-chrome){: .btn .btn-primary }
