---
layout: post
title: "Paramiko Security Audit"
date: 2026-05-04 22:00:00 +0300
categories: [RSS]
tags: [ssh, python, crypto, audit, paramiko]
toc: true
---

Quarkslab and OSTIF audited Paramiko and its use of pyca/cryptography, focusing on SSHv2 key exchange, signature handling, entropy sources, constant-time behavior, and the security of the surrounding build and CI/CD pipeline. The review found 30 issues, including high-severity weaknesses such as insecure RSA signature parameters in `paramiko/rsakey.py` and acceptance of unsafe TripleDES key sizes in Cryptography, plus medium-severity problems around deprecated Diffie-Hellman group exchange, legacy GSS-API key exchanges, and an 8-byte seed used for TripleDES key generation. Lower-severity findings included MD5-based key derivation in `paramiko/pkey.py`, Ed25519 signature validation paths that could mishandle exceptions or crash the transport thread, and allowing insecure RSA key sizes. The practical takeaway is not a new exploit chain but a detailed hardening map for one of Python's most widely used SSH stacks and its crypto integration, with multiple fixes already linked to specific remediation commits and pull requests.

[Read original article](http://blog.quarkslab.com/paramiko-security-audit.html){: .btn .btn-primary }
