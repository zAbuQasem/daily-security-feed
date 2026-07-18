---
layout: post
title: "Azure Penetration Testing Training"
date: 2026-07-17 21:11:34 +0300
categories: [RSS]
tags: [azure, cloud, identity, privilege-escalation, entra-id]
toc: true
---

Azure's attack surface is identity-centric, with Entra ID compromise cascading to Azure subscriptions, Microsoft 365, and hybrid on-premises infrastructure. Key techniques include password spray against legacy auth endpoints, device code phishing via OAuth device flows, application consent abuse, Conditional Access bypass, managed identity exploitation on VMs and App Services, custom role misconfigurations enabling self-escalation, Pass-the-PRT for device-based token theft, Golden SAML via AD FS certificate compromise, and hybrid identity attacks bridging on-premises AD into Azure tenants. The article references real threat campaigns (Storm-0558, APT-29) and covers Microsoft 365 attack chains (mailbox delegation, Teams/SharePoint enumeration) and serverless compute abuse. While primarily educational marketing for training bootcamps rather than novel research or CVE disclosure, the content provides substantive technical descriptions of Azure-specific attack methodologies.

[Read original article](https://blog.pwnedlabs.io/azure-penetration-testing-training){: .btn .btn-primary }
