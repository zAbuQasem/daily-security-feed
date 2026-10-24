---
layout: post
title: "Field Notes: Reconstructing an Attacker’s Workflow"
date: 2026-10-22 17:58:20 +0300
categories: [RSS]
tags: [incident-response, powershell, credential-harvesting, active-directory, tradecraft]
toc: true
---

A detailed forensic reconstruction of PowerShell-based attacker tradecraft recovered during post-compromise incident investigation. The attacker deployed a persistent file-watching command runner that monitors a temporary file for changes and executes commands via Invoke-Expression, overlapping with Microsoft's documented TerminalFix campaign. Credential harvesting occurs via a fake Windows credential prompt (PromptForCredential) that repeatedly challenges the victim until valid credentials for a target account are supplied, logging all plaintext attempts—demonstrating that sophisticated credential theft doesn't always require LSASS dumping or infostealer malware. Reconnaissance scripts leverage DirectoryServices.DirectorySearcher to enumerate Active Directory computer objects, then validate admin access via remote WMI queries to Win32_OperatingSystem across up to 30 concurrent targets, followed by SMB share discovery across /24 ranges. The analysis reveals how forensic artifacts (particularly credential logs) directly expose attacker workflow and victim compromise scope.

[Read original article](https://dfir.ch/posts/field_note_attacker_workflow/){: .btn .btn-primary }
