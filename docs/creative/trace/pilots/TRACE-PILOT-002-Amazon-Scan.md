---
title: TRACE-PILOT-002 — Amazon Scan
owner: Creative Director
status: Complete — Amazon prerequisite blocked; zero selections
pilot_id: TRACE-PILOT-002
run_mode: CALIBRATION-FIRST-ACTUAL
methodology_version: TRACE v0.3
methodology_frozen_commit: 0b74489e083d58d8037129247399d3cece866de6
preregistration_commit: f5f3291
observation_date: 2026-09-25
access_window_start_utc: 2026-09-25T17:59:25.333Z
access_window_end_utc: 2026-09-25T17:59:56.790Z
---

# TRACE-PILOT-002 — Amazon Scan

## Controlling rule

TRACE-PILOT-002 preregistered the Amazon Men's and Women's Top-100 pages as one complete-frame prerequisite. The frozen rule requires:

1. one direct retrieval per official Top-100 URL;
2. one ordinary signed-out browser retrieval per pool;
3. at most one ordinary browser reload per failed pool in the same execution window; and
4. zero Amazon selections from both pools if either complete Top 100 is unavailable.

No rank may be reconstructed from snippets, isolated product pages, caches, or third-party lists. This record follows the preregistration at commit `f5f3291` and TRACE v0.3 frozen at commit `0b74489e083d58d8037129247399d3cece866de6`.

## Frozen pools

| Pool ID | Pool | Official URL | Required frame | Final disposition |
|---|---|---|---:|---|
| `TRACE-P002-POOL-AMZ-M` | Amazon Best Sellers — Men's Novelty T-Shirts | <https://www.amazon.com/Best-Sellers-Men%27s-Novelty-T-Shirts/zgbs/fashion/9056987011> | Complete Top 100 | `BLOCKED` |
| `TRACE-P002-POOL-AMZ-W` | Amazon Best Sellers — Women's Novelty T-Shirts | <https://www.amazon.com/Best-Sellers-Women%27s-Novelty-T-Shirts/zgbs/fashion/9056923011> | Complete Top 100 | `BLOCKED` |

## Access-attempt register

All timestamps are UTC. The browser attempts used an ordinary unauthenticated session; no sign-in or alternate client was used. Direct retrieval and ordinary-browser retrieval were kept distinct.

| Attempt | UTC time | Pool(s) | Retrieval mode | Response | Complete frame captured? |
|---|---|---|---|---|---|
| `AMZ-A01` | 2026-09-25T17:59:25.333Z–2026-09-25T17:59:26.332Z | Men's | Direct retrieval | HTTP `503 Service Unavailable`; response contained no ranked product frame | No |
| `AMZ-A02` | 2026-09-25T17:59:25.333Z–2026-09-25T17:59:26.332Z | Women's | Direct retrieval | HTTP `503 Service Unavailable`; response contained no ranked product frame | No |
| `AMZ-A03` | 2026-09-25T17:59:37.144Z–2026-09-25T17:59:47.264Z | Men's | Ordinary signed-out browser retrieval | Amazon title `500 - Amazon.com`; visible response: “We are sorry for the inconvenience. We do not support your session or client.” The page suggested a different current browser or Amazon's mobile app. | No |
| `AMZ-A04` | 2026-09-25T17:59:37.144Z–2026-09-25T17:59:47.264Z | Women's | Ordinary signed-out browser retrieval | Amazon title `500 - Amazon.com`; same visible session/client-not-supported response | No |
| `AMZ-A05` | 2026-09-25T17:59:56.554Z–2026-09-25T17:59:56.790Z | Men's | Single permitted ordinary-browser reload | Amazon title remained `500 - Amazon.com`; same visible session/client-not-supported response | No |
| `AMZ-A06` | 2026-09-25T17:59:56.554Z–2026-09-25T17:59:56.790Z | Women's | Single permitted ordinary-browser reload | Amazon title remained `500 - Amazon.com`; same visible session/client-not-supported response | No |

Both browser tabs remained on their exact frozen official URLs after the initial retrieval and the single permitted reload. Neither response exposed any ranked cards, ranks, list-surface identifiers, or a partial traversable frame.

## Pool closeout

| Field | Men's pool | Women's pool |
|---|---|---|
| Demand signal | Unavailable | Unavailable |
| Access/render mode | `BLOCKED` | `BLOCKED` |
| Raw ranked observations captured | 0 | 0 |
| Complete-frame prerequisite | Failed | Failed |
| Expression families created | 0 | 0 |
| Product selections | 0 | 0 |
| SDCs created | 0 | 0 |
| Unused quota transferred | No | No |

The Amazon prerequisite is therefore `BLOCKED`. Under the frozen both-or-none rule, Amazon contributes **zero Men's selections and zero Women's selections** to TRACE-PILOT-002. No `TRACE-P002-OBS-AMZ-*`, expression-family, or Source Decode Card IDs were assigned because no ranked observation was captured.

## Integrity notes

- No snippets, search-engine results, cached fragments, isolated detail pages, alternate Amazon URLs, mobile-app routes, or third-party rankings were used to infer or reconstruct the Top 100.
- No retries occurred beyond the single permitted ordinary-browser reload for each failed pool.
- No products were opened, decoded, excluded, quarantined, or selected from Amazon.
- No Amazon quota was backfilled or transferred to Etsy, DTC, or the other Amazon pool.
- This is an access failure, not a statement about product eligibility or current bestseller composition.
- The independent Etsy and DTC pools may continue under their own frozen protocols; this artifact does not alter those rules.

## Amazon lane result

`BLOCKED — BOTH POOLS CONTRIBUTE ZERO SELECTIONS`
