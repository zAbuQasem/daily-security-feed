---
layout: post
title: "Kernel Drivers, Process Protection, and ...Bears?"
source_url: https://0xv1n.github.io/posts/processprotection/
date: 2026-04-08
priority: 3
tags: [windows, kernel, lsass, credential-access, bypass, github-zabuqasem, linkedin-zeyad-abulaban]
feed: https://0xv1n.github.io/index.xml
---

This post documents the author's journey through Windows Protected Process Light (PPL) internals with the goal of disabling PPL on lsass.exe via a kernel driver. It explains the PPL hierarchy — where higher protection level processes can interact with lower ones but not vice versa — and covers how lsass.exe runs at PROTECTION_LEVEL_LSA_LIGHT to guard credential storage. The author details how to enable LSA PPL via registry key (RunAsPPL DWORD under HKLM\SYSTEM\CurrentControlSet\Control\Lsa) or Group Policy, and sets up the context for kernel-mode driver development to strip the protection flag directly from the EPROCESS structure. The technique is well-known (builds on Mimikatz/PPLdump prior art) but the post is a clear educational walkthrough for those learning Windows internals and driver-based credential access bypasses.
