---
layout: post
title: "ClearFake WebDAV infection chain delivers Amatera stealer, ZigCryptoStealer, and NetSupport Manager"
date: 2026-09-08 10:01:07 +0300
categories: [RSS]
tags: [malware, stealer, webdav, supply-chain, clickfix]
toc: true
---

Cisco Talos documented a sophisticated multi-stage WebDAV-based malware distribution chain that combines Cloudflare Workers for JavaScript injection, BNB Smart Chain (EtherHiding) for bulletproof payload hosting, and fake Google CAPTCHA ClickFix social engineering to deliver Amatera stealer and secondary payloads. The chain executes malicious DLLs via WebDAV UNC paths and rundll32.exe ordinal execution, with secondary payloads including ZigCryptoStealer (delivered via signed Chrome DLL side-loading to evade EDR), a Go-based reverse TCP proxy, and NetSupport Manager RAT. Observed targeting a Ukrainian government organization with infrastructure suggesting Russian threat actor involvement (UAT-10820). The technique chains novel evasion primitives—blockchain-backed code storage, Cloudflare infrastructure abuse, and legitimate application side-loading—in a highly orchestrated attack demonstrating significant sophistication.

[Read original article](https://blog.talosintelligence.com/clearfake-webdav-infection-chain/){: .btn .btn-primary }
