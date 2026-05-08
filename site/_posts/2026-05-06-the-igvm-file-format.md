---
layout: post
title: "The IGVM File Format"
date: 2026-05-06 22:00:00 +0300
categories: [RSS]
tags: [virtualization, confidential-computing, igvm, tdx, sev-snp]
toc: true
---

Quarkslab breaks down the Independent Guest Virtual Machine (IGVM) binary format used to package and securely launch a VM’s initial state, including firmware, kernel, and initrd, across different virtualization stacks. The article walks through the fixed header fields such as `variable_header_offset`, `variable_header_size`, `total_file_size`, and the CRC32 checksum, then explains how version 2 adds architecture and page size metadata for x64 and AArch64 guests. It also details the variable-header model, where platform headers describe supported isolation environments and VTL levels, initialization headers define guest policy and relocatable memory regions, and directive headers drive how embedded payloads like the OpenHCL bootloader, Linux kernel, and ramdisk are mapped and processed. The security relevance is in how IGVM supports measured launch for confidential-computing environments like AMD SEV-SNP and Intel TDX, giving practitioners a concrete view of the structures that underpin VM integrity and attestation.

[Read original article](http://blog.quarkslab.com/the-igvm-file-format.html){: .btn .btn-primary }
