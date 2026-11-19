---
layout: post
title: "NGINX HTTP/2 Vulnerabilities: How to Identify Affected Images and Apply Security Updates"
date: 2026-11-18 23:43:24 +0300
categories: [RSS]
tags: [nginx, http2, rce, cve, kubernetes]
toc: true
---

Two critical vulnerabilities in NGINX's HTTP/2 implementation (CVE-2026-123633 and CVE-2026-123007, CVSS 9.2) enable unauthenticated remote code execution on affected servers. CVE-2026-123633 requires HTTP/2 enabled, proxying to a backend, and low connection availability; CVE-2026-123007 requires only HTTP/2. Affected versions: NGINX Open Source 1.19.7–1.30.6 and 1.31.0–1.31.8; NGINX Plus R33–R36 and affected 37.x releases. Fixes: upgrade to 1.30.7/1.31.9 (Open Source) or 37.0.7.1/37.2.0.1+ (Plus). The article provides practical remediation for web servers, reverse proxies, and Kubernetes ingress deployments, including mitigation via disabling HTTP/2 if patching is delayed.

[Read original article](https://www.aquasec.com/blog/nginx-http2-vulnerabilities-affected-images/){: .btn .btn-primary }
