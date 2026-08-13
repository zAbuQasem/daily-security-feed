---
layout: post
title: "Avoid Azure secret rotation with secretless authentication"
date: 2026-08-12 00:00:00 +0300
categories: [RSS]
tags: [cloud, azure, oidc, authentication, identity]
toc: true
---

Datadog's Azure integration now supports secretless authentication using OpenID Connect (OIDC) federated identity credentials instead of long-lived client secrets. The mechanism establishes a trust relationship via federated credentials in Microsoft Entra ID; when Datadog requests access, it presents an OIDC token, which Entra ID validates against the configured trust relationship and exchanges for a short-lived access token. This eliminates the operational burden of creating, storing, and rotating client secrets, reducing the risk of credential expiration outages and the attack surface of long-lived credentials. The feature is available during new Azure integration setup or via a migration path for existing client secret-based configurations, supporting Azure CLI, Terraform, and portal-based configuration.

[Read original article](https://www.datadoghq.com/blog/azure-secretless-authentication/){: .btn .btn-primary }
