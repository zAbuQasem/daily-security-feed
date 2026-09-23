---
layout: post
title: "User writeback from Entra ID to AD!"
date: 2026-09-22 16:04:00 +0300
categories: [RSS]
tags: [cloud, identity-management, azure]
toc: true
---

Microsoft Entra Connect Cloud Sync now supports user writeback from Entra ID to on-premises Active Directory in public preview. This enables creation and management of AD users entirely through Microsoft Graph/Entra ID, supporting hybrid scenarios like access packages automatically provisioning on-premises accounts. The article explains attribute mapping via transformation expressions (e.g., sAMAccountName derived from UPN prefix, UPN construction logic), scoping filters, and configuration of target containers for AD placement. Notably, password writeback is not yet supported, requiring passwordless authentication for practical deployment. This extends existing group writeback capability to individual users, reducing dependency on legacy AD management.

[Read original article](https://goodworkaround.com/2026/09/22/user-writeback-from-entra-id-to-ad/){: .btn .btn-primary }
