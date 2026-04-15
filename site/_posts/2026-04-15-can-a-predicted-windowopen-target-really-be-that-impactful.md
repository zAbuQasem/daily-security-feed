---
layout: post
title: "Can a Predicted `window.open` Target Really Be That Impactful?"
date: 2026-04-15 03:12:37 +0300
categories: [RSS]
tags: [oauth, postmessage, iframe-hijacking, web, pii]
toc: true
---

The article describes an OAuth popup hijack caused by a hardcoded `window.open(..., "addons-oauthWindow")` target in an addons-linking flow, which lets an attacker pre-create a browsing context with the same name and capture the authorization window inside an attacker-controlled iframe. Because the application only validated `postMessage` events using the parsed `redirect_uri` origin and `n.source === k`, the named iframe collision let the attacker satisfy the expected window reference and interfere with the trusted popup relationship. In the demonstrated exploit, a victim could be tricked into authorizing an attacker-controlled marketplace addon against their workspace, leading to exposure of workspace owner identity data and configuration details returned during the OAuth completion flow. The write-up is useful because it shows how predictable popup names, opener messaging, and origin/source checks can combine into a practical iframe-based account-linking attack even when the flow appears to have postMessage validation.

[Read original article](https://lab.ctbb.show/research/can-a-predicted-window-open-target-really-be-that-impactful){: .btn .btn-primary }
