---
layout: post
title: "One Tap Too Far: Using Shortcuts to Bypass Chrome for iOS Call Prompts"
date: 2026-09-23 22:00:00 +0300
categories: [RSS]
tags: [bypass, ios, chrome, cve]
toc: true
---

Chrome for iOS allowed webpages to bypass app-launch confirmation policies by chaining through the native Shortcuts app's x-callback-url mechanism, enabling unauthorized tel: or facetime: URL initiations without user consent. A malicious link to shortcuts://run-shortcut?x-error=tel://NUMBER would bypass Chrome's app-launch alert (treating Shortcuts as trusted), then Shortcuts would open the tel: callback without Chrome's re-validation or gesture requirement. Although Chrome guards direct tel: URLs by requiring explicit user interaction, it has no visibility into Shortcuts callback chains, allowing a single click to trigger phone calls. Assigned CVE-2026-13795, the fix adds a confirmation prompt before opening any Shortcuts or legacy Workflow URLs, ensuring explicit user consent before callbacks execute.

[Read original article](https://blog.doyensec.com/2026/09/24/chrome-ios-policy-bypass.html){: .btn .btn-primary }
