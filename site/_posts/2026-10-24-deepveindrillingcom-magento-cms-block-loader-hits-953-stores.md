---
layout: post
title: "deepveindrilling.com: Magento CMS block loader hits 953 stores"
date: 2026-10-24 00:00:00 +0300
categories: [RSS]
tags: [malware, magento, cms-injection, evasion, supply-chain]
toc: true
---

A sophisticated 15-month campaign injects malicious JavaScript loaders into Magento CMS blocks, affecting 953+ online stores since July 2025. The latest `deepveindrilling.com` variant uses browser fingerprinting (detecting webdriver APIs, GPU/CPU details, timezone, and client hints) to evade automated security scanners before delivering payloads to real visitors. Initial compromise occurs via PolyShell (CVE-2026-48356) and SessionReaper (CVE-2025-54236) vulnerabilities, granting admin-level access and persistent CMS block modification. The attacker rotates loader domains every few months through a Keitaro traffic distribution system, delivering credential-stealing payloads including spoofed crypto wallet sites. Once infected, simply deleting the loader does not remove the attacker's underlying database write access—full remediation requires patching vulnerabilities, removing webshells and backdoors, and auditing admin accounts.

[Read original article](https://sansec.io/research/magento-cms-block-loader-deepveindrilling){: .btn .btn-primary }
