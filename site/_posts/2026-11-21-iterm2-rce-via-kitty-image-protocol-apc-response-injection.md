---
layout: post
title: "iTerm2 RCE via Kitty Image Protocol APC Response Injection"
date: 2026-11-21 00:00:00 +0300
categories: [RSS]
tags: [rce, iterm2, injection, parser-bug, escape-sequence]
toc: true
---

iTerm2 versions prior to 3.7.9 contain a remote code execution vulnerability in the Kitty image protocol implementation. Three logic bugs combine into a complete exploit chain: (1) the APC escape sequence handler lacks the `terminalIsTrusted` check present in OSC handlers, allowing untrusted input to be processed; (2) the Kitty file transmit error path preserves literal newlines (0x0A) from crafted filenames in `NSError.localizedDescription` without escaping them; (3) the error response is unconditionally written to PTY stdin, where the shell interprets newlines as command separators. An attacker can embed an APC sequence with a base64-encoded filename containing newlines into any file, triggering arbitrary command execution when the file is viewed with `cat` or similar. The vulnerability is 100% reproducible on default installations and affects all shells (bash, zsh, fish).

[Read original article](https://ii4gsp.github.io/iterm2-rce/){: .btn .btn-primary }
