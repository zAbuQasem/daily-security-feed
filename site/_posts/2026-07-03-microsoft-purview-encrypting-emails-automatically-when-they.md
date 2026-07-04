---
layout: post
title: "Microsoft Purview: Encrypting Emails Automatically When They Contain a BSN"
date: 2026-07-03 05:00:00 +0300
categories: [RSS]
tags: [dlp, pii, encryption, microsoft-365, defensive]
toc: true
---

A technical guide on configuring Microsoft Purview DLP policies combined with message encryption to automatically protect emails containing sensitive PII like Dutch BSN (Burgerservicenummer). The article covers three core components: DLP rules detecting sensitive info types, automatic message encryption with "Do Not Forward" protection (preventing forwarding, printing, and copying), and optional custom branding templates for expiration and revocation. It includes PowerShell commands to enable Azure Rights Management, step-by-step DLP policy configuration in the Purview portal, testing methodology via Activity Explorer, and explains the different recipient experiences (native decryption for Microsoft account holders vs. portal-based access for external recipients). This is practical defensive guidance for organizations securing sensitive personal data in email workflows.

[Read original article](https://thalpius.com/2026/07/03/microsoft-purview-encrypting-emails-automatically-when-they-contain-a-bsn/){: .btn .btn-primary }
