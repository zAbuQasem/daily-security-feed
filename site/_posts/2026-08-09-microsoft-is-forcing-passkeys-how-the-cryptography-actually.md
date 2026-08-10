---
layout: post
title: "Microsoft Is Forcing Passkeys: How the Cryptography Actually Works"
date: 2026-08-09 05:00:00 +0300
categories: [RSS]
tags: [authentication, cryptography, webauthn, passkeys]
toc: true
---

Microsoft Entra ID is forcing a migration from SMS/voice MFA to passkeys, with full deprecation by February 2027. The article provides a technical deep-dive on how passkeys work: leveraging public-key cryptography (FIDO2/WebAuthn), where a private key sealed on the device signs server-issued challenges without ever exposing the secret, and the server verifies via the stored public key—eliminating the shared-secret model entirely. Passkeys are inherently phishing-resistant because they're origin-bound; a key created for login.microsoft.com cryptographically refuses to sign for spoofed domains. The article distinguishes device-bound passkeys (TPM, secure enclave, YubiKey—hardware-attested, highest assurance) from synced passkeys (cloud-encrypted across devices, more convenient but larger trust boundary), a choice enterprises will make via the `passkeyType` setting. This represents a significant practical shift for organizations still on SMS/voice, requiring new infrastructure decisions around authenticator types and provider selection.

[Read original article](https://thalpius.com/2026/08/09/microsoft-is-forcing-passkeys-how-the-cryptography-actually-works/){: .btn .btn-primary }
