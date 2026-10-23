---
layout: post
title: "The Current Landscape of OAuth Attacks"
date: 2026-10-22 17:00:25 +0300
categories: [RSS]
tags: [oauth, authentication, session-fixation, token-hijacking, mfa-bypass]
toc: true
---

As organizations deploy MFA, attackers have shifted from stealing credentials to hijacking OAuth tokens, which bypass MFA (since authentication already occurred) and survive password resets via long-lived refresh tokens. The article details three authorization-layer vulnerabilities: Cross-User OAuth Session Fixation (COSF) allows attackers to use frozen sessions to capture victim tokens; Cross-Tenant Client ID Confusion enables malicious tenants to impersonate trusted apps in shared OAuth-as-a-Service vaults; and Cross-Connector Account Takeover reroutes authorization flows to attacker control. OAuth tokens grant persistent, durable access across all connected services without triggering credential-based alerts, making lateral movement and data exfiltration difficult to detect. Defense strategies include disabling end-user app consent, enforcing admin approval workflows, monitoring authorization code events, and auditing redirect_uri configurations.

[Read original article](https://unit42.paloaltonetworks.com/current-landscape-oauth-attacks/){: .btn .btn-primary }
