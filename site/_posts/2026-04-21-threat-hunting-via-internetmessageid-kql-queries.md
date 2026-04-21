---
layout: post
title: "Threat Hunting via InternetMessageId (+ KQL Queries)"
date: 2026-04-21 03:12:37 +0300
categories: [RSS]
tags: [email, threat-hunting, kql, m365, phishing]
toc: true
---

The article explores Microsoft 365 threat hunting techniques that use the email InternetMessageId field as a detection signal instead of relying only on subjects, sender domains, or other higher-level metadata. It shows KQL queries over EmailEvents and EmailUrlInfo that normalize the Message-ID, split the local part from the domain, measure local-part length, and look for malformed IDs or embedded strings that may correlate with spam, phishing, or unusual sending infrastructure. The most useful case is hunting for Microsoft-generated "odspnotify" message IDs, where the author parses semicolon- and hyphen-delimited components to extract message type, correlation data, tenant identifiers, routing hints, and activity IDs, then joins that data with URLs and sender context. The practical value is in building language-agnostic detections for SharePoint/OneDrive sharing emails and one-time passcode delivery messages, which can help identify phishing and MFA-code theft activity that would be harder to catch with subject-based rules alone.

[Read original article](https://detect.fyi/threat-hunting-via-internetmessageid-kql-queries-240d32e6f330?source=rss----d5fd8f494f6a---4){: .btn .btn-primary }
