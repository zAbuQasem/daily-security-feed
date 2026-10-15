---
layout: post
title: "Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant"
date: 2026-10-14 22:00:44 +0300
categories: [RSS]
tags: [fortigate, supply-chain, malware, rce, cve]
toc: true
---

Unit 42 analyzed a multi-stage intrusion against a telecommunications MSP originating in September 2024, in which attackers exploited CVE-2024-47575 against a centralized FortiManager to gain initial access and exfiltrate running configurations, cryptographic material, and management databases for 500+ managed FortiGate firewalls. Post-exploitation activities included network reconnaissance via unauthorized packet-capture rules deployed to downstream firewalls, credential brute-forcing from reversible ciphertext, and abuse of CVE-2025-61624 (FortiOS auto-script path traversal) to deploy PEERSTITCH—a novel, memory-resident ARM64 malware that achieves C2 persistence through legitimate process traffic without disk artifacts, listening ports, or overt outbound connections. The intrusion chain demonstrates sophisticated understanding of Fortinet appliance architecture and affects not only the MSP's infrastructure but also the networks of its clients. The attackers' tradecraft overlaps with suspected nation-state activity and includes credential reuse, VPN session hijacking, and lateral movement impersonating the FortiManager platform.

[Read original article](https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/){: .btn .btn-primary }
