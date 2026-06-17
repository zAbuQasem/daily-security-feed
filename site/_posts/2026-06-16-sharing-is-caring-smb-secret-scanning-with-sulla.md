---
layout: post
title: "Sharing is Caring: SMB Secret Scanning with Sulla"
date: 2026-06-16 15:15:41 +0300
categories: [RSS]
tags: [tool-release, secrets-scanning, smb, credentials, pentesting]
toc: true
---

Sulla is an open-source SMB secret scanner that automates discovery of hardcoded credentials (AWS keys, GitHub tokens, SSH keys, database connection strings, etc.) across enterprise network shares. It employs a four-stage pipeline: automated SMB discovery via DNS SRV and LDAP enumeration, six-layer filtering (extension/size/recursion depth/binary detection) to reduce noise before SMB traversal, content matching via the Titus detection library, and structured output (JSON/SARIF/human-readable). Key optimizations include DFS namespace deduplication to eliminate redundant scans across 10,000+ machines in ~30 minutes, and quick-mode allowlisting to surface high-confidence findings fast. The tool runs as a standalone Linux binary—eliminating the need for a Windows attack box—and integrates with Praetorian's Guard platform for continuous weekly SMB scanning with deduplication across runs.

[Read original article](https://www.praetorian.com/blog/sharing-is-caring-smb-secret-scanning-with-sulla/){: .btn .btn-primary }
