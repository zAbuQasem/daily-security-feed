---
layout: post
title: "The New Hotness in Phishing: Device Code Attacks in M365"
date: 2026-07-21 04:00:00 +0300
categories: [RSS]
tags: [m365, identity, phishing, authentication, bec]
toc: true
---

TrustedSec describes device code phishing attacks exploiting the OAuth 2.0 device authorization grant (RFC 8628) to compromise M365 accounts with unusual effectiveness. The attacker initiates the device code flow targeting a trusted first-party client ID (e.g., Microsoft Office), persuades the victim to visit the authentic `microsoft.com/devicelogin` and enter the code, then captures OAuth tokens when the victim completes legitimate sign-in. The attack bypasses Conditional Access policies because authentication originates from Microsoft's infrastructure and generates legitimate MFA prompts; the victim sees nothing suspicious, leaving only an OAuth token in attacker-controlled logs. The technique has surfaced repeatedly across BEC and M365 incident response engagements and is automated by tools like TokenTacticsV2 and roadtx, enabling broad-scale exploitation.

[Read original article](https://trustedsec.com/blog/the-new-hotness-in-phishing-device-code-attacks-in-m365){: .btn .btn-primary }
