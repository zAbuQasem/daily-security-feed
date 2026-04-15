---
layout: post
title: "The n8n n8mare: How threat actors are misusing AI workflow automation"
date: 2026-04-15 12:54:03 +0300
categories: [RSS]
tags: [phishing, malware, rmm, threat-intel, email]
toc: true
---

Cisco Talos documents how attackers are abusing n8n’s public webhook feature to turn trusted n8n.cloud subdomains into phishing and malware-delivery infrastructure. In the observed campaigns, email links to n8n-hosted webhooks returned self-contained HTML/JavaScript phishing pages with CAPTCHA gates, then fetched payloads from attacker-controlled hosts while making the download appear to originate from the n8n domain; one sample dropped a fake "DownloadedOneDriveDocument.exe" that unpacked a modified Datto RMM agent, created a scheduled task, connected to a relay on centrastage.net, and deleted its staging files. A second campaign used a malicious MSI protected with the Armadillo packer to install a trojanized ITarian Endpoint Management RMM instance via msiexec.exe, alongside Python-based data exfiltration and a fake installer progress UI. Talos also highlights webhook-driven tracking and fingerprinting via embedded content in emails, showing how legitimate automation platforms can help adversaries evade reputation-based filtering and tailor follow-on payloads to the victim environment.

[Read original article](https://blog.talosintelligence.com/the-n8n-n8mare/){: .btn .btn-primary }
