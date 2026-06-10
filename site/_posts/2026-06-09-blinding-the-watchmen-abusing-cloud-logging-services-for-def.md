---
layout: post
title: "Blinding the Watchmen: Abusing Cloud Logging Services for Defense Evasion and Visibility"
date: 2026-06-09 22:00:21 +0300
categories: [RSS]
tags: [cloud, aws, gcp, defense-evasion, logging]
toc: true
---

Palo Alto Unit 42 analysis of attack techniques targeting cloud logging services (AWS CloudTrail and Google Cloud Logging) used for defense evasion and reconnaissance. Attackers with minimal IAM permissions can stop logging via cloudtrail:StopLogging or logging.sinks.update, delete log storage destinations, disable log routers, exploit attacker-controlled encryption keys, or poison logs to evade detection by SIEM, SOAR, and CSPM systems. The techniques demonstrate how a compromised account with basic permissions can blind an organization's entire audit trail, extending attacker dwell time and preventing incident response. This represents a critical gap in cloud security posture where logging infrastructure itself is the attack surface.

[Read original article](https://unit42.paloaltonetworks.com/cloud-logging-defense-evasion/){: .btn .btn-primary }
