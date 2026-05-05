---
layout: post
title: "CloudZ RAT potentially steals OTP messages using Pheno plugin"
date: 2026-05-05 10:00:18 +0300
categories: [RSS]
tags: [windows, malware, rat, otp, phone-link]
toc: true
---

Cisco Talos describes a 2026 intrusion chain where a fake ScreenConnect update launches a Rust dropper, which writes a .NET loader disguised as update.txt into ProgramData and persists it via a scheduled task named SystemWindowsApis that runs regasm.exe as SYSTEM. The loader performs timing, process, and VM/sandbox checks, reconstructs and decrypts the CloudZ RAT in memory, opens an encrypted C2 channel, and supports browser credential theft plus plugin delivery. The notable technique is the previously undocumented Pheno plugin, which abuses Microsoft Phone Link by monitoring for active PC-to-phone sessions and accessing PhoneExperiences-*.db SQLite files on the Windows host. That lets the operator harvest synced SMS and notification data, including potential one-time passwords and authenticator prompts, without deploying malware directly to the victim’s phone.

[Read original article](https://blog.talosintelligence.com/cloudz-pheno-infostealer/){: .btn .btn-primary }
