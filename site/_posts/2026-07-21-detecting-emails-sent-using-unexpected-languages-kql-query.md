---
layout: post
title: "Detecting Emails Sent Using Unexpected Languages (+KQL Query)"
date: 2026-07-21 07:46:36 +0300
categories: [RSS]
tags: [detection, email, threat-hunting, kql]
toc: true
---

Sergio Albea presents a KQL-based threat hunting technique that detects emails where the detected language doesn't match the expected language(s) for the sender's IP country of origin (e.g., Japanese email from a Spanish IP). The query uses geoIP geolocation to determine sender country, compares the detected email language against a CSV reference mapping, and flags mismatches. This is designed as a hunting signal to combine with other indicators (newly registered domains, suspicious infrastructure, auth anomalies) rather than a standalone detector — individually weak signals, collectively powerful. The author provides production-ready KQL code with tuning guidance for email volume thresholds, country exclusions, and trusted domain whitelisting, making it immediately applicable in Microsoft 365 / Defender environments.

[Read original article](https://detect.fyi/detecting-emails-sent-using-unexpected-languages-kql-query-41c435e3176b?source=rss----d5fd8f494f6a---4){: .btn .btn-primary }
