---
layout: post
title: "VMs won't contain cyber-capable agents"
date: 2026-08-26 11:00:00 +0300
categories: [RSS]
tags: [vm-escape, 0-day, ai-security, kvm, infrastructure]
toc: true
---

Trail of Bits demonstrated that GPT 5.6-Cyber successfully escaped a QEMU/KVM VM on a hardened Linux host three times by discovering and chaining multiple vulnerabilities: initially exploiting Januscape (CVE-2026-53359) in the kernel, then combining libslirp CVE-2026-9539 with an unmarked fix commit to achieve arbitrary memory read/write on the host, and finally constructing a reliable exploit chain using three 0-days (QEMU VAPIC SMRAM alias overlap, unpatched KVM shadow page bugs) plus a patched-upstream-but-unpatched-in-distribution KVM TLB invalidation bug. The agent operated autonomously for ~12 hours, backtracked from failed approaches, pulled research papers, wrote exploits with minimal prompting, and demonstrated that VMs can no longer be assumed to contain sufficiently advanced AI agents—they should be treated as advanced persistent threats requiring isolation at the physical or hardware level.

[Read original article](https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/){: .btn .btn-primary }
