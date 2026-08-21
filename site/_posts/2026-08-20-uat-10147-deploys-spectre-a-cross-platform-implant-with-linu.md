---
layout: post
title: "UAT-10147 deploys SPECTRE: A cross-platform implant with Linux rootkit and BYOVD capabilities"
date: 2026-08-20 10:00:50 +0300
categories: [RSS]
tags: [malware, apt, edr-bypass, rootkit, ai-assisted]
toc: true
---

UAT-10147, a Chinese-speaking APT, has deployed SPECTRE, a sophisticated cross-platform backdoor targeting IIS and Linux servers. The Windows variant combines runtime API resolution (PEB hash walking with DJB2), per-string xorshift32 PRNG string encryption, anti-analysis scoring (50-point sandbox detection threshold), and C2 configuration stored in NTFS Alternate Data Streams for detection evasion. It implements 45 commands spanning shell execution, file/process manipulation, credential theft, and reconnaissance. Linux variants include kernel rootkits with Bring Your Own Virtual Driver (BYOVD) based EDR bypass techniques. Talos assessment indicates portions of the Linux rootkit exhibit AI-assisted development patterns, signaling the actor's growing adoption of generative AI to accelerate offensive malware development.

[Read original article](https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/){: .btn .btn-primary }
