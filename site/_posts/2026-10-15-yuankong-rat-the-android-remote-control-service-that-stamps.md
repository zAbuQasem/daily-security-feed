---
layout: post
title: "YuanKong RAT: the Android remote-control service that stamps its operators' names into every build"
date: 2026-10-15 00:00:00 +0300
categories: [RSS]
tags: [malware, android, rat, reverse-engineering, threat-intelligence]
toc: true
---

YuanKong is an Android RAT deployed via dropper APKs that store their encryption key and IV in cleartext in `assets/vault-config.json`, using a trivial "SVLT-XOR-v2" two-key XOR cipher. Star Labs reverse-engineered 110 samples to identify 42 distinct operator accounts (e.g., `lichunfeng7`), all sharing one signing certificate and C2 infrastructure, with operator IDs hardcoded as string constants in each build. The malware establishes WebSocket (Socket.IO) connections to known C2 domains and exfiltrates data via screen recording, accessibility tree reading (including password fields), clipboard theft, and wireless ADB escalation to `shell` user. The sloppy operational security—embedding operator names and account IDs in every binary—enables attribution and tracking of distinct threat actors; the analysis confirms 44 distinct build brands tied to 42 operator accounts across the malware family.

[Read original article](https://starlabs.sg/blog/2026/10-yuankong-rat-the-android-remote-control-service-that-stamps-its-operators-names-into-every-build/){: .btn .btn-primary }
