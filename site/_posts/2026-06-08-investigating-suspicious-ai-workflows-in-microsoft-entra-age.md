---
layout: post
title: "Investigating suspicious AI workflows in Microsoft Entra Agent ID: Assistive agents"
date: 2026-06-08 15:37:01 +0300
categories: [RSS]
tags: [cloud, detection, azure, oauth]
toc: true
---

This article examines how assistive agents in Microsoft Entra perform actions on behalf of users through the 'On behalf of' (OBO) OAuth flow, which requires users to grant the `access_agent` scope to an agent blueprint principal. Authorization is limited to the intersection of the agent's permissions and the user's assigned roles—dangerous permissions like `User.ReadWrite.All` are blocked for agents, but they can still perform malicious actions within their delegated scope. The article provides concrete detection methodology through detailed Purview log analysis, showing how to identify agent-based email activity using fields like `AgentBlueprintId`, `AppAccessContext`, and `ClientAppId`. This is critical for blue teams deploying AI agents in Entra, enabling detection of unauthorized or suspicious agent behavior on an emerging attack surface.

[Read original article](https://redcanary.com/blog/threat-detection/entra-id-ai-workflows-assistive-agents/){: .btn .btn-primary }
