---
layout: post
title: "Hacking the My Arcade Contra Pocket Player - Part II"
date: 2026-11-17 05:00:00 +0300
categories: [RSS]
tags: [hardware-hacking, firmware-analysis, reverse-engineering, embedded-systems, bootloader]
toc: true
---

This article details a comprehensive firmware analysis and modification workflow for the My Arcade Contra Pocket Player, powered by a Rockchip RK3128 SoC. The author maps the NAND flash layout (MBR + GPT with five partitions: U-Boot bootloader, ARM Trusted Firmware, Android boot image, SquashFS rootfs, and ext2 userdata) and documents the first-stage IDB loader with RC4-encrypted magic values at sector 64. The practical methodology extracts individual partitions using dd, unpacks the 65 MiB SquashFS rootfs using unsquashfs, makes modifications to the game launcher filesystem, repacks with mksquashfs (gzip compression, 131KB blocks), and reflashes via RockUSB mode. Specific technical details include partition offsets in bytes and sectors, the case-sensitivity pitfall on macOS filesystems, and the boot chain flow through BusyBox init to the proprietary MiniGUI game selector. This enables end-users to swap custom games on these handheld emulation devices.

[Read original article](https://trustedsec.com/blog/hacking-the-my-arcade-contra-pocket-player-part-ii){: .btn .btn-primary }
