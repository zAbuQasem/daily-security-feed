---
layout: post
title: "Keys to the Kingdom Live Stripe Credentials Exposed via Unauthenticated OAuth Endpoint"
date: 2026-05-12 11:55:00 +0300
categories: [RSS]
tags: [oauth, stripe, api, infoleak, credentials]
toc: true
---

The write-up describes an unauthenticated information disclosure bug in a SaaS platform where a simple GET request to `/api/oauth/provider/` returned the full OAuth configuration for every configured third-party integration. The JSON response exposed live production secrets including client IDs, client secrets, authorization and token endpoints, redirect URIs, and Stripe publishable keys across multiple environments, with no auth bypass or user interaction required. In practical terms, this gave an external attacker the material needed to impersonate the application to integrated providers, abuse payment workflows, and potentially obtain downstream access depending on each provider's OAuth flow and trust model. The finding is technically straightforward but operationally severe because the root cause was a publicly reachable API endpoint leaking high-value integration secrets at platform scope rather than a single tenant or sandbox environment.

[Read original article](https://labs.cognisys.group/posts/Keys-to-the-Kingdom-Live-Stripe-Credentials-Exposed-via-Unauthenticated-OAuth-Endpoint/){: .btn .btn-primary }
