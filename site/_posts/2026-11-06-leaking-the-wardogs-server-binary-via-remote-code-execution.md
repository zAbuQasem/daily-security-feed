---
layout: post
title: "Leaking the WARDOGS Server Binary via Remote Code Execution on a Hosting Partner"
date: 2026-11-06 00:00:00 +0300
categories: [RSS]
tags: [rce, api-key, supply-chain, lateral-movement]
toc: true
---

A command injection vulnerability in a WARDOGS hosting provider's custom game server management panel allowed remote code execution through shell metacharacters in server launch parameters (StartupMap, Hostname, WDRcon_Password). The attacker exploited lateral filesystem access between containerized game instances to download the production WARDOGS server binary—a protected private artifact—along with a hardcoded Pragma backend API token granting permissions to globally ban players, manipulate currency, XP, gold bars, and vault data across WARDOGS' shared economy. The researcher demonstrated full impact by running a private server with admin cheats (god mode, infinite ammo, teleportation) and responsibly disclosed the vulnerability to both WARDOGS and the hosting provider before public disclosure.

[Read original article](https://samcurry.net/wardogs){: .btn .btn-primary }
