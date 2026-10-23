---
layout: post
title: "EMudhra Intermediate CA Certificates Compromised"
date: 2026-10-22 17:15:32 +0300
categories: [RSS]
tags: [pki, crypto, tls, supply-chain]
toc: true
---

Eight intermediate CA private keys from eMudhra Limited were compromised due to insufficient randomness during certificate generation, allowing attackers to derive the private keys from public certificates through cryptographic analysis. Affected organizations must immediately identify systems using certificates issued under these compromised intermediates and re-issue them through alternative CAs. Attackers can use the derived private keys to sign unauthorized TLS certificates for man-in-the-middle attacks and session hijacking against any targeted domain. Major browser vendors (Google Chrome, Mozilla) and OS vendors are revoking trust in these CAs globally. Organizations should audit PKI assets, enforce strict revocation checking, implement Certificate Transparency monitoring, and update trust stores across all endpoints, servers, and container images.

[Read original article](https://unit42.paloaltonetworks.com/emudhra-certificate-compromise/){: .btn .btn-primary }
