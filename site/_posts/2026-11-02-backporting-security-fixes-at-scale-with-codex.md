---
layout: post
title: "Backporting security fixes at scale with Codex"
date: 2026-11-02 12:00:00 +0300
categories: [RSS]
tags: [supply-chain, devops, automation, linux]
toc: true
---

Trail of Bits developed a Codex-based workflow to automate security patch backporting to stable Linux distributions and LTS releases, reducing patch preparation and review time from days to 30 minutes (simple cases) or 3 hours (complex cases). The backlog is substantial: Linux kernel 5.10.y LTS has 2,006 unfixed CVEs including 213 critical/high severity; Debian 13 has 1,128 packages with 4,562 unfixed CVEs (1,822 critical/high). The workflow has already delivered fixes for 149 CVEs to Linux stable kernel releases and major distributions, addressing a critical supply chain gap where ~95% of deployed systems run older stable versions that lack security patches. By automating patch adaptation, dependency checking, test assembly, and submission preparation while maintaining human review, the approach makes previously impractical backporting work economically viable at scale.

[Read original article](https://blog.trailofbits.com/2026/11/02/backporting-security-fixes-at-scale-with-codex/){: .btn .btn-primary }
