---
layout: post
title: "Microsoft Entra ID: Understanding OAuth App Consent and Permissions"
date: 2026-04-22 03:12:34 +0300
categories: [RSS]
tags: [entra-id, oauth, app-consent, iam, microsoft-365]
toc: true
---

This post is a technical walkthrough of how OAuth application consent actually works in Microsoft Entra ID, aimed at correcting common misconceptions that appear when teams deploy third-party Microsoft 365 integrations. It explains the architectural split between an App Registration and the tenant-local Enterprise Application (service principal), emphasizing that granted consent is recorded on the Enterprise Application rather than on the App Registration itself. The article then breaks down Entra's user consent controls, including the difference between disabling user consent entirely, allowing consent only for verified publishers and low-impact delegated permissions, and using Microsoft's managed default policy that blocks specific high-impact scopes such as Mail.Read and Files.ReadWrite.All. It also covers the Admin Consent Workflow, where blocked users can submit approval requests and designated reviewers can evaluate requested permissions, making the piece useful as a defensive identity-security guide for controlling third-party OAuth app access in Entra tenants.

[Read original article](https://thalpius.com/2026/04/21/microsoft-entra-id-understanding-oauth-app-consent-and-permissions/){: .btn .btn-primary }
