---
layout: post
title: "Auditing Application Permissions in Microsoft Entra ID: Hidden Risks, Pitfalls, and Quarkslab's QAZPT Tool"
date: 2026-04-29 22:00:00 +0300
categories: [RSS]
tags: [entra-id, azure, iam, cloud, permissions]
toc: true
---

Quarkslab breaks down why Microsoft Entra ID application auditing is hard in practice by separating the roles of App Registrations and Service Principals, then tracing how effective access expands through app roles, delegated permissions, credentials, ownership, group membership, and federated identity links. The post highlights that the risky part is not just the permissions visible on a single object, but the transitive paths that let an application or principal inherit broader reach across Microsoft Graph, Azure Resource Manager, and Microsoft 365 resources. It also points out operational blind spots such as credentials stored on the App Registration while authorization happens through the Service Principal, which makes portal-only review incomplete. To address this, Quarkslab introduces QAZPT, an open-source tool that collects tenant data, computes effective permissions across inheritance chains, and visualizes the resulting access graph so defenders can identify unexpected privilege paths and over-permissioned applications.

[Read original article](http://blog.quarkslab.com/auditing-application-permissions-in-microsoft-entra-id-hidden-risks-pitfalls-and-quarkslabs-qazpt-tool.html){: .btn .btn-primary }
