---
layout: post
title: "AWS Security Digest #263 - Going fwd"
date: 2026-06-01 12:00:00 +0300
categories: [RSS]
tags: [aws, supply-chain, cloud, digest, lambda]
toc: true
---

AWS Security Digest #263 is a curated newsletter covering recent AWS security developments. The main feature provides detailed post-mortem analysis of the TeamPCP supply chain campaign that compromised the Trivy scanner, cascaded through multiple tools, and resulted in a CERT-EU breach where a single stolen AWS API key from the poisoned Trivy build chain on March 19 led to compromise of Europa's hosting account and 350GB data dump affecting 42 EU Commission entities. The digest highlights the Zapocalypse research showing how to extract AWS Lambda session tokens from /proc/self/mem to pivot into ECR and extract secrets from container images, and features the Shadow Asset Scanner integration with AWS Strands security agents for attack chain correlation. Additional sections aggregate AWS security blog posts, service announcements (Shield DDoS flow logs, Organizations CloudTrail events, GuardDuty S3 backup scanning), and community discussions on serverless security scanning challenges.

[Read original article](https://awssecuritydigest.com/past-issues/aws-security-digest-263){: .btn .btn-primary }
