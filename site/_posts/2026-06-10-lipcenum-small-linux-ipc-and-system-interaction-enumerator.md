---
layout: post
title: "lipcenum - small Linux IPC and system interaction enumerator"
date: 2026-06-10 20:00:00 +0300
categories: [RSS]
tags: [linux, enumeration, ipc, tooling, analysis]
toc: true
---

lipcenum is a pure-Python 3.7+ tool for enumerating Inter-Process Communication (IPC) mechanisms and system interactions on Linux by parsing the `/proc` filesystem. It identifies pipes, network sockets (TCP/UDP), UNIX domain sockets, file descriptors, and anonymous inodes (eventfd, epoll, timerfd) associated with a target process. The tool requires no compilation and depends only on Python standard library, making it easy to deploy in restricted or minimal environments. It supports JSON output for integration with other tools, providing a lightweight alternative to heavier solutions like IPCDump or Procmon-for-Linux.

[Read original article](https://malacupa.com/2026/06/10/lipcenum.html){: .btn .btn-primary }
