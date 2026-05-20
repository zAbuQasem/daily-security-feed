---
layout: post
title: "How OLTs may have exposed entire ISP networks"
date: 2026-05-18 22:00:00 +0300
categories: [RSS]
tags: [rce, isp, network-infrastructure, command-injection, pre-auth]
toc: true
---

Quarkslab describes a pre-authentication takeover chain against VSOL GPON OLTs and the vendor’s Cloud EMS fleet manager that could let an attacker move from an exposed access device to control of an ISP’s broader FTTH infrastructure. The OLT bugs are unauthenticated command injections in traceroute and TACACS+ authentication functionality, reachable via SNMP and web endpoints such as /action/tracert.html and /action/main.html, with exploitation occurring inside binaries including gpond, hostapp, and vsapp. The Cloud EMS side adds unauthenticated information disclosure plus an unrestricted arbitrary file upload that allows deployment of a JSP webshell on Tomcat, giving attackers a central management foothold over all managed OLTs. The post also notes shared default credentials hardcoded in firmware and documentation, which amplifies compromise at scale across multiple models. This is high-impact infrastructure research because it combines edge-device RCE, weak credential hygiene, and fleet-manager compromise into a realistic path for full ISP network takeover.

[Read original article](http://blog.quarkslab.com/how-olts-may-have-exposed-entire-isp-networks.html){: .btn .btn-primary }
