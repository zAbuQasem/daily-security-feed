---
layout: post
title: "Race Against the (Mac)hine: Local Privilege Escalation in Microsoft Defender for macOS"
date: 2026-11-15 12:00:00 +0300
categories: [RSS]
tags: [lpe, macos, edr, race-condition, ipc]
toc: true
---

Two local privilege escalation vulnerabilities in Microsoft Defender for macOS (CVE-2026-50657 for arbitrary file read/information disclosure and CVE-2026-50658 for TOCTOU race condition) exploit subtle differences in macOS security APIs compared to Windows. The vulnerabilities are cross-platform variants of Windows Defender CVEs (CVE-2026-33825 "BlueHammer" and CVE-2026-41091) that were patched on Windows but remain exploitable on macOS due to architectural differences and how authorization, code signing, and peer identity validation work differently. The root cause involves improper IPC peer identity verification—relying on cached process IDs without accounting for `execve()` re-execution, whereas macOS audit tokens bind credentials to both the process *and* a pidversion counter invalidated on re-exec. This research demonstrates that cross-platform variant analysis can reveal significant regressions where mitigations effective on one OS fail on another.

[Read original article](https://spaceraccoon.dev/race-against-the-machine-defender-macos-lpe/){: .btn .btn-primary }
