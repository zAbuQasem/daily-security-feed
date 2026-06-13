---
layout: post
title: "Unauthenticated file upload in Amasty Order Attributes for Magento"
date: 2026-06-12 00:00:00 +0300
categories: [RSS]
tags: [rce, magento, file-upload, unauthenticated, ecommerce]
toc: true
---

An unauthenticated arbitrary file upload vulnerability (CVE-2026-53787, CVSS 9.3) in Amasty Order Attributes for Magento 2 (versions ≤3.16.0) allows attackers to upload executable files to the media directory with no authentication, potentially enabling remote code execution. The vulnerability stems from missing input validation and unsanitized filenames on the upload endpoint; prior versions also allow path traversal to write outside the media folder. Amasty patched the flaw in version 4.0.0 by adding mandatory `attribute_code` parameter validation, file extension allow-listing, and stricter attribute verification. Unpatched Magento stores running this popular extension face rising exploit pressure and should prioritize immediate patching or deploy WAF-based upload filtering.

[Read original article](https://sansec.io/research/amasty-order-attributes-file-upload){: .btn .btn-primary }
