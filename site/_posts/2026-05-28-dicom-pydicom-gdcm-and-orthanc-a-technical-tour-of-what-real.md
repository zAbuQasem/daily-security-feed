---
layout: post
title: "DICOM, Pydicom, GDCM, and Orthanc: A technical tour of what really happens in the heap"
date: 2026-05-28 10:00:52 +0300
categories: [RSS]
tags: [heap-overflow, out-of-bounds-write, dicom, medical-imaging, rce]
toc: true
---

Cisco Talos presents a technical white paper demonstrating a heap overflow vulnerability in the DICOM image parsing stack, specifically targeting the Orthanc open-source PACS server during file upload. The attack exploits malformed DICOM files to trigger an out-of-bounds write in the heap, leveraging the inherent complexity of the DICOM format and the fact that PACS systems automatically ingest files received over the network — making this a zero-interaction attack surface. The research covers the internals of multiple DICOM parsers (pydicom, GDCM, Orthanc) and maps how malformed data flows through the heap to reach the vulnerable write primitive. This is high-impact research given that hospitals depend on DICOM-based PACS infrastructure and a remotely-triggered memory corruption in an image ingestion path could lead to full server compromise.

[Read original article](https://blog.talosintelligence.com/dicom-pydicom-gdcm-and-orthanc-a-technical-tour-of-what-really-happens-in-the-heap/){: .btn .btn-primary }
