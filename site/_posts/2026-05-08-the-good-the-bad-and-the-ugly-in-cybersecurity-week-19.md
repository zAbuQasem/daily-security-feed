---
layout: post
title: "The Good, the Bad and the Ugly in Cybersecurity – Week 19"
date: 2026-05-08 13:00:14 +0300
categories: [RSS]
tags: [cloud, credential-theft, pan-os, rce, threat-intel]
toc: true
---

This weekly roundup aggregates three security developments: U.S. sentencing actions against a Karakurt extortion negotiator and two facilitators of DPRK laptop-farm operations, SentinelLABS reporting on the PCPJack cloud worm, and an alert on Palo Alto PAN-OS zero-day CVE-2026-0300. The most technical section describes PCPJack as a multi-stage credential theft framework that starts from a bootstrap.sh dropper, pulls Python modules from attacker-controlled S3, steals cloud keys, Kubernetes service account tokens, Docker secrets, SaaS tokens, and crypto wallets, then laterally moves by exploiting Next.js and WordPress flaws while scanning exposed Docker, Redis, RayML, and MongoDB services before exfiltrating encrypted loot via Telegram. The PAN-OS item highlights an actively exploited unauthenticated buffer overflow in the User-ID Authentication Portal/Captive Portal that can yield root-level remote code execution on internet-exposed firewalls. Overall, the post is useful as an operational digest of current threats and mitigations, but it is a summary article rather than a deep original technical write-up.

[Read original article](https://www.sentinelone.com/blog/the-good-the-bad-and-the-ugly-in-cybersecurity-week-19-7/){: .btn .btn-primary }
