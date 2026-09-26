---
title: TRACE-PILOT-002 — Noncontrolling Prestage Origin Evidence Manifest
owner: Creative Director
status: Superseded audit evidence — no selection or downstream credit
pilot_id: TRACE-PILOT-002
methodology_version: TRACE v0.3
methodology_frozen_commit: 0b74489e083d58d8037129247399d3cece866de6
preregistration_anchor: f5f3291fc3de64673f8e66ed85e139f2ec9df535
recorded_at: 2026-09-25
---

# TRACE-PILOT-002 — Noncontrolling Prestage Origin Evidence Manifest

## Controlling classification

The origin-search fragments listed below are preserved as `NONCONTROLLING-PRESTAGE` audit evidence. They cannot establish a final Gate 0 disposition, platform selection, expression-family ID, Source Decode Card, grammar finding, recipe support, maturity credit, or transfer input.

The searches began before the preregistered raw-frame stage had closed through DTC store 12 and before the cross-platform family-deduplication checkpoint. Most source-side searches also used domain-scoped web search without first documenting that Etsy native search was unavailable, although Etsy native search had been accessible during raw capture. Those two defects make every apparent disposition in these fragments provisional and superseded.

No timestamp, result, or decision is rewritten as though it occurred in the controlling stage.

## Preserved fragments

| Fragment | Scope actually completed | Rows after header | Recorded disposition summary | Controlling limitation |
|---|---|---:|---|---|
| [`TRACE-PILOT-002-Origin-Etsy-Badge-01-04.csv`](./TRACE-PILOT-002-Origin-Etsy-Badge-01-04.csv) | Badge ranks 1–4 | 228 | 1 apparent `IP-EXCLUDED`; 3 apparent `IP-QUARANTINE` | Searches and decisions closed before DTC raw-frame close; source-side runs used domain-scoped web search rather than Etsy native. |
| [`TRACE-PILOT-002-Origin-Etsy-Badge-05-08.csv`](./TRACE-PILOT-002-Origin-Etsy-Badge-05-08.csv) | Badge ranks 5–8 | 227 | 2 apparent `IP-EXCLUDED`; 2 apparent `IP-QUARANTINE` | Prestage and non-native; exact per-query timestamps were not captured and remain unavailable. |
| [`TRACE-PILOT-002-Origin-Etsy-Review-01-05.csv`](./TRACE-PILOT-002-Origin-Etsy-Review-01-05.csv) | Review-depth ranks 1–5 | 283 | 4 apparent `IP-QUARANTINE`; 1 apparent `ELIGIBLE` | Prestage and non-native. The apparent eligible result is not a clearance and receives no selection credit. |
| [`TRACE-PILOT-002-Origin-Etsy-Badge-09-13.csv`](./TRACE-PILOT-002-Origin-Etsy-Badge-09-13.csv) | Badge rank 9 only | 48 | 1 apparent `IP-EXCLUDED` | Six runs were completed before the stage stop. Open-web discovery queries for ranks 10–13 had launched but were intentionally omitted; no decisions were made for them. |

The files retain blank expression-family IDs and contain no SDC IDs. Their local result notes remain evidence of what was inspected, not authority to select or decode a product.

## Chronology and containment

| Event | UTC fact |
|---|---|
| DTC raw-frame stage closed through store 12 | `2026-09-25T18:28:03.414Z` |
| Badge 1–4 searches | `2026-09-25T18:19:40.361Z` through `2026-09-25T18:19:44.811Z` |
| Badge 1–4 record decisions closed | `2026-09-25T18:23:23.183Z` |
| Review-depth searches | `2026-09-25T18:20:38Z` through `2026-09-25T18:21:44Z` |
| Review-depth record decisions closed | `2026-09-25T18:25:06.459Z` |
| Badge 5–8 exact query times | `UNAVAILABLE — not captured; completed before the sequence stop` |
| Badge 5–8 record close | `2026-09-25T18:26:26Z` |
| Badge 9 record decision closed | `2026-09-25T18:28:37.195Z` |

The DTC raw-scan operator performed no origin search and created no SDC. Prestage Etsy findings were not used to choose stores, alter locked store order, change raw capture depth, replace a store, or inspect beyond raw rank 24. The DTC capture therefore remains mechanically independent of the prestage findings.

## Required controlling rerun

Before any final selection or SDC:

1. freeze and validate every raw platform frame and DTC candidate register;
2. record the cross-platform family-deduplication checkpoint;
3. restart each frozen Etsy queue at rank 1 without using the apparent prestage outcomes to skip or favor a candidate;
4. execute fresh Etsy-native and separate open-web searches, reviewing and recording the first 10 organic results or a truthful shorter/blocked state with exact UTC timestamps;
5. make new controlling Gate 0 decisions after those compliant runs;
6. continue each queue deterministically until its quota is filled or its frozen candidates are exhausted.

If an Etsy-native required run is blocked, record the bounded access failure. Do not silently substitute the earlier domain-scoped evidence. A required unresolved run cannot support `ELIGIBLE`.

## Separate panel-lock sequence deviation

The DTC panel was locked after the Amazon and Etsy raw captures rather than in the preregistered step-2 position. It was nevertheless locked before any DTC ranked-result or product-detail inspection, and membership was based on store/assortment criteria only. This fact requires an explicit no-effect finding at the checkpoint; this manifest does not itself resolve that deviation.

