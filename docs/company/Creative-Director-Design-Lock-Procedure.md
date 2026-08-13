---
title: Creative Director Design Lock Procedure
owner: Creative Director
status: Proposed
version: 0.1
last_updated: 2026-08-12
---

# Creative Director Design Lock Procedure

## Purpose

This procedure defines when a T-shirt design may be considered `LOCKED` and how the exact approved visual is preserved so the design can be recovered across chats, sessions, or future Creative Director work.

The goal is simple:

> **A design is not locked until the exact approved visual is archived with its lock record.**

A written description alone is not sufficient because small changes in typography, scale, spacing, color, or composition can materially change a shirt.

---

## Lock Requirements

A design may be marked `LOCKED` only when all of the following exist in the same reviewable branch / pull request:

1. founder approval of the specific visual execution,
2. a lock-registry entry describing the decisions that must not drift,
3. the exact approved visual asset stored in the repository at its canonical path,
4. a SHA-256 hash of that exact asset recorded in the registry,
5. verification that the repository asset hash matches the approved source asset hash.

If any of these are missing, use `APPROVED — ARCHIVE PENDING`, not `LOCKED`.

---

## Canonical Asset Rule

For a locked design, the repository visual asset is authoritative for composition.

If prose conflicts with the stored visual, the visual wins unless the founder explicitly approves a revision.

A proposed change to a locked design should become a new version or sibling concept rather than silently replacing the approved asset.

---

## One-Design-at-a-Time Rule

During active Creative Director execution:

1. develop one design,
2. founder reviews it,
3. archive and verify the approved asset,
4. mark the design `LOCKED`,
5. only then move to the next design.

This prevents batch-generation or later edits from accidentally changing work that has already been approved.

---

## Asset Verification

Use SHA-256 as a practical file-integrity fingerprint.

Matching hashes confirm that the repository PNG is byte-for-byte identical to the founder-approved source render.

Hash verification does not judge creative quality. It only proves file identity.

---

## Stop Rule

Do not merge a design-lock PR while an intended locked asset is still absent from the repository.

If the binary cannot be added in the current tool environment, keep the PR draft and explicitly list the missing asset paths and expected hashes until the upload is completed and verified.
