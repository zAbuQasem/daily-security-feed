---
layout: post
title: "Tracing Digital Intent: New MacOS Tahoe 26 Artifact Discovered"
date: 2026-06-12 22:00:14 +0300
categories: [RSS]
tags: [forensics, macos, detection, blue-team]
toc: true
---

Palo Alto Unit 42 discovered a new macOS Tahoe 26 Biome stream artifact—App.MenuItem—that logs specific menu selections with timestamps in SEGB-encapsulated protobuf format. The artifact, located at ~/Library/Biome/streams/restricted/App.MenuItem/local, can be parsed using the open-source ccl-segb tool. By capturing deliberate user actions (e.g., 'Compress folder' followed by 'Empty Trash'), it reveals user intent and workflow patterns, enabling investigators to detect suspicious behavior like data exfiltration preparation. While limited by generic menu labels, it gains power when correlated with file system logs, filling a forensic gap between technical logs and human-level activity narratives.

[Read original article](https://unit42.paloaltonetworks.com/new-macos-artifact-discovered/){: .btn .btn-primary }
