---
layout: post
title: "Copy Fail: What You Need to Know About the Most Severe Linux Threat in Years"
date: 2026-05-05 23:00:33 +0300
categories: [RSS]
tags: [linux, kernel, lpe, containers, ci-cd]
toc: true
---

CVE-2026-31431 ("Copy Fail") is a deterministic Linux local privilege escalation bug in the kernel's AF_ALG AEAD path, specifically the algif_aead module combined with the authencesn algorithm and a 2017 in-place scatterlist optimization. The flaw lets an unprivileged user abuse sendmsg() plus splice() so page-cache pages are incorrectly chained into a writable destination buffer, enabling a controlled 4-byte overwrite beyond the intended output region; the attacker controls the overwrite via seqno_lo in bytes 4-7 of the AAD. In practice, this allows corruption of the in-memory page cache for readable setuid binaries such as /usr/bin/su or sudo, so the modified cached image executes with root privileges while the on-disk file remains unchanged and many integrity checks see nothing. Because the exploit is straight-line, offset-free, and reportedly works across kernels 4.14 through 6.19.12 on major distributions, it has broad impact for container escape, multi-tenant host compromise, and CI/CD runner takeover.

[Read original article](https://unit42.paloaltonetworks.com/cve-2026-31431-copy-fail/){: .btn .btn-primary }
