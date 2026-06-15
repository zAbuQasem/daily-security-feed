---
layout: post
title: "FridaNamedPipesHooks - Transitioning to Nt* syscall stubs"
date: 2026-06-14 20:00:00 +0300
categories: [RSS]
tags: [windows, frida, ipc, syscalls, debugging]
toc: true
---

FridaNamedPipesHooks is a Frida-based tool that hooks Windows API functions to intercept and analyze named pipe communications for IPC debugging and security analysis. The update extends hook coverage to lower-level syscall stubs (NtReadFile, NtWriteFile, NtCreateFile, NtCreateNamedPipeFile) in ntdll.dll, catching IPC traffic that bypasses standard kernel32.dll ReadFile/WriteFile APIs. This addresses a gap discovered during Windows internals analysis where .NET code uses System.IO.Pipes.PipeStream.WriteFileNative, which directly invokes ntdll stubs. The expanded syscall-level hooking provides comprehensive named pipe interception for scenarios where applications bypass the higher-level API surface.

[Read original article](https://malacupa.com/2026/06/14/frida-named-pipes-hooks-syscalls.html){: .btn .btn-primary }
