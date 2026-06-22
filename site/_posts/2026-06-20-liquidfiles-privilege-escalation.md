---
layout: post
title: "Liquidfiles Privilege Escalation"
date: 2026-06-20 12:31:46 +0300
categories: [RSS]
tags: [privesc, authorization, cve, logic-bug, web]
toc: true
---

LiquidFiles contains a privilege escalation vulnerability (CVE-2026-12673) where a Domain Admin in a secondary domain can escalate themselves or users to System Admin. The authorization check in the `limit_create_for_admins` and `limit_update_for_admins` controller methods fails to validate that non-sysadmin users cannot grant `admin_level=5` (System Admin) privileges in secondary domains, only preventing `admin_level=4` (Domain Admin) escalation. An attacker can bypass the check by directly modifying the `group[admin_level]` parameter to 5 in a POST or PATCH request to `/admin/groups/groupslug`, escalating a secondary user to full system administrator. The article includes code analysis, step-by-step exploitation walkthrough, and the vendor's corrected implementation using a `permitted_admin_level?` method that enforces privilege ceiling checks.

[Read original article](https://projectblack.io/blog/liquidfiles-privilege-escalation/){: .btn .btn-primary }
