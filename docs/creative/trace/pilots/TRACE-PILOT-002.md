---
title: TRACE-PILOT-002 — v0.3 Calibration-First Actual Run
owner: Creative Director
status: Preregistered — ranked-product inspection not begun
pilot_id: TRACE-PILOT-002
run_mode: CALIBRATION-FIRST-ACTUAL
methodology_version: TRACE v0.3
methodology_frozen_commit: 0b74489e083d58d8037129247399d3cece866de6
methodology_frozen_blob: e6ce1dac883877455a4e915251821f4997006bbc
preregistered_at: 2026-09-25T17:55:37Z
observation_date: 2026-09-25
checkpoint_target_sdcs: 5
---

# TRACE-PILOT-002 — v0.3 Calibration-First Actual Run

## Authorization and integrity attestation

The Founder authorized TRACE v0.3 for a calibration-first actual run on 2026-09-25.

No current ranked marketplace or store-product surface was inspected for this run before this preregistration was committed. TRACE-PILOT-001 observations remain historical evidence only; they do not prequalify, select, or clear a TRACE-PILOT-002 source.

The Git commit that first introduces this file is the preregistration anchor. After ranked inspection begins, preserve these rules unchanged. Record deviations and methodology friction; do not silently repair the frozen procedure.

## Objective and stop/go design

Execute a real broad winner scan under TRACE v0.3. Preserve qualifying sources and Source Decode Cards as usable creative intelligence if the first five cards pass the calibration gate.

Pause before SDC 6 and before mechanism clustering.

- `PASS`: continue this same run; retain the first five cards as real run evidence.
- `PASS-WITH-RECORDED-FRICTION`: continue only when the friction changes no eligibility, ordering, identity, lineage, or downstream-support decision.
- `STOP-REVISE`: stop before SDC 6 and clustering; preserve evidence and freeze a corrected methodology version before resumption.
- `STOP-INSUFFICIENT-SAMPLE`: fewer than five eligible families across completed accessible pools; do not cluster.

## Sample and no-backfill rule

Target 36 eligible expression families:

- Amazon Men's Novelty T-Shirts: 6;
- Amazon Women's Novelty T-Shirts: 6;
- Etsy `RECENT-SALES-BADGE`: 6;
- Etsy `ITEM-REVIEW-DEPTH`: 6;
- Shopify/DTC: 12, at most one from each locked store.

Never transfer quota between pools, cohorts, stores, or platforms. Never replace a post-selection Gate 0 failure. Traversing farther through a frozen complete pool before its selection closes to bypass exclusions or duplicates is ordinary deterministic selection, not backfill.

## Execution order

1. Commit this preregistration and no-inspection attestation.
2. Lock all 12 DTC stores in a timestamped panel artifact before opening any DTC ranked-result surface.
3. Capture raw frames in this order:
   1. Amazon Men's Top 100;
   2. Amazon Women's Top 100;
   3. Etsy query-major, `Most relevant` then `Top reviews`, in the six-query methodology order;
   4. DTC stores `P002-DTC-S01` through `P002-DTC-S12`.
4. Assign immutable observation IDs at capture and global expression-family IDs after deduplication.
5. Complete all required origin searches and close final Gate 0 before platform selections are final.
6. Create SDCs in this repeating lane order, skipping empty lanes:
   1. Amazon Men;
   2. Amazon Women;
   3. Etsy badge;
   4. Etsy review-depth;
   5. DTC.
7. Stop after five eligible SDCs for the calibration checkpoint.

Within a lane, preserve the selection order defined by TRACE v0.3. Never renumber IDs after an exclusion, duplicate, failure, or later audit event.

## Platform failure rules

### Amazon

Both Top-100 frames are one complete-frame prerequisite. Attempt one direct retrieval and one ordinary signed-out browser retrieval, with at most one ordinary browser reload per failed pool in the same execution window.

If either Top 100 cannot be captured completely, preserve accessible responses as audit evidence and mark the Amazon prerequisite `BLOCKED`. Both Amazon quotas contribute zero selections. Do not reconstruct ranks from snippets, isolated pages, caches, or third-party lists.

### Etsy

Each of the 12 frozen query/sort surfaces must yield 12 organic cards under the methodology's bounded loading rule. A `PARTIAL` surface supplies audit evidence only and receives no selection or first-occurrence credit. Other complete frozen surfaces may continue. Ads are recorded separately and never occupy an organic ordinal.

For attribution tiebreaks, use:

> `EXACT` > defensible `SAME-PRINT-VARIANTS`.

`MIXED`, `SHOP-LEVEL`, and `UNCLEAR` cannot qualify.

### Shopify/DTC

Create a separate panel-lock artifact containing all 12 stores, frozen order, eligibility basis, intended broad collection, and expected native-sort verification before ranked inspection.

Capture only raw ranks 1–24, or the documented complete shorter broad collection. Rank greater than 24 is prohibited for this run. A failed locked store leaves its slot empty; do not replace the store or take a second family elsewhere.

## Origin-screen depth

Before final `ELIGIBLE`, run every applicable methodology query:

1. exact distinctive wording;
2. exact or minimally cleaned distinctive title;
3. distinctive subject/action/composition.

Review and record the first 10 organic results from:

- the source platform's native search when available, otherwise a domain-scoped web search; and
- a separate open-web search.

For a design with no text, mark exact wording `N/A — no text`; the title and composition searches remain mandatory. Record engine/surface, query, UTC time, representative URLs, material matches, and the analyst comparison. Search recurrence is contamination evidence, not an infringement finding.

## Stable identifiers

- Pool ID: `TRACE-P002-POOL-<platform/lane>`
- DTC store ID: `P002-DTC-S01` through `P002-DTC-S12`
- Observation ID:
  - Amazon: `TRACE-P002-OBS-AMZ-<M|W>-<rank>`
  - Etsy: `TRACE-P002-OBS-ETSY-<scan>-<organic-ordinal>`
  - DTC: `TRACE-P002-OBS-DTC-S<store>-<raw-rank>`
- Expression-family ID: `TRACE-P002-EF-###`, assigned by earliest qualifying canonical observation
- Source Decode Card ID: `TRACE-P002-SDC-###`, assigned in frozen decode order

Selection fields appear only on the canonical observation. All recipe and grammar joins use expression-family and SDC IDs, never mutable titles or ranks.

## Five-card checkpoint rubric

The checkpoint passes only if all five cards satisfy every condition:

1. final disposition was `ELIGIBLE` before decoding;
2. all required origin searches and a reasoned provenance basis are recorded;
3. every mandatory field is populated or explicitly marked unavailable with a reason;
4. one canonical observation-to-family-to-SDC chain is preserved;
5. observed facts and analytical hypotheses are visibly separate;
6. source-specific truth remains attached to its source niche;
7. the primary outcome is usable and not forced;
8. each `RECIPE-CANDIDATE` mechanism states frame, operation, tension, reveal, and payoff and discriminates beyond broad style or humor;
9. no excluded or quarantined source receives decode, grammar, recipe, maturity, or transfer credit;
10. no unresolved rule deviation could change selection, eligibility, identity, lineage, or downstream support.

Any failure produces `STOP-REVISE`. Do not silently alter a card, change the selection rules, backfill a removed source, create SDC 6, or begin clustering.

The independent checkpoint reviewer must verify source eligibility, origin-screen completeness, lineage joins, required-field completeness, and rubric outcome.

## Required calibration artifacts

- this preregistration;
- DTC panel lock, if the DTC lane is reached;
- raw platform scan registers, including failures and exclusions;
- origin-search register;
- first five Source Decode Cards;
- deviation and methodology-friction log;
- five-card checkpoint record and independent review;
- recommendation to continue v0.3, revise to a newly frozen version, or stop for insufficient sample.

## Authorization boundary

This run may produce creative-intelligence records and noncommercial candidate mechanisms. It does not authorize final artwork, copying, product publication, marketplace listing, legal clearance, advertising, or spending.
