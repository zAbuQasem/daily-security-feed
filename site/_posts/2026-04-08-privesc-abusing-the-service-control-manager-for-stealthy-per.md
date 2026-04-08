---
layout: post
title: "PrivEsc: Abusing the Service Control Manager for Stealthy & Persistent LPE"
date: 2026-04-08 00:00:00 +0300
categories: [Research]
tags: [privesc, windows, lpe, persistence, detection]
toc: true
---

A Windows local privilege escalation technique abuses the Service Control Manager (SCM) by modifying its DACL via `sc.exe sdset scmanager D:(A;;KA;;;WD)`, which grants Everyone full KEY_ALL_ACCESS rights to the SCM. Once set from a compromised admin account, any non-privileged user can create a new Windows service that runs under SYSTEM context, enabling arbitrary command execution as SYSTEM. The persistence mechanism is resilient: removing the account from local admins doesn't remove the service, and removing the service doesn't revoke the ability to create a new one — only reverting the SCM DACL remediation breaks the chain. The article includes a Sigma rule detecting `sc.exe sdset scmanager` with the permissive ACL string for high-confidence alerting.

---

[Read original article](https://0xv1n.github.io/posts/scmanager/)
