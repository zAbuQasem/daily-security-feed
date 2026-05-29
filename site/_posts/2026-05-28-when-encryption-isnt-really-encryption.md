---
layout: post
title: "When Encryption Isn’t Really Encryption"
date: 2026-05-28 21:27:41 +0300
categories: [RSS]
tags: [iot, credential-leak, client-side-enforcement, lateral-movement, printer-security]
toc: true
---

Canon imageRUNNER ADVANCE DX printers (200+ models, CVE-2026-1789) expose stored credentials via a client-side-only encryption enforcement flaw in the configuration export feature. The web UI presents encryption as mandatory, but the actual HTTP POST parameter controlling plaintext vs. encrypted export is never validated server-side — changing it to 'plaintext' causes the server to return the full config file with all credentials unprotected. Exploitation requires admin access, but default credentials on these devices are common, making the bar low. In a real assessment, Praetorian extracted domain service account credentials from a printer, bypassed network segmentation, and achieved full domain compromise. Full reproduction details are withheld pending Canon's broader product-line patch assessment.

[Read original article](https://www.praetorian.com/blog/canon-printer-credential-leak/){: .btn .btn-primary }
