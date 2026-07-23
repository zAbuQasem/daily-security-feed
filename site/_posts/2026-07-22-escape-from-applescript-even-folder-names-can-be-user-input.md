---
layout: post
title: "Escape from AppleScript: Even folder names can be user input"
date: 2026-07-22 13:00:00 +0300
categories: [RSS]
tags: [applescript-injection, macos, rce, escaping-bypass]
toc: true
---

SonarSource discovered an AppleScript injection vulnerability in OpenInTerminal, a macOS utility for opening directories in terminals. The vulnerability stems from insufficient escaping of folder path names when constructing AppleScript `do shell script` commands; while quotes are escaped for shell context, they remain unescaped for AppleScript, allowing an attacker to break out of the string and inject arbitrary AppleScript code. The exploitation technique bypasses character restrictions by encoding commands as ASCII character arrays (e.g., `ASCII character 105`) and splitting long payloads across nested folder names, using line comments to hide path separators from the AppleScript interpreter. A victim needs only to attempt opening a maliciously-crafted folder via OpenInTerminal to achieve arbitrary code execution; the attack can be obscured with symlinks to minimize user interaction. The vulnerability was patched in v2.3.9 by replacing string-based command construction with structured argument passing and applying POSIX quoting to individual arguments rather than attempting sanitization.

[Read original article](https://www.sonarsource.com/blog/escape-from-applescript/){: .btn .btn-primary }
