---
layout: post
title: "Design-Based Vulnerabilities on macOS： Oops, Not a One-Shot Fix"
date: 2026-05-15 00:00:00 +0300
categories: [RSS]
tags: [macos, tcc, sip, pkg, persistence]
toc: true
---

This write-up examines macOS design-level security flaws that can be chained into more serious outcomes than a standalone userland root bug, focusing on how TCC and SIP remain the real security boundaries after root compromise. A central example is the PKG installation path: PackageKit's `package_script_service` runs `preinstall` and `postinstall` scripts as root and carries the `com.apple.private.security.storage.InstallerSandboxes` entitlement, which grants access to the `/Library/InstallerSandboxes/` Data Vault. The article argues that these installer semantics, notarization assumptions, and privileged entitlements can be combined into full TCC bypass and persistence rather than treated as isolated bugs with one-off patches. The practical takeaway is that macOS design flaws often live in the interaction between protections, where a malicious or abused installer flow can become a stepping stone from root execution to broader access to protected user data and longer-term compromise.

[Read original article](https://imlzq.com/apple/macos/2026/05/15/Design-Based-Vulnerabilities-on-macOS-Oops-Not-a-One-Shot-Fix.html){: .btn .btn-primary }
