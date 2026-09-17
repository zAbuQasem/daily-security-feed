---
layout: post
title: "Living Inside the Shell: zsh Modules on macOS"
date: 2026-09-16 17:58:20 +0300
categories: [RSS]
tags: [evasion, macos, shell, threat-hunting, detection]
toc: true
---

macOS zsh includes a module system providing networking, file manipulation, and extended-attribute access as shell builtins rather than separate processes. The `zsh/net/tcp` module exposes the `ztcp` builtin for raw TCP connections, enabling file-less script retrieval and execution via `/dev/fd/<n>` without spawning curl, wget, or nc. This approach evades process-based telemetry and forensic artifact detection while maintaining network connectivity. A working example demonstrates retrieving a second-stage payload through a socket and executing it directly within the zsh process, bypassing traditional detection mechanisms. The technique is limited to unencrypted connections due to lack of TLS support in zsh/net/tcp.

[Read original article](https://dfir.ch/posts/zsh_modules/){: .btn .btn-primary }
