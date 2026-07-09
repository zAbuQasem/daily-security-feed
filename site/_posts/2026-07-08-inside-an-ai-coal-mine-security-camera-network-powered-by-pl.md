---
layout: post
title: "Inside an AI coal mine security camera network powered by plaintext passwords"
date: 2026-07-08 17:07:38 +0300
categories: [RSS]
tags: [authentication, credentials, access-control, critical-infrastructure]
toc: true
---

Project DigiCoal, an AI-powered security camera system deployed across 7 Coal India Ltd. mines, contained multiple critical authentication and authorization failures. An unauthenticated API endpoint exposed the complete user list with plaintext passwords (many duplicated and weak), and the frontend enforced access control via local storage only, allowing trivial privilege escalation by modifying browser state. The attack chain bypassed all authentication layers to grant full access to alert dashboards and camera feeds spanning all monitored mines. Responsibly disclosed to India's CERT-IN in August 2025 and confirmed fixed by November 2025.

[Read original article](https://eaton-works.com/2026/07/08/coal-india-camera-hack/){: .btn .btn-primary }
