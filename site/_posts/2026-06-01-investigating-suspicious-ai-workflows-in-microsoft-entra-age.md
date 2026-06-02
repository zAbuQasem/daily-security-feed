---
layout: post
title: "Investigating suspicious AI workflows in Microsoft Entra Agent ID: Agent’s user account"
date: 2026-06-01 13:04:01 +0300
categories: [RSS]
tags: [cloud, detection, microsoft, ai, threat-hunting]
toc: true
---

Red Canary provides a detection engineering guide for investigating suspicious Microsoft Teams activity originating from Entra ID agent user accounts—AI agents that can interact with licensed products like Teams and email on behalf of automated workflows. The article demonstrates how to correlate Purview audit logs (MessageReported, MessageSent, MessageCreatedHasLink operations) to trace a suspicious Teams message containing a link back to its agent sender, including IP address, AAD session ID, and unique token ID. Agent users extend the Graph API user resource type but require association with an agent identity at provisioning, creating a new identity attack surface where agents could be compromised to send phishing links or exfiltrate data via Teams. The post includes raw JSON log samples and field mapping guidance for building detection pipelines around user-reported content in Teams, applicable to organizations deploying AI agents with interactive user access.

[Read original article](https://redcanary.com/blog/threat-detection/entra-id-ai-workflows-teams/){: .btn .btn-primary }
