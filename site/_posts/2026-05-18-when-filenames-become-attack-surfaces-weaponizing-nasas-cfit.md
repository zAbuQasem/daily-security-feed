---
layout: post
title: "When Filenames Become Attack Surfaces: Weaponizing NASA's CFITSIO Extended Filename Syntax"
date: 2026-05-18 22:00:00 +0300
categories: [RSS]
tags: [ssrf, file-write, header-injection, cfitsio, parsing]
toc: true
---

Doyensec shows that NASA CFITSIO's Extended Filename Syntax (EFS) is effectively a filename mini-language processed by `ffopen()`, where strings are reinterpreted into protocol handlers, output clauses, extension selectors, and filter expressions via registered backends like `http://`, `ftps://`, and `mem://`. The key abuse primitive is the outfile clause (`input.fits(output.fits)`): CFITSIO copies the source to an attacker-chosen destination before validating that the source is even a FITS file, turning a filename parameter into an arbitrary file-copy primitive. Because EFS also supports remote URL schemes, the same behavior becomes an SSRF gadget that can fetch attacker-specified HTTP/FTP resources and persist the response to a local path, which is useful for targeting localhost or cloud metadata services. The write-up also highlights HTTP header injection in the legacy raw-socket HTTP path, showing how documented compatibility features in a scientific file library can be chained into practical exfiltration, local file write, and cloud-environment attack primitives.

[Read original article](https://blog.doyensec.com/2026/05/19/cfitsio-weaponized-filenames.html){: .btn .btn-primary }
