---
layout: post
title: "When it Snows it Pours – Anatomy of a ServiceNow Red Team"
date: 2026-08-28 08:47:38 +0300
categories: [RSS]
tags: [servicenow, privilege-escalation, lateral-movement, cloud-security, role-abuse]
toc: true
---

MDSec details a multi-stage ServiceNow exploitation chain that enables full control over enterprise IT infrastructure in real-world red team engagements. Initial access is gained via session hijacking (cookie dumping) or exposed credentials like MID server `config.xml` files; attackers then chain role inheritance through `catalog_admin`, `import_admin`, and `action_designer` roles to execute Glide scripts at elevated (system) privilege levels. The authors identified 24+ distinct ServiceNow roles vulnerable to privilege escalation and describe how high-privileged roles like `user_criteria_admin` can be abused to escalate further—notably, they highlight pre-authentication RCE zero-days (Smashing the ServiceNow Sandbox and BodySnatcher) that bypass the need for initial credentials entirely. This is critical for defenders because ServiceNow is widely deployed in enterprise environments, yet organizations often lack visibility into these escalation paths, allowing attackers to hide undetected within the platform.

[Read original article](https://www.mdsec.co.uk/2026/08/when-it-snows-it-pours-anatomy-of-a-servicenow-red-team/){: .btn .btn-primary }
