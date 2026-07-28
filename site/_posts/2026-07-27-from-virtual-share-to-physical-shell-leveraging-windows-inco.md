---
layout: post
title: "From Virtual Share to Physical Shell: Leveraging Windows’ Inconsistent Access Control for LPE"
date: 2026-07-27 15:02:32 +0300
categories: [RSS]
tags: [lpe, windows, kernel, cve, access-control]
toc: true
---

Two improper access control vulnerabilities in the Windows storvsp.sys kernel driver (CVE-2025-59517 and CVE-2025-64673) allow local privilege escalation to SYSTEM on Windows systems with Virtual Machine Platform enabled. CVE-2025-59517 enables a low-privileged user to open a vSMB share handle to arbitrary directories (e.g., C:\Windows\System32) by bypassing NTFS ACL checks in VspVsmbFileCreate() due to missing security flags passed to IoCreateFileEx(). CVE-2025-64673 in VspVsmbHandleSetInformationFileRequest() then performs file operations with SYSTEM privileges when the share lacks write access, enabling an attacker to relocate arbitrary files. By chaining these primitives, an attacker can plant a malicious DLL in System32, invoke a COM interface to load it as SYSTEM, and gain shell access—demonstrated with reverse-engineered structures and control flow analysis.

[Read original article](https://blog.exodusintel.com/2026/07/27/from-virtual-share-to-physical-shell-leveraging-windows-inconsistent-access-control-for-lpe/){: .btn .btn-primary }
