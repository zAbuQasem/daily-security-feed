---
layout: post
title: "Multiple Vulnerabilities in Frappe LMS Leading to Remote Code Execution"
date: 2026-09-15 15:00:54 +0300
categories: [RSS]
tags: [rce, path-traversal, xss, frappe, open-source]
toc: true
---

Frappe LMS contains two chained vulnerabilities enabling RCE from student-level access. CVE-2026-39405 is a path traversal in SCORM package upload where unsanitized chapter titles allow extraction to arbitrary directories, enabling injection of backdoored api.py. CVE-2026-34606 is stored XSS in profile bio that bypasses HTML sanitization by splitting dangerous tags across elements—BeautifulSoup's get_text() concatenates text nodes to reconstruct executable payloads like `<script>`. A student attacker embeds XSS in their bio; when an admin views the profile, it executes and allows uploading a malicious SCORM package, achieving RCE via command injection in the get_job_details endpoint.

[Read original article](https://rhinosecuritylabs.com/research/multiple-vulnerabilities-in-frappe-lms-leading-to-remote-code-execution/){: .btn .btn-primary }
