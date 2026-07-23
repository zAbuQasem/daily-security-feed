---
layout: post
title: "Intercepting Android WebView traffic under new certificate validity requirement by Chromium"
date: 2026-07-22 14:08:17 +0300
categories: [RSS]
tags: [tls, chromium, webview, android, certificates]
toc: true
---

Chromium now strictly enforces maximum certificate validity periods for leaf certificates, validated in the HasTooLongValidity function. For certificates issued after March 15, 2026, the limit is 200 days; after March 15, 2027, it drops to 100 days. When certificates exceed these limits, Chromium rejects them with error -213 (CERT_VALIDITY_TOO_LONG), causing WebView to fail TLS negotiation. This breaks HTTPS interception on Android devices with updated WebView versions, since tools like Burp Suite generate certificates with validity periods longer than 200 days. The article includes detailed code analysis from Chromium's cert verification logic and explains the historical progression of these limits per CA/Browser Forum Baseline Requirements.

[Read original article](https://blog.nviso.eu/2026/07/22/intercepting-android-webview-traffic-under-new-certificate-validity-requirement-by-chromium/){: .btn .btn-primary }
