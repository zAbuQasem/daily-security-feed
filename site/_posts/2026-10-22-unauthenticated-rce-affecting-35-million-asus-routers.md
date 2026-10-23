---
layout: post
title: "Unauthenticated RCE affecting 35 million ASUS routers"
date: 2026-10-22 00:00:00 +0300
categories: [RSS]
tags: [rce, command-injection, auth-bypass, router, network]
toc: true
---

An unauthenticated remote code execution chain affecting 35 million ASUS routers released since 2018. A command injection vulnerability in the NTP server configuration handler accepts shell metacharacters (e.g., `;telnetd -l/bin/sh -p9999;`) within the 32-character ntp_server0 parameter, which is then passed unsanitized to nslookup via the doSystem wrapper. An authentication bypass in the OAuth token refresh endpoint (/asusrouter_request_access_token.cgi) allows attackers to forge valid admin tokens by encrypting a timestamp and router MAC with a blank key when providing an invalid device_id, since the code initializes the shared secret to an empty string before checking if the device_id exists. The exploit requires prior mobile app pairing to have occurred on the target router; attackers can alternatively enable SSH and inject public keys. ASUS declined to patch within the 90-day disclosure window, requesting an additional 30-day extension which the researcher declined.

[Read original article](https://mrbruh.com/asusrouter/){: .btn .btn-primary }
