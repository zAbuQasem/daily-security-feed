---
layout: post
title: "SpooNMAP Grows Up: Findings, Local LLM Detection, and a Whole Lot Less Waiting"
date: 2026-08-25 04:00:00 +0300
categories: [RSS]
tags: [reconnaissance, tools, network-scanning]
toc: true
---

TrustedSec released a major update to SpooNMAP, a masscan+Nmap wrapper that now generates severity-sorted findings reports by running context-aware NSE scripts against discovered services. The tool detects configuration weaknesses including anonymous FTP, weak SSH ciphers, SMBv1, unencrypted RDP, expired certificates, LDAP without signing/channel binding, anonymous LDAP enumeration, default SNMP credentials, and unauthenticated VNC. A significant addition is Local LLM detection covering Ollama, OpenAI-compatible endpoints, Gradio, and KoboldCpp, flagged as HIGH/MEDIUM severity. The release includes 15 custom NSE scripts for coverage gaps (RAKP hash capture from IPMI/BMC, DameWare CVE-2019-3980, cups-browsed CVE-2024-47176), improved host discovery with IDS-aware rate limiting, and resume/checkpoint functionality for interrupted scans.

[Read original article](https://trustedsec.com/blog/spoonmap-grows-up-findings-local-llm-detection-and-a-whole-lot-less-waiting){: .btn .btn-primary }
