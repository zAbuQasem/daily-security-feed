---
layout: post
title: "Adobe patches critical Magento account takeover (APSB26-92)"
date: 2026-08-11 00:00:00 +0300
categories: [RSS]
tags: [account-takeover, magento, cve, unauthenticated, session]
toc: true
---

CVE-2026-71362 is an unauthenticated customer account takeover in Adobe Commerce and Magento Open Source (CVSS 9.1). The vulnerability exists in how Magento handles customer identity in account sessions, allowing attackers to switch a customer session to another customer account without existing credentials, admin privileges, or user interaction. Successful exploitation grants full access to the victim's account and private customer data. Adobe released isolated patch files as APSB26-92 to fix this and six other vulnerabilities, including stored XSS and authorization flaws.

[Read original article](https://sansec.io/research/adobe-commerce-account-takeover-apsb26-92){: .btn .btn-primary }
