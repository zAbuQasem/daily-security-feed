---
layout: post
title: "Disclosure: Teachable's CDN Is Stealing From Teachers"
date: 2026-05-13 00:00:00 +0300
categories: [RSS]
tags: [s3, cloudfront, misconfiguration, paywall-bypass, asset-exposure]
toc: true
---

The post discloses a Teachable CDN misconfiguration where `uploads.teachablecdn.com` exposes the first page of an S3 bucket listing for `lecture_attachments` through CloudFront, even though direct access to the underlying bucket is denied. Any `Key` value returned in the XML listing can be appended to the CDN hostname to download the corresponding file, which lets unauthenticated users retrieve paid course materials and other creator-uploaded assets. The author notes that query parameters do not pass through cleanly enough to make the full bucket trivially enumerable, but the impact is amplified because the exposed listings were crawlable and had already been indexed by major search engines. Teachable reportedly fixed access for `digital-products` by requiring temporary signed access, but `attachments` remained exposed after a 90-day disclosure window, leaving creators vulnerable to paywall bypass and IP theft.

[Read original article](https://taggart-tech.com/20260513-teachable-disclosure/){: .btn .btn-primary }
