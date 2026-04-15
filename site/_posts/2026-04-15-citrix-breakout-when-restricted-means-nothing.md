---
layout: post
title: "Citrix Breakout When Restricted Means Nothing"
date: 2026-04-15 03:12:17 +0300
categories: [RSS]
tags: [citrix, windows, application-whitelisting, powershell, evasion]
toc: true
---

Cognisys shows a Citrix breakout in a locked-down Windows desktop where direct launches of `cmd.exe` and `powershell.exe` were blocked, but `.bat` files were still executable. That gap allowed the team to run batch commands for local and domain enumeration, then generate a VBScript in `%temp%` that used `CreateObject("WScript.Shell")` to spawn `powershell.exe -NoExit` via `wscript.exe`. The bypass worked because the policy focused on blocking the target binary rather than restricting trusted script hosts and child-process creation paths, so PowerShell could be brokered through an allowed Windows component. It is a practical write-up on application-whitelisting weakness in Citrix-style restricted environments: no memory corruption or 0-day is needed, just incomplete control over batch files, VBScript, and native scripting engines.

[Read original article](https://labs.cognisys.group/posts/Citrix-Breakout-When-Restricted-Means-Nothing/){: .btn .btn-primary }
