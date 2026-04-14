---
layout: post
title: "Fixing ESC8 - Web Enrollment is enabled over HTTP and HTTPS, and Channel Binding is disabled"
date: 2026-04-14 03:12:06 +0300
categories: [RSS]
tags: [adcs, ntlm-relay, active-directory, iis, hardening]
toc: true
---

The post explains how ESC8 in Active Directory Certificate Services can turn otherwise low-value authentication coercion bugs like PetitPotam or PrintNightmare into full domain compromise. If AD CS Web Enrollment or Certificate Enrollment Web Service is exposed in its default IIS configuration, an attacker can relay a coerced NTLM authentication from a domain controller computer account to the enrollment endpoint and request a certificate as that machine. A certificate issued for the DC account gives the attacker authentication material that effectively translates into administrative control over the domain controller and broader Active Directory compromise. The mitigation is to harden the IIS sites hosting enrollment by requiring SSL and setting Extended Protection for Authentication (channel binding / EPA) to Required, which blocks HTTP relay paths and binds authentication to the TLS channel.

[Read original article](https://projectblack.io/blog/fixing-esc8-web-enrollment-is-enabled-over-http-and-https-and-channel-binding-is-disabled/){: .btn .btn-primary }
