---
layout: post
title: "Living Off the Pipeline: Defending Against CI/CD Subversion"
date: 2026-05-15 13:00:53 +0300
categories: [RSS]
tags: [ci-cd, supply-chain, teamcity, gitlab]
toc: true
---

SentinelOne surveys how attackers are increasingly compromising the software delivery pipeline itself rather than only poisoning downstream dependencies, focusing on build servers, self-hosted runners, service accounts, and developer workstations as trusted execution points. The article highlights several concrete mechanisms: exploitation of a vulnerable self-hosted TeamCity server to create a benign-looking build configuration that ran on a trusted agent with SYSTEM privileges, compromise of a GitLab service account token to submit malicious Ansible projects that the pipeline executed automatically, and malware registering attacker-controlled systems as self-hosted GitHub runners to gain persistent access to repositories, secrets, and workflows. It also covers developer-targeting intrusion paths such as the Contagious Interview campaign, where fake troubleshooting commands installed malware and exposed SSH keys, repo access, and tokens that could be used to pivot into CI/CD systems. The main defensive point is that malicious pipeline activity often looks identical to legitimate build behavior—package downloads, script execution, artifact movement, and workflow triggers—so organizations need controls around runner registration, service identities, workflow authorization, and privileged automation rather than relying on traditional malware-style detection alone.

[Read original article](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/){: .btn .btn-primary }
