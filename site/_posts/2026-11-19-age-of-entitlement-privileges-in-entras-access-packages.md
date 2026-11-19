---
layout: post
title: "Age of Entitlement: Privileges in Entra's access packages"
date: 2026-11-19 00:00:00 +0300
categories: [RSS]
tags: [cloud, entra-id, privilege-escalation, iam, azure]
toc: true
---

Datadog Security Labs examines privilege escalation risks in Microsoft Entra ID's entitlement management system, which bundles access (group memberships, app roles, SharePoint access) for user lifecycle management. While Microsoft blocks assignment of privileged Entra roles via access packages, the system allows inclusion of role-assignable groups and high-privilege roles like Exchange Administrator, creating an attack surface for privilege escalation. The article details the architecture of entitlement management (catalogs, resources, access packages, and approval policies) and identifies how misconfigured access packages could be exploited. This is part 1 of a series that promises deeper analysis of real-world attack scenarios and defensive monitoring strategies for Entra ID governance deployments.

[Read original article](https://securitylabs.datadoghq.com/articles/entra-access-packages-part-1-privileges/){: .btn .btn-primary }
