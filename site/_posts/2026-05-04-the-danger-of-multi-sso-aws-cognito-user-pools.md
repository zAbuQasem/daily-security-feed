---
layout: post
title: "The Danger of Multi-SSO AWS Cognito User Pools"
date: 2026-05-04 22:00:00 +0300
categories: [RSS]
tags: [aws, cognito, sso, oidc, cloud]
toc: true
---

Doyensec shows how multi-tenant AWS Cognito User Pools that let each tenant register its own external OIDC or SAML IdP can be abused when security checks are placed in the wrong Lambda triggers. The core issue is Cognito's federated login execution order: `PreSignUp_ExternalProvider` is the only trigger that runs before the user object is persisted, while checks deferred to `PostConfirmation`, `PreAuthentication`, or some `TokenGeneration` paths can block a session but still leave a durable "ghost" identity in the pool with no automatic rollback. A malicious tenant-controlled IdP can exploit this by registering via `CreateIdentityProvider`, completing the OIDC code flow, influencing claims returned from `/userinfo`, and causing Cognito to create identities that later interact with password reset, impersonation, or other account-linked platform features. The article also maps risky `event.triggerSource` differences such as `InboundFederation_ExternalProvider` versus `PreAuthentication_Authentication`, showing how first-login and returning-login paths often enforce different constraints and create subtle authorization gaps in SaaS SSO designs.

[Read original article](https://blog.doyensec.com/2026/05/05/cloudsectidbits-masso-cognito-sso.html){: .btn .btn-primary }
