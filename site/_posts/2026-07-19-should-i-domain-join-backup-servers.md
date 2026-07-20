---
layout: post
title: "Should I Domain Join Backup Servers?"
date: 2026-07-19 08:06:57 +0300
categories: [RSS]
tags: [backup, active-directory, access-control, defensive, incident-response]
toc: true
---

Backup servers and storage infrastructure should not be joined to production Active Directory due to blast radius amplification and misconfiguration risks. Backup files commonly contain password hashes, service accounts, and domain user credentials that can be extracted through trivially misconfigured SMB share permissions, often serving as attack vectors to domain administrator compromise. Once an attacker gains domain admin privileges, they can reach and destroy domain-joined backup infrastructure to eliminate recovery options. The recommendation is to isolate backup infrastructure in a separate AD forest with strict trust boundaries and dedicated administrative accounts, or keep it completely outside the production domain.

[Read original article](https://projectblack.io/blog/should-i-domain-join-backup-servers/){: .btn .btn-primary }
