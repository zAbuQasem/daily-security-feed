---
layout: post
title: "Bad Habits: An ANTISOC Operation"
date: 2026-05-27 14:00:00 +0300
categories: [RSS]
tags: [social-engineering, password-spray, mfa-bypass, red-team, lateral-movement]
toc: true
---

A Black Hills ANTISOC red team engagement narrative demonstrating how a helpdesk technician's habit of reusing a single predictable password for all resets created a systemic vulnerability. Operators obtained the password via a social engineering call, then sprayed it across 100+ accounts sourced from an Entra ID enumeration. Accounts lacking MFA enrollment were quietly hijacked, MFA was self-enrolled by operators, and SSH tunneling combined with replacing zoom.exe in user profiles established persistent C2 without commercial tooling. Operators then pivoted to SharePoint credential files, ultimately gaining access to a SaaS backup portal with full read/write access to all corporate backups — a ransomware-equivalent impact. Remediation included disabling open MFA enrollment, enforcing SSO for backup access, and deploying EDR on VDI infrastructure.

[Read original article](https://www.blackhillsinfosec.com/antisoc-operation/){: .btn .btn-primary }
