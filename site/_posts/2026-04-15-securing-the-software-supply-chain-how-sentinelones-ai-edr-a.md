---
layout: post
title: "Securing the Software Supply Chain: How SentinelOne’s AI EDR Autonomously Blocked the CPU-Z Watering Hole Cyber Attack"
date: 2026-04-15 03:12:26 +0300
categories: [RSS]
tags: [supply-chain, malware, dll-sideloading, edr, stx-rat]
toc: true
---

This write-up covers a watering-hole compromise of CPUID's official download flow in which cpuid.com served legitimate signed CPU-Z packages bundled with a malicious `CRYPTBASE.dll`, turning the vendor's own infrastructure into the delivery vector. The payload chain relied on DLL side-loading and an in-memory reflective loader that decrypted a second-stage DLL with XXTEA and DEFLATE, allocated RWX memory, resolved APIs outside the normal loader path, and then injected follow-on code while spawning the abnormal chain `cpuz_x64.exe -> powershell.exe -> csc.exe -> cvtres.exe`. The final malware was STX RAT, which provided hidden VNC access, browser and Windows Vault credential theft, crypto wallet targeting, persistence via a Run key, long-lived scheduled task, and MSBuild project files under `AppData\Local`, plus C2 over an encrypted DNS-over-HTTPS channel to `1.1.1.1`. Although the post is vendor-authored, it contains meaningful technical detail on the intrusion mechanics and highlights a high-signal software supply chain compromise where trust in a signed binary and official distribution channel was insufficient.

[Read original article](https://www.sentinelone.com/blog/securing-the-software-supply-chain-how-sentinelones-ai-edr-autonomously-blocked-the-cpu-z-watering-hole-cyber-attack/){: .btn .btn-primary }
