---
layout: post
title: "Microsoft Windows Installer Folder Delete Privilege Escalation"
date: 2026-07-06 15:32:55 +0300
categories: [RSS]
tags: [privilege-escalation, windows, com, rce, cve]
toc: true
---

A logic vulnerability in the Windows Installer COM interface (CVE-2025-27727, patched April 2025) allows a low-privileged user to cause the MSI service (running as SYSTEM) to delete arbitrary folders by injecting paths into the TempPackages registry key via SetEEUIDirectoryAndFilter(). The MSI service lacks validation that TempPackages entries were created by the installer itself and blindly trusts this registry as authoritative, enumerating and deleting specified folders with SYSTEM privileges using LockdownPath to override ACLs. The vulnerability chains to arbitrary SYSTEM code execution by planting malicious rollback scripts in a recreated C:\Config.Msi folder, with exploitation requiring only DELETE permission on a folder the attacker controls.

[Read original article](https://blog.exodusintel.com/2026/07/06/microsoft-windows-installer-folder-delete-privilege-escalation/){: .btn .btn-primary }
