---
layout: post
title: "C/C++ checklist challenges, solved"
date: 2026-05-05 11:00:00 +0300
categories: [RSS]
tags: [c-cpp, windows-driver, command-injection, type-confusion, kernel]
toc: true
---

Trail of Bits walks through two C/C++ bug patterns from its testing handbook: a Linux ping utility that is reachable for command injection, and a Windows WDF driver handler that can be turned into a registry-driven kernel memory corruption bug. In the Linux sample, exploitation relies on `inet_aton()` accepting trailing garbage and `inet_ntoa()` returning a pointer to a shared static buffer, letting an attacker bypass the localhost comparison and reach `system("ping '%s'")` with injected shell metacharacters. In the Windows sample, the driver trusts an attacker-supplied absolute registry path and reads values with `RtlQueryRegistryValues` using `RTL_QUERY_REGISTRY_DIRECT` but without `RTL_QUERY_REGISTRY_TYPECHECK`, enabling type confusion when a controlled registry value is interpreted as an integer version field. The article frames this as escalating from a local denial of service into a kernel write primitive, making it a useful case study in unsafe API contracts, static-buffer footguns, and registry parsing mistakes in privileged C/C++ code.

[Read original article](https://blog.trailofbits.com/2026/05/05/c/c-checklist-challenges-solved/){: .btn .btn-primary }
