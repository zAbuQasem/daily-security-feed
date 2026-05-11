---
layout: post
title: "Personal Software and BaremetalVMM"
date: 2026-05-10 07:00:00 +0300
categories: [RSS]
tags: [llm, firecracker, virtualization, supply-chain, secure-design]
toc: true
---

The post describes BaremetalVMM, a personal Firecracker-based microVM manager built largely with LLM assistance to support security testing workloads that do not fit well in containers. The tool can launch microVMs with different kernels, start Kubernetes clusters, expose a web UI and systemd service, and now embeds an xterm.js browser console for remote VM access. The security-relevant point is not a single vulnerability but the author's observation that LLM-generated software can easily ship with weak defaults and poorly-reviewed architecture; in this case, the generated web UI was initially bound to all interfaces and protected only by unproven authentication. The article also highlights broader risks in "personal software," especially unvetted dependency choices, opaque supply-chain exposure, and the likelihood that lightly engineered internal tools become production-critical systems without proper security review.

[Read original article](https://raesene.github.io/blog/2026/05/10/personal-software-and-baremetalvmm/){: .btn .btn-primary }
