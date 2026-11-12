---
layout: post
title: "Who needs permissions and the orange dot that never lit"
date: 2026-11-09 06:00:00 +0300
categories: [RSS]
tags: [macos, ios, permission-bypass, privilege-escalation, audio]
toc: true
---

Apple's `audiomxd` audio daemon trusted an audit token supplied by the client app instead of validating the kernel-supplied token, allowing a sandboxed app to forge a token impersonating the daemon itself. This bypassed TCC permission checks and enabled microphone recording even after permission denial, without permission prompts on subsequent launches or an orange indicator. The vulnerability affected iOS 26, iPadOS 26, and macOS Tahoe, exploiting a fundamental design error where accepting app-supplied audit tokens circumvented permission enforcement. Apple patched it in iOS 27.0 beta 5, iOS 26.6.1/iPadOS 26.6.1, and macOS Tahoe 26.6.2 with improved token validation. This CVE exemplifies a recurring class of vulnerability in daemon-app boundaries where trusting untrusted identity sources defeats security boundaries.

[Read original article](https://rtx.meta.security/exploitation/2026/11/09/CVE-2026-65339.html){: .btn .btn-primary }
