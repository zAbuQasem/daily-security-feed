---
layout: post
title: "Amasty patches 25 Magento extensions, 1 critical"
date: 2026-07-02 00:00:00 +0300
categories: [RSS]
tags: [rce, magento, file-upload, unauthenticated]
toc: true
---

Amasty released patches for 25 Magento extensions, including a critical remote code execution vulnerability in Advanced Product Reviews that allows unauthenticated attackers to upload arbitrary files to unrestricted locations, bypassing standard PHP execution restrictions under pub/media and enabling web shell deployment. One prior Amasty vulnerability (Order Attributes) saw 12,000+ exploitation attempts within 3 days of patching. The flaw affects thousands of Magento and Adobe Commerce stores. Immediate upgrade to patched versions is recommended for the critical issue; medium and low severity patches should be applied within 4 weeks.

[Read original article](https://sansec.io/research/amasty-mass-disclosure){: .btn .btn-primary }
