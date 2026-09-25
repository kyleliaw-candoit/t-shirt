---
title: TRACE-PILOT-002 — Execution Schema and Recorded Friction
owner: Creative Director
status: Active execution clarification — non-rule-changing
pilot_id: TRACE-PILOT-002
methodology_version: TRACE v0.3
methodology_frozen_commit: 0b74489e083d58d8037129247399d3cece866de6
preregistration_anchor: f5f3291fc3de64673f8e66ed85e139f2ec9df535
created_at: 2026-09-25T18:04:20Z
---

# TRACE-PILOT-002 — Execution Schema and Recorded Friction

## Purpose and authority

This artifact records operational schemas and deterministic interpretations needed to execute and audit `TRACE-PILOT-002` consistently.

It is **not** an amendment to the frozen TRACE v0.3 methodology or the committed Pilot 002 preregistration. Ranked inspection began before this artifact was created. Therefore, every item below is classified as non-selection-changing execution friction or record-format clarification.

This artifact may not change:

- platform, pool, cohort, or store eligibility;
- frozen traversal or selection order;
- quotas, caps, or no-transfer rules;
- Gate 0 dispositions or provenance thresholds;
- the no-backfill rule;
- expression-family membership;
- SDC eligibility, primary-outcome rules, or downstream support;
- the five-card stop/go rubric.

If this artifact conflicts with the frozen methodology or preregistration, the frozen source controls and the conflict must be logged as unresolved friction. No interpretation below may be used to rescue, replace, reorder, or newly qualify a source.

## Recorded friction and controlling interpretations

| ID | Execution friction | Controlling interpretation | Why it is non-selection-changing |
|---|---|---|---|
| `P002-FRI-001` | The preregistration requires review and recording of the first 10 organic origin-search results, while also referring to representative URLs. | Record every reviewed organic result by ordinal. Separately mark the subset used as representative evidence. | The frozen query types, surfaces, depth, and Gate 0 rules do not change; this only makes the required review auditable. |
| `P002-FRI-002` | Origin searches need explicit completeness states when a surface returns fewer than 10 results or cannot be accessed. | Use `COMPLETE-10`, `EXHAUSTED-LT10`, or `BLOCKED`. `EXHAUSTED-LT10` means every organic result exposed by that search was recorded. A required unresolved search cannot be treated as complete; the frozen rule that `UNRESOLVED` provenance maps to `IP-QUARANTINE` still controls. | These states document whether the preregistered search occurred; they do not add a new fallback or eligibility exception. |
| `P002-FRI-003` | The Etsy observation-ID pattern contains an undefined `<scan>` token. | Use the fixed `S01`–`S12` map below. Render an organic observation as `TRACE-P002-OBS-ETSY-S<scan>-O<organic-ordinal>`, for example `TRACE-P002-OBS-ETSY-S01-O01`. | The codes merely name the already frozen query-major sequence. Search order and organic ordinals remain unchanged. |
| `P002-FRI-004` | The DTC observation-ID pattern `S<store>` could be misread as adding an extra `S` to an already prefixed store ID. | Render the store token once: `TRACE-P002-OBS-DTC-S01-<raw-rank>` through `TRACE-P002-OBS-DTC-S12-<raw-rank>`. Example: `TRACE-P002-OBS-DTC-S01-01`. | This resolves formatting only. Locked store order and raw rank are unchanged. |
| `P002-FRI-005` | The checkpoint must prove that final Gate 0 closed before decoding, but the required fields do not name an SDC-creation timestamp. | Record the UTC timestamps defined below and enforce their temporal ordering. | Additional audit timestamps do not alter any evidence or decision. |
| `P002-FRI-006` | Expression-family IDs are join keys, but the preregistration also says they are assigned by the earliest qualifying canonical observation. | For every family that receives an EF ID, attach the same ID to every occurrence judged to be the same commercial expression. Identify the canonical observation separately; only it carries selection fields. The earliest qualifying canonical observation controls eligible-family numbering, and later exclusions or discoveries never renumber an existing ID. | This preserves the frozen numbering and selection rule while making all duplicate occurrences traceable. An EF join never confers eligibility or selection. |
| `P002-FRI-007` | Amazon's frozen both-or-none prerequisite failed, leaving both Amazon decode lanes empty. | Apply the preregistered repeating-lane order with the two empty Amazon lanes skipped, as specified below. | The preregistration already requires skipping empty lanes. This records the deterministic consequence of the Amazon result. |
| `P002-FRI-008` | The preregistration captures and closes the raw platform selections before the five-card checkpoint, so the pause is early in decoding rather than early in collection. | Preserve the committed execution order. The checkpoint occurs before SDC 6 and mechanism clustering, not before completion of the frozen raw scan. | This is disclosure of the preregistered sequence, not a change to it. |

## Fixed Etsy scan-code map

The `<scan>` token in Etsy observation IDs uses this map. Query order and sort order are exactly the preregistered query-major sequence.

| Scan code | Query | Sort | Organic observation example |
|---|---|---|---|
| `S01` | `graphic t shirt` | `Most relevant` | `TRACE-P002-OBS-ETSY-S01-O01` |
| `S02` | `graphic t shirt` | `Top reviews` | `TRACE-P002-OBS-ETSY-S02-O01` |
| `S03` | `funny t shirt` | `Most relevant` | `TRACE-P002-OBS-ETSY-S03-O01` |
| `S04` | `funny t shirt` | `Top reviews` | `TRACE-P002-OBS-ETSY-S04-O01` |
| `S05` | `novelty t shirt` | `Most relevant` | `TRACE-P002-OBS-ETSY-S05-O01` |
| `S06` | `novelty t shirt` | `Top reviews` | `TRACE-P002-OBS-ETSY-S06-O01` |
| `S07` | `text t shirt` | `Most relevant` | `TRACE-P002-OBS-ETSY-S07-O01` |
| `S08` | `text t shirt` | `Top reviews` | `TRACE-P002-OBS-ETSY-S08-O01` |
| `S09` | `illustrated t shirt` | `Most relevant` | `TRACE-P002-OBS-ETSY-S09-O01` |
| `S10` | `illustrated t shirt` | `Top reviews` | `TRACE-P002-OBS-ETSY-S10-O01` |
| `S11` | `retro graphic t shirt` | `Most relevant` | `TRACE-P002-OBS-ETSY-S11-O01` |
| `S12` | `retro graphic t shirt` | `Top reviews` | `TRACE-P002-OBS-ETSY-S12-O01` |

`O01` through `O12` are organic ordinals only. Interleaved ads are recorded separately and never consume or change an organic ordinal.

## DTC observation-ID interpretation

Use:

> `TRACE-P002-OBS-DTC-S01-<raw-rank>`

through:

> `TRACE-P002-OBS-DTC-S12-<raw-rank>`

The store token appears once. Raw rank is the preserved position in the locked store's broad, verified native-best-selling frame and should be zero-padded from `01` through `24`. A failed store is represented in the store/pool audit record and does not receive a fabricated product observation.

## Origin-search register schema

The origin-search register uses three joined logical tables. They may be maintained in one Markdown artifact or as separate CSV files as long as the keys, values, and row granularity below are preserved.

### A. Search runs

One row represents one query on one required surface.

| Field | Requirement |
|---|---|
| `ORIGIN_RUN_ID` | Unique immutable run ID. |
| `PILOT_ID` | `TRACE-PILOT-002`. |
| `OBSERVATION_ID` | Candidate's canonical observation ID when assigned. |
| `EXPRESSION_FAMILY_ID` | Joined family ID when assigned; do not use it as an eligibility flag. |
| `QUERY_TYPE` | `EXACT-WORDING`, `CLEAN-TITLE`, or `COMPOSITION`. |
| `APPLICABILITY` | `REQUIRED` or `N/A-NO-TEXT`; only `EXACT-WORDING` may be N/A for a genuinely text-free design. |
| `NA_REASON` | Required when applicability is N/A. |
| `SURFACE_ROLE` | `SOURCE-NATIVE`, `SOURCE-DOMAIN`, or `OPEN-WEB`. `SOURCE-DOMAIN` is the preregistered fallback when native search is unavailable. |
| `ENGINE_OR_SURFACE` | Search engine or native-search surface used. |
| `SOURCE_DOMAIN` | Source platform/domain being searched, when applicable. |
| `QUERY_EXACT` | Exact executed query string, including quotation marks when used. |
| `SEARCH_URL` | Search-result URL when available. |
| `SEARCHED_AT_UTC` | UTC timestamp of the search. |
| `LOCALE` | Country/language or other known locale context. |
| `ACCESS_STATUS` | `COMPLETE-10`, `EXHAUSTED-LT10`, or `BLOCKED`. |
| `ORGANIC_TARGET` | `10` for required searches. |
| `ORGANIC_COUNT` | Number of organic results actually reviewed and recorded. |
| `ANALYST` | Analyst identity. |
| `RUN_NOTES` | Access limitation, exhaustion basis, or other factual note. |

For a text-bearing design, completeness normally requires six run rows: three query types across the source-native/domain role and a separate open-web role. For a text-free design, retain explicit N/A records for the wording query and complete the title and composition searches on both required surface roles.

### B. Organic results

One row represents one reviewed organic result. Sponsored results and other nonorganic modules do not consume an organic ordinal.

| Field | Requirement |
|---|---|
| `ORIGIN_RUN_ID` | Foreign key to the search-run row. |
| `RESULT_ORDINAL` | Organic ordinal `1` through `10`, or through the exhausted shorter result set. |
| `RESULT_URL` | URL shown in the result. |
| `FINAL_URL` | Resolved destination when opened; otherwise explicitly unavailable with reason. |
| `DOMAIN_OR_PLATFORM` | Result domain or marketplace. |
| `RESULT_TITLE` | Displayed title. |
| `SELLER_CREATOR` | Seller, publisher, creator, or rights source shown, when available. |
| `SELLER_RELATION` | `SOURCE-SELLER`, `SAME-COMMERCIAL-SOURCE`, `UNRELATED-SELLER`, or `UNKNOWN`. |
| `VISIBLE_PUBLICATION_DATE` | Visible publication/listing date, or explicit unavailable value. |
| `MATCH_ELEMENTS` | Matching wording, subject, action, composition, punchline, artwork, or source indicators. |
| `MATERIAL_MATCH` | `YES`, `NO`, or `UNCERTAIN`. |
| `TRACEABLE_SOURCE` | `YES`, `NO`, or `UNRESOLVED`, with the basis in notes. |
| `MATCH_NOTES` | Factual comparison with the candidate. |
| `REPRESENTATIVE` | `YES` when this result is cited in the candidate-level decision; otherwise `NO`. |

Record every reviewed organic result. Representative evidence is a marked subset, not a substitute for the complete first-10 record.

### C. Candidate decisions

One row represents the completed origin-screen and Gate 0 provenance decision for one expression family.

| Field | Requirement |
|---|---|
| `EXPRESSION_FAMILY_ID` | Candidate family. |
| `CANONICAL_OBSERVATION_ID` | Selected canonical observation, if any. |
| `EXPECTED_RUNS` | Count expected under text/no-text applicability. |
| `COMPLETED_RUNS` | Runs completed as `COMPLETE-10` or `EXHAUSTED-LT10`. |
| `NA_RUNS` | Explicitly inapplicable wording runs for a text-free design. |
| `BLOCKED_RUNS` | Required runs that remained blocked. |
| `CROSS_SELLER_RECURRENCE` | `YES`, `NO`, or `UNCERTAIN`. |
| `TRACEABLE_CREATOR_OR_RIGHTS_SOURCE` | `YES`, `NO`, or `UNRESOLVED`. |
| `PROVENANCE_CONFIDENCE` | `HIGH`, `MEDIUM`, `LOW`, or `UNRESOLVED`. |
| `PROVENANCE_BASIS` | Reasoned basis tied to run/result IDs. |
| `FINAL_GATE0_DISPOSITION` | One normative TRACE v0.3 disposition. |
| `DECISION_RATIONALE` | Application of the frozen decision rule. |
| `DECIDED_BY` | Gate 0 reviewer. |
| `DECIDED_AT_UTC` | Final Gate 0 closeout timestamp. |
| `LIMITATIONS` | Remaining evidentiary limitations. |

## Gate 0 and SDC timestamps

For every SDC candidate, record:

| Field | Meaning |
|---|---|
| `ORIGIN_SCREEN_STARTED_AT_UTC` | First required origin-query execution time. |
| `ORIGIN_SCREEN_CLOSED_AT_UTC` | Time the required search record and comparison were completed. |
| `FINAL_GATE0_CLOSED_AT_UTC` | Time the reviewer recorded the controlling final disposition. |
| `SDC_CREATED_AT_UTC` | Time semantic decoding began or the SDC was first created, whichever occurred first. |
| `CHECKPOINT_REVIEWED_AT_UTC` | Time the independent five-card review closed. |

For an eligible SDC, audit the ordering:

> `ORIGIN_SCREEN_CLOSED_AT_UTC <= FINAL_GATE0_CLOSED_AT_UTC <= SDC_CREATED_AT_UTC < CHECKPOINT_REVIEWED_AT_UTC`

If the ordering cannot be demonstrated, record the limitation and treat the checkpoint field as failed rather than reconstructing a convenient timestamp.

## Expression-family join and canonical observation

- `OBSERVATION_ID` identifies one captured occurrence.
- `EXPRESSION_FAMILY_ID` joins occurrences judged to be the same commercial expression.
- `CANONICAL_OBSERVATION_ID` identifies the single observation that represents an eligible selected family.
- `SDC_ID` joins only to an eligible family and its canonical observation.

For an assigned EF ID, apply it to every known same-expression occurrence, including duplicate or audit-only occurrences. This does not change any occurrence's surface status, disposition, first-occurrence credit, eligibility, or selection state.

Only the canonical observation carries selection fields. An excluded, quarantined, partial-surface, or duplicate observation may share an EF ID but never inherits the canonical observation's eligibility or downstream credit. Later audit events preserve the existing IDs and add the controlling disposition; they do not trigger renumbering.

## Deterministic SDC order after the Amazon block

The frozen Amazon both-or-none prerequisite failed, so Amazon Men's and Amazon Women's contribute no selections and both decode lanes are empty. Applying the preregistered repeating-lane order with empty lanes skipped produces:

| SDC ordinal | Source selection |
|---|---|
| `TRACE-P002-SDC-001` | Etsy `RECENT-SALES-BADGE` selection 1 |
| `TRACE-P002-SDC-002` | Etsy `ITEM-REVIEW-DEPTH` selection 1 |
| `TRACE-P002-SDC-003` | DTC selection 1 in frozen eligible-store order |
| `TRACE-P002-SDC-004` | Etsy `RECENT-SALES-BADGE` selection 2 |
| `TRACE-P002-SDC-005` | Etsy `ITEM-REVIEW-DEPTH` selection 2 |

If a listed lane has no finalized eligible selection at that ordinal, skip it and continue through the same repeating order until five eligible SDCs are created or all completed accessible lanes are exhausted. A skip must be supported by the finalized platform register; it cannot be based on convenience, decode quality, or anticipated mechanism value.

Pause after `TRACE-P002-SDC-005`. Do not create SDC 6 or begin mechanism clustering until the independent checkpoint record is complete.

## Classification statement

All schemas, codes, timestamps, joins, and ordering consequences in this artifact are classified as **non-selection-changing execution friction**. They make frozen decisions identifiable and auditable; they do not revise the methodology or preregistration. Any later finding that one of these interpretations changes eligibility, order, identity, lineage, or downstream support must be logged as material friction and evaluated under the preregistered `STOP-REVISE` rule.
