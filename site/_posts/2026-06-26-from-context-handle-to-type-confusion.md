---
layout: post
title: "From context_handle to type confusion"
date: 2026-06-26 02:27:16 +0300
categories: [RSS]
tags: [windows, rpc, type-confusion, cve, reverse-engineering]
toc: true
---

A type confusion vulnerability pattern affecting Windows RPC servers arises from insufficient constraints in IDL definitions and lack of validation of context-handle types. The author discovered that RPC context handles marked as FC_BINDING_CONTEXT (0x70) bypass validation during unmarshalling, unlike FC_SUPPLEMENT types (0x75), allowing an attacker to pass one context-handle type into an interface expecting another. In ssdpsrv, passing a CONTEXT_HANDLE into a SYNC_HANDLE interface enables arbitrary handle closure via reference-count manipulation (CVE-2025-48815). The same pattern was identified in message queuing (MQQM, CVE-2025-53143) and firewall (fwbase, CVE-2025-54104) RPC servers, demonstrating a systemic vulnerability class across Windows infrastructure components. The research includes reverse-engineering of rpcrt4.dll and practical exploitation techniques using James Forshaw's NtObjectManager to identify vulnerable RPC servers.

[Read original article](https://whereisk0shl.top/post/From%20context_handle%20to%20type%20confusion/){: .btn .btn-primary }
