---
layout: post
title: "Old Wine in a New Bottle: A Decade-Old lxd-Group Root, Re-Armed"
date: 2026-06-09 00:00:00 +0300
categories: [RSS]
tags: [privesc, ubuntu, lxd, cloud, rce]
toc: true
---

A privilege escalation chain on Ubuntu Server (20.04–26.04) exploits the default placement of the first user in the `lxd` group combined with the `lxd-installer` socket, which socket-activates a root service allowing password-free installation of LXD. An attacker can launch a privileged container with `security.privileged=true` and bind-mount the host root filesystem, then create SUID binaries or modify `/etc/shadow` to gain unauthenticated root access without entering the sudo password. The vulnerability is an insecure composition of documented, intended behaviors: LXD's design explicitly treats group membership as root-equivalent, but 2024+ Server images re-enable the risk by default while LXD itself is no longer pre-installed. Canonical has reviewed and cleared publication with a "won't fix" stance, and the researchers provide a full PoC (`exploit.sh`) and impact validation across four releases.

[Read original article](https://starlabs.sg/blog/2026/06-old-wine-in-a-new-bottle-a-decade-old-lxd-group-root-re-armed/){: .btn .btn-primary }
