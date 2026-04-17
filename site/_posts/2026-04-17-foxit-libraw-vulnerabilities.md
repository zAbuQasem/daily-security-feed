---
layout: post
title: "Foxit, LibRaw vulnerabilities"
date: 2026-04-17 03:12:23 +0300
categories: [RSS]
tags: [pdf, use-after-free, libraw, heap-overflow, integer-overflow]
toc: true
---

Cisco Talos disclosed seven patched memory-safety issues across Foxit Reader and LibRaw, including Foxit Reader CVE-2026-3779, a use-after-free triggered by crafted JavaScript embedded in a malicious PDF. In Foxit, improper handling of an Array object can leave freed memory reachable, enabling memory corruption and potentially arbitrary code execution when a user opens the document. Talos also reported six LibRaw bugs affecting RAW image parsing: four heap-based buffer overflows (CVE-2026-20911, CVE-2026-21413, CVE-2026-20889, CVE-2026-24660) and two integer overflows (CVE-2026-24450, CVE-2026-20884), all reachable via specially crafted image files. The post is mainly a disclosure roundup rather than a deep root-cause analysis, but it is still useful for tracking exploit-prone parsing flaws in widely deployed document and image-processing components.

[Read original article](https://blog.talosintelligence.com/foxit-libraw-vulnerabilities/){: .btn .btn-primary }
