---
layout: post
title: "Investigating server compromises with cgroups: A Linux DFIR primer"
date: 2026-05-13 13:01:43 +0300
categories: [RSS]
tags: [linux, dfir, cgroups, detection, containers]
toc: true
---

This article shows how Linux cgroup metadata can be repurposed as a DFIR and detection signal to enrich process telemetry during server compromise investigations. It explains how cgroups v2 expose a hierarchical path that often embeds high-value context from user space managers such as systemd, including service names under paths like /system.slice/<service>.service, per-user slices, and session scopes such as /user.slice/user-$UID.slice/session-1.scope that help correlate processes to specific logins. The post also covers container environments, where runtimes like Docker assign all processes in a container to a shared cgroup such as /docker/<container_id>, giving defenders a way to group related activity and distinguish containerized execution without depending on runtime-specific hooks. The practical value is in separating benign and malicious processes that may have similar parent/child trees, using cgroup paths to identify attacker-created services, user sessions, and container boundaries during Linux investigations.

[Read original article](https://redcanary.com/blog/threat-detection/linux-cgroups/){: .btn .btn-primary }
