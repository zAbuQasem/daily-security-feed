---
layout: post
title: "The skb that wasn't freed - the Fragnesia primitive via Open vSwitch"
date: 2026-09-16 22:00:00 +0300
categories: [RSS]
tags: [kernel, lpe, infrastructure, memory-corruption, container]
toc: true
---

Open vSwitch's kernel datapath strips the SKBFL_SHARED_FRAG flag from forwarded packets, re-opening the in-place-decrypt-on-shared-pages primitive that the Fragnesia fix was designed to block. An unprivileged user can exploit this through the OVS userspace genl API (which lacks CAP_SYS_MODULE requirement and supports GENL_UNS_ADMIN_PERM within user namespaces) to achieve deterministic local privilege escalation on default installs of Arch, Fedora, Debian, Amazon Linux, and RHEL. The vulnerability affects the kernel datapath flow execution logic where skb frags are manipulated during packet forwarding; OVS forwards packets through the TCP coalesce and ESP decryption paths without preserving shared-frag ownership markers. Tracked as CVE-2026-90049, CVE-2026-89487, and CVE-2026-80977, with fixes merged upstream 09/04/2026.

[Read original article](https://blog.doyensec.com/2026/09/17/ovs.html){: .btn .btn-primary }
