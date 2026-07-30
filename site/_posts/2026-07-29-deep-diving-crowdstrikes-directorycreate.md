---
layout: post
title: "Deep-diving Crowdstrike’s DirectoryCreate"
date: 2026-07-29 10:30:28 +0300
categories: [RSS]
tags: [detection, edr, crowdstrike, hunting, windows]
toc: true
---

A systematic analysis of CrowdStrike Falcon's DirectoryCreate telemetry event, which fires on IRP_MJ_CREATE at kernel altitude 321410. Testing 60 directory creation methods reveals critical detection gaps: directory renames/moves produce no telemetry (only IRP_MJ_SET_INFORMATION), junctions and bind links report the target path not the request path (bypassing path-based detection rules), actor attribution is unreliable (showing intermediate processes like WmiPrvSE rather than actual requestors), and SMB creates fire twice with distinct signatures. The resolved device path format (\Device\HarddiskVolumeN\...) means drive-letter or obfuscation-based bypass attempts fail, but renaming a staged directory to its final path generates zero events. Critical implications for detection engineering: path-based rules can be bypassed via rename-then-move technique, and attribution-based hunting requires process chain pivoting beyond the raw event.

[Read original article](https://detect.fyi/deep-diving-crowdstrikes-directorycreate-6d7e5756c073?source=rss----d5fd8f494f6a---4){: .btn .btn-primary }
