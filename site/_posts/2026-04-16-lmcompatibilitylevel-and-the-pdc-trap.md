---
layout: post
title: "LmCompatibilityLevel and the PDC Trap"
date: 2026-04-16 03:12:34 +0300
categories: [RSS]
tags: [ntlm, windows, active-directory, netlogon, authentication]
toc: true
---

The article shows that on Windows domain controllers, setting LmCompatibilityLevel=5 on a non-PDC DC does not reliably block NTLMv1 authentication because the DC is not treated as authoritative for that decision. After reversing msv1_0.dll and ntlmshared.dll, the author found that MsvpPasswordValidate skips NTLMv1 hash comparison at level 5, returns STATUS_WRONG_PASSWORD, and leaves the Authoritative flag unset; Netlogon then forwards the NTLMv1 authentication blob unchanged to the PDC emulator for final validation. If the PDC is configured with a lower LmCompatibilityLevel, NTLMv1 can still succeed even when clients connect to other supposedly hardened DCs, making the PDC the real enforcement point for the entire domain. The practical impact is a security-feature bypass of administrators' intended segmentation strategy: lowering NTLMv1 support on the PDC for a limited legacy-use case effectively re-enables NTLMv1 acceptance domain-wide.

[Read original article](https://decoder.cloud/2026/04/15/lmcompatibilitylevel-and-the-pdc-trap/){: .btn .btn-primary }
