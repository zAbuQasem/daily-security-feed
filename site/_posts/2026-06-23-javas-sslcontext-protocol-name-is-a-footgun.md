---
layout: post
title: "Java’s SSLContext protocol name is a footgun"
date: 2026-06-23 20:12:31 +0300
categories: [RSS]
tags: [tls, java, configuration, downgrade, defensive]
toc: true
---

Java's SSLContext.getInstance('TLSv1.2') sets a maximum TLS version rather than a minimum, contrary to misleading documentation—the default SunJSSE provider (and others like Android's Conscrypt) enable silent protocol downgrades. Developers following security guidance to specify a version may inadvertently implement a self-inflicted downgrade attack, accepting TLS 1.0/1.1 when expecting 1.2/1.3. The issue is pervasive because security scanners recommend this practice. The workaround is using the generic 'TLS' identifier to get sensible modern defaults, though with no formal guarantee of behavior.

[Read original article](https://neilmadden.blog/2026/06/23/javas-sslcontext-protocol-name-is-a-footgun/){: .btn .btn-primary }
