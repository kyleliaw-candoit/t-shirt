---
title: TRACE-PILOT-002 — Post-Raw Global Expression-Family Deduplication Checkpoint
owner: Creative Director
status: Closed — controlling origin stage authorized after barrier time
pilot_id: TRACE-PILOT-002
methodology_version: TRACE v0.3
methodology_frozen_commit: 0b74489e083d58d8037129247399d3cece866de6
preregistration_anchor: f5f3291fc3de64673f8e66ed85e139f2ec9df535
etsy_raw_anchor: 0b5898974c8902495d49da65a2c6c9029ed93c99
dtc_raw_anchor: aba5883aaef91caff27148f317ed872f5fd357f2
dedup_started_at_utc: UNAVAILABLE — exact start was not captured; work began after the DTC raw anchor
dedup_closed_at_utc: 2026-09-25T18:50:26.170Z
---

# TRACE-PILOT-002 — Post-Raw Global Expression-Family Deduplication Checkpoint

## Barrier decision

All accessible raw frames were frozen before this checkpoint closed:

- Amazon's complete-frame prerequisite was already closed `BLOCKED`, with zero observations;
- Etsy contributed 144 organic observations resolving to 109 unique listing IDs;
- DTC contributed 288 product observations resolving to 284 canonical within-store families after four duplicate-family collapses;
- DTC raw capture through store 12 closed at `2026-09-25T18:28:03.414Z`.

The controlling post-raw origin stage is authorized only for searches started after `2026-09-25T18:50:26.170Z`. Every earlier origin fragment remains `NONCONTROLLING-PRESTAGE` under the [prestage manifest](./TRACE-PILOT-002-Noncontrolling-Prestage-Origin-Manifest.md).

No expression-family or SDC ID was assigned before this barrier. Final EF numbering remains governed by the earliest qualifying canonical observation after Gate 0 closes.

## Inputs and comparison method

| Input | Frozen evidence |
|---|---|
| Etsy raw frame and queue | [`TRACE-PILOT-002-Etsy-Scan-Register.csv`](./TRACE-PILOT-002-Etsy-Scan-Register.csv) and [`TRACE-PILOT-002-Etsy-Candidate-Selection.md`](./TRACE-PILOT-002-Etsy-Candidate-Selection.md), frozen at `0b5898974c8902495d49da65a2c6c9029ed93c99` |
| DTC raw frame and queues | [`TRACE-PILOT-002-DTC-Scan-Register.csv`](./TRACE-PILOT-002-DTC-Scan-Register.csv) and [`TRACE-PILOT-002-DTC-Candidate-Selection.md`](./TRACE-PILOT-002-DTC-Candidate-Selection.md), frozen at `aba5883aaef91caff27148f317ed872f5fd357f2` |

The review compared all 109 unique Etsy listings against all 284 canonical DTC families: 30,956 cross-platform pairs. It used immutable observation IDs, normalized titles and handles, shop/store identity, captured thumbnail metadata, and targeted side-by-side primary-image inspection for plausible subject/action/composition overlaps. The 22 frozen Etsy queue listings also received a direct comparison against the 248 DTC title/thumbnail survivors.

This was a family-identity check, not an origin search. It did not decide ownership, licensing, copying direction, eligibility, or provenance.

## Confirmed cross-platform expression-family relation

| Etsy occurrence | DTC occurrence | Relation | Sampling consequence |
|---|---|---|---|
| `TRACE-P002-OBS-ETSY-01-MR-10` — [Bigfoot Dandelion](https://www.etsy.com/listing/4520342710/comfort-colors-bigfoot-dandelion-shirt), Etsy badge queue rank 4 | `TRACE-P002-OBS-DTC-S12-04` — [Blowing Wishes](https://slothhikingclub.com/products/blowing-wishes-t-shirt), DTC store 12 queue rank 4 | `CLONE-LINKED SAME EXPRESSION FAMILY` — both preserve a shaggy Bigfoot upper-body/profile facing right, holding and blowing a dandelion at its mouth, seeds drifting right, in a monochrome etched treatment. Line details and product mockups differ, so identical artwork is not asserted. | Count at most one eligible expression family across these occurrences. If either occurrence is reached, its controlling origin screen must record the cross-platform join. Do not allow the two observations to become independent recipe support. |

No EF ID is assigned at this checkpoint because neither occurrence has a final qualifying canonical observation. If the family later qualifies, attach the same EF ID to both observations and designate one canonical observation under the frozen earliest-qualifying rule.

The relation is conservative contamination control, not an infringement finding.

## Related but separate family

`TRACE-P002-OBS-ETSY-03-MR-07` depicts a ghost blowing dandelion wishes and shares the action/composition scaffold with the confirmed Bigfoot family. The substituted subject creates a separate expression family under TRACE v0.3. It may later be considered for a template-cluster relationship only if it independently clears Gate 0; this checkpoint gives it no downstream credit.

## Rejected same-family leads

Targeted review found materially different wording, subjects, actions, or compositions for the following broad-theme overlaps, so they remain separate families:

- Etsy cryptid ensemble versus DTC Mothman;
- Etsy Medusa versus DTC Medusa;
- Etsy raccoon expressions versus DTC `Everything Is Trash Raccoon`;
- Etsy butterfly/botanical designs versus DTC insect/botanical designs;
- Etsy `Salty Girl` versus DTC `Live Salty`;
- Etsy painter cats versus DTC cat art;
- Etsy Bigfoot/dandelion versus DTC `Stay Wild` lighthouse/shoreline;
- Etsy beer/brewery, Jesus, and science designs versus differently expressed DTC themes.

These negative findings prevent broad subject coincidence from collapsing distinct commercial expressions.

## Commercial-source relation without family merge

Etsy shop `CrazyDogTshirts` and DTC store `Crazy Dog T-Shirts` normalize to the same commercial-source identity:

- Etsy `TRACE-P002-OBS-ETSY-04-TR-07` — `Funny Dad Jokes T-Shirt`;
- DTC store `P002-DTC-S05` — 24 frozen raw observations.

No DTC title, handle, or available thumbnail metadata matches the Etsy `Funny Dad Jokes` expression, so no product-family join is established. If distinct families from these surfaces later qualify, apply the single three-family commercial-source cap across the shared source identity.

## Limitations

- Exact dedup start time was not separately captured. Work began only after the DTC raw anchor; the exact close/barrier time is preserved.
- DTC thumbnail alternative text is incomplete, so targeted visual review focused on plausible metadata leads rather than claiming a pixel-level comparison of all 30,956 pairs.
- Family identity can be revised if a controlling origin search reveals a stronger clone or exact-art relation. Preserve existing observation IDs and add the relation; do not renumber prior observations.
- This checkpoint does not clear any source. All queue heads remain origin-pending.

## DTC panel-lock chronology no-effect finding

The DTC panel lock occurred after the Amazon and Etsy raw captures rather than in preregistered step 2. The deviation did not alter DTC membership or rank capture:

- all 12 stores, their order, eligibility bases, broad collections, and expected sort checks were committed before any DTC ranked-result or product-detail inspection;
- ranked DTC capture began at `2026-09-25T18:13:28.478Z`, after the panel lock artifact;
- the DTC operator received no prestage origin outcome and performed no origin search or SDC work;
- no store was replaced, reordered, or allowed to contribute beyond raw rank 24.

The panel remains valid for this run. The out-of-sequence lock is retained as `P002-FRI-009` and must remain visible at the five-card checkpoint, but the evidence establishes no effect on eligibility, selection order, identity, lineage, or downstream support.

## Authorized next action

Restart controlling origin work from rank 1 in each frozen queue. Use the source platform's native search when available plus a separate open-web search, record the first 10 organic results or a truthful shorter/blocked state with exact UTC timestamps, and close new Gate 0 decisions only from those compliant post-barrier runs.

