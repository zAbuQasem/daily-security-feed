---
layout: post
title: "Detecting the Klue supply chain attack in Salesforce instances"
date: 2026-06-22 00:00:00 +0300
categories: [RSS]
tags: [supply-chain, oauth, salesforce, detection, cloud]
toc: true
---

The Klue supply chain attack exploited a dormant OAuth credential to harvest Salesforce tokens and exfiltrate CRM data across multiple customer instances. The threat actor (Icarus group) used Python scripts with REST API queries against the `/services/data/v59.0/query/` endpoint, leveraging QueryMore to retrieve >2000 records per request and targeting objects including Opportunity, Case, Task, Lead, Contact, and Account. The article provides concrete detection guidance: identifying Klue Battlecards connected app activity in LoginEvent logs, detecting OAuth refresh token usage, and recognizing anomalous API exception patterns and large-scale data access spikes. This is an active threat with ongoing extortion campaigns—essential for SaaS-centric organizations using third-party integrations.

[Read original article](https://securitylabs.datadoghq.com/articles/detecting-the-klue-supply-chain-attack-in-salesforce/){: .btn .btn-primary }
