---
layout: post
title: "Chaining ISC DHCP Server Features for Unauthenticated Root Remote Code Execution"
date: 2026-05-02 16:56:50 +0300
categories: [RSS]
tags: [rce, dhcp, omapi, unauthenticated, linux]
toc: true
---

The post shows how ISC DHCP Server can be driven to unauthenticated root RCE by chaining intended features rather than exploiting memory corruption. If `omapi-port` is exposed without an `omapi-key`, an attacker can use OMAPI to create or modify a host object and set its `statements` attribute, which is parsed with the normal `dhcpd.conf` grammar and can include `execute()` directives. By binding that injected host entry to a chosen `hardware-address` and then sending a DHCP DISCOVER with a matching `chaddr`, the server resolves the host during normal lease processing and runs the embedded command via `fork()`/`execvp()` as the `dhcpd` process user, typically root. The research is notable because it turns documented management and configuration behavior in a still-widely-deployed, root-running DHCP daemon into a practical network-to-root execution path.

[Read original article](https://shells.systems/chaining-isc-dhcp-server-features-for-unauthenticated-root-remote-code-execution/){: .btn .btn-primary }
