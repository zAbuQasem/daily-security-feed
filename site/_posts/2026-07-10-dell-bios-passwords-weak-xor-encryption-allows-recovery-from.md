---
layout: post
title: "Dell BIOS Passwords: Weak XOR Encryption Allows Recovery from SPI Flash (CVE-2026-40639)"
date: 2026-07-10 10:25:38 +0300
categories: [RSS]
tags: [bios, firmware, cryptography, cve, dell]
toc: true
---

Dell BIOS stores administrator and user passwords using repeating-key XOR encryption in the DVAR flash region, not a one-way hash. The scheme uses a 20-byte key to encrypt a 32-byte password field (with the first character stored in the clear), but the null-padding that follows short passwords is XOR-encrypted with the key, leaking raw key material into the stored record. For passwords up to 12 characters, the entire 20-byte key is recoverable directly from the flash dump; longer passwords can be recovered via a key derivation quirk. An attacker with physical access (via SOIC clip and cheap SPI programmer or compromised OS boot) can extract the SPI flash and recover the original password deterministically in milliseconds, gaining full BIOS control. The vulnerability (CVE-2026-40639) affects legacy Dell platforms and current hardware including the supported Wyse 5070 thin client. This research is from MDSec, a high-confidence source, and combines practical hardware attack with a fundamental cryptographic failure.

[Read original article](https://www.mdsec.co.uk/2026/07/dell-bios-passwords-weak-xor-encryption-allows-recovery-from-spi-flash-cve-2026-40639/){: .btn .btn-primary }
