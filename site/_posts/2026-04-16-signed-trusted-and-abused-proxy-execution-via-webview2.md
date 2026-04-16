---
layout: post
title: "Signed, Trusted, and Abused: Proxy Execution via WebView2"
date: 2026-04-16 03:12:36 +0300
categories: [RSS]
tags: [windows, webview2, dll-sideloading, persistence, applocker]
toc: true
---

The article describes a proxy-execution technique against Microsoft Edge WebView2 Runtime in which trusted Windows Apps such as Teams, Outlook, and other Store-style apps spawn msedgewebview2.exe, which in turn loads domain_actions.dll from locations under %LocalAppData%. Because that DLL can reside in a user-writable path outside the app container, an attacker can replace it with a malicious proxy DLL that forwards legitimate exports to a renamed original copy (for example, domain_actions-old.dll) while running arbitrary payload code first. The write-up shows this working with both a simple Rust proof of concept and Cobalt Strike shellcode, turning WebView2 into a practical code-execution and persistence primitive on systems where these apps run continuously. The practical impact is that a Microsoft-signed, required runtime component can be abused to sideload code through trusted application launches, potentially weakening allow-listing controls such as AppLocker and reducing defender visibility inside sandboxed app containers.

[Read original article](https://www.blackhillsinfosec.com/proxy-execution-via-webview2/){: .btn .btn-primary }
