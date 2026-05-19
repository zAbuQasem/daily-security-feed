---
layout: post
title: "SHub Reaper | macOS Stealer Spoofs Apple, Google, and Microsoft in a Single Attack Chain"
date: 2026-05-18 13:00:42 +0300
categories: [RSS]
tags: [macos, infostealer, applescript, social-engineering, malware]
toc: true
---

SentinelOne analyzes a new SHub Stealer variant, "Reaper," that delivers a macOS infostealer through fake WeChat and Miro installers while rotating its disguise across Apple, Microsoft, and Google branding during different stages of the infection chain. The campaign uses the applescript:// URL scheme to open Script Editor with a pre-populated malicious AppleScript, hiding the real payload below visible text and then invoking a base64-decoded curl | zsh command that fetches additional stages and executes the core AppleScript via osascript without writing it to disk. The malware checks com.apple.HIToolbox.plist for Russian input sources to avoid CIS victims, fingerprints visitors for IP, WebGL, VPN, VM, and installed wallet/password-manager extensions, and sends telemetry to operators through a hardcoded Telegram bot while using debugger traps and DevTools detection to frustrate analysis. On infected hosts it steals browser and wallet data, scrapes the user password to access decrypted credentials, and adds an AMOS-style file grabber that harvests documents, keys, spreadsheets, JSON, RDP files, and PNGs from Desktop and Documents under size limits, making it a useful case study in modern macOS stealer delivery and collection tradecraft.

[Read original article](https://www.sentinelone.com/blog/shub-reaper-macos-stealer-spoofs-apple-google-and-microsoft-in-a-single-attack-chain/){: .btn .btn-primary }
