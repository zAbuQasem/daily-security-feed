---
layout: post
title: "Business CTF 2022: H2 Request Smuggling and SSTI - Phishtale"
date: 2026-04-16 03:12:31 +0300
categories: [RSS]
tags: [http2, request-smuggling, ssti, twig, rce]
toc: true
---

This write-up covers a CTF challenge built around chaining an HTTP/2 request smuggling flaw with a Twig sandbox escape to achieve remote code execution. The first stage abuses H2 request desynchronization to smuggle a request past frontend/backend parsing boundaries, letting the attacker reach unintended application behavior that is not exposed through normal routing. The second stage turns that access into server-side template injection, then bypasses Twig Sandbox Policy restrictions using known sandbox-escape techniques associated with CVE-2021-36740 and CVE-2022-23614. Although framed as a challenge, it is technically useful because it demonstrates a realistic multi-step exploit chain across protocol parsing and template engine isolation rather than a single isolated bug.

[Read original article](https://rayhan0x01.github.io/ctf/2022/11/17/phishtale-business-ctf-2022-web-writeup.html){: .btn .btn-primary }
