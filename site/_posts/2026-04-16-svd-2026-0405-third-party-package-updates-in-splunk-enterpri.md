---
layout: post
title: "SVD-2026-0405: Third-Party Package Updates in Splunk Enterprise - April 2026"
date: 2026-04-16 03:12:32 +0300
categories: [RSS]
tags: [splunk, package-updates, openssl, protobuf, cve]
toc: true
---

Splunk's April 2026 advisory is a bundled dependency-remediation notice for Splunk Enterprise rather than a root-cause write-up, but it is still operationally useful because it maps affected product versions to fixed releases. The update rolls protobuf to 5.29.6 for Splunk Secure Gateway, PostgreSQL to 17.7 in Splunk Enterprise 10.2.2 and 10.0.5, azure-core to 1.38.0 in 9.4.10, and OpenSSL to 1.0.2zo for the bundled libcrypto/libssl libraries in 9.4.10 and 9.3.11. Splunk also identifies where some vulnerable components live on disk, including `$SPLUNK_HOME/etc/apps/splunk_secure_gateway/lib/protobuf` and `$SPLUNK_HOME/lib/libcrypto.so.1.0.0` / `$SPLUNK_HOME/lib/libssl.so.1.0.0`, which helps defenders verify exposure in installed environments. There is no exploit-chain analysis or vulnerability internals here, so the main value is patch prioritization and dependency inventory for teams running affected Splunk Enterprise branches.

[Read original article](https://advisory.splunk.com//advisories/SVD-2026-0405){: .btn .btn-primary }
