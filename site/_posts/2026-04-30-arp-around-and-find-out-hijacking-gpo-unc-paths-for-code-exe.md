---
layout: post
title: "ARP Around and Find Out: Hijacking GPO UNC Paths for Code Execution and NTLM Relay"
date: 2026-04-30 04:00:00 +0300
categories: [RSS]
tags: [active-directory, gpo, ntlm-relay, webdav, arp-spoofing]
toc: true
---

TrustedSec shows that a principal with only WriteGPLink on an Active Directory OU can weaponize existing GPOs that reference UNC paths, without editing the GPO itself or modifying SYSVOL. The attack links a legitimate software deployment GPO to the victim OU, then uses same-segment ARP spoofing to impersonate the file server referenced by the MSI path so the target machine retrieves an attacker-controlled installer and executes it as SYSTEM during policy processing. The post extends the technique beyond software installation to drive mappings, logon scripts, and startup scripts, all of which can be redirected to capture NTLMv2 or serve attacker-controlled content from the expected UNC location. It also demonstrates forcing SMB disruptions so authentication falls back to WebDAV, moving NTLM over HTTP into a form that can be relayed to LDAP(S), AD CS, or SMB for further domain compromise.

[Read original article](https://trustedsec.com/blog/arp-around-and-find-out-hijacking-gpo-unc-paths-for-code-execution-and-ntlm-relay){: .btn .btn-primary }
