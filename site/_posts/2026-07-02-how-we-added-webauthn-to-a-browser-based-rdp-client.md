---
layout: post
title: "How We Added WebAuthn to a Browser-Based RDP Client"
date: 2026-07-02 22:00:39 +0300
categories: [RSS]
tags: [webauthn, browser-security, rdp, reverse-engineering, authentication]
toc: true
---

Palo Alto Networks built WebAuthn redirection support for a browser-based RDP client by reverse-engineering the undocumented MS-RDPEWA protocol and overcoming browser API limitations. The core challenge: navigator.credentials.create() recomputes clientDataJSON with the browser's own origin (chrome-extension://...), causing hash and signature mismatches when a remote Okta server expects the original website's origin. The solution wraps Chromium's native FIDO2 stack with a custom extension API that accepts a pre-computed clientDataHash directly, bypassing the standard browser flow to support USB keys, Touch ID, Windows Hello, and phone-as-authenticator over caBLE/Hybrid. Implementation required reverse-engineering Windows internals (webauthn.dll calling patterns) and discovering that older Windows servers send only the hash—no cleartext challenge or origin—making traditional clientDataJSON reconstruction impossible.

[Read original article](https://unit42.paloaltonetworks.com/webauthn-added-to-browser-based-rdp/){: .btn .btn-primary }
