---
title: TRACE-PILOT-002 — Recovery Checkpoint 2026-09-25
pilot_id: TRACE-PILOT-002
status: PARTIAL RESUMPTION — origin queues open; five-SDC checkpoint not reached
recorded_at_utc: 2026-09-26T00:04:01.447109Z
recovered_local_head: c28da5e
verified_remote_calibration_head: 5f760cb679f2b29b53edc87aaee367a68f9e1c56
verified_main_head: d12ad66fc21e09616f7f650306c074410a224d65
methodology_frozen_blob: e6ce1dac883877455a4e915251821f4997006bbc
---

# Recovery result

The previous working checkout survived at `/workspace/scratch/4fef3b6613a3/trace-v03-calibration-repo`, branch `docs/trace-v03-calibration`. Its working tree was clean at recovery. Git fetch and GitHub reads verified main and the remote calibration branch. Main contains merged PR 114. The remote calibration branch stopped at the five-card template commit; three later local commits had not reached that remote.

| Recoverable component | Exact state at recovery |
|---|---|
| Preregistration | `f5f3291fc3de64673f8e66ed85e139f2ec9df535` |
| Frozen methodology | Commit `0b74489e083d58d8037129247399d3cece866de6`; current file blob matches the frozen blob exactly |
| Amazon | Both-or-none prerequisite BLOCKED; zero observations/selections; closed decision retained |
| Etsy frame | 12 complete surfaces; 144 organic occurrences; 109 unique listings; frozen queues of 17 badge and 5 review-depth candidates |
| DTC frame | All 12 locked stores complete; 288 raw product observations; 284 canonical within-store families; no reranking or replacement required |
| Prestage origin evidence | Four CSV fragments, 786 rows total, covering badge 1–9 and review-depth 1–5; expressly NONCONTROLLING-PRESTAGE |
| Global deduplication | Closed `2026-09-25T18:50:26.170Z`; Bigfoot/dandelion cross-platform relation retained |
| Controlling origin register | Header only at recovery |
| Final eligible selections / EF IDs | None recorded |
| SDCs | Five empty templates; zero completed cards; no checkpoint decision |

Recovered unpushed commits, in order:

1. `0b5898974c8902495d49da65a2c6c9029ed93c99` — Etsy frame and prestage audit evidence.
2. `aba5883aaef91caff27148f317ed872f5fd357f2` — complete DTC raw frame.
3. `c28da5e` — closed global family-deduplication barrier.

No additional controlling post-barrier origin artifacts were found in the inspected workspace. Transient browser state or unrecorded reasoning is not treated as recovered evidence. The earlier conversational report of only seven DTC stores was stale relative to the saved 12-store register.

# Fresh work completed

The controlling origin register now records 12 required runs, 120 reviewed result entries, and two decisions. All recorded query times follow the dedup barrier. Exact wording, cleaned title, and composition were searched on native source surfaces and separately on the open web. Full native-search product variants count as origin occurrences only, never independent creative support.

| Frozen queue position | Observation | Decision | Basis |
|---|---|---|---|
| Etsy badge 1 | `TRACE-P002-OBS-ETSY-01-MR-06` | `IP-EXCLUDED` | Fresh candidate image and native/open-web evidence identify recognizable Morton umbrella-girl mascot dependence; first-party Morton history confirms brand association. |
| DTC S01 queue 1 | `TRACE-P002-OBS-DTC-S01-01` | `IP-QUARANTINE` | Recurrent exact slogan, book subject and anti-censorship punchline; seller authorship claim does not establish origin. Other inspected compositions differ; no copied-art or same-family assertion is made. |

Primary Morton corroboration: https://www.mortonsalt.com/article/happy-100th-birthday-morton-salt-girl/ (opened during recovery).

Boredwalk comparisons: https://www.goddessandgrove.com/products/ban-the-fascists-save-the-books-sticker and https://www.etsy.com/listing/1421103423/ban-the-fascists-save-the-books-funny (opened during recovery).

These are research contamination controls, not ownership or infringement conclusions. The S01 quarantine is conservative; no product is selected in its place yet.

# Capture qualifications

- Initial recovery discovery searches were exploratory. Only the six explicitly indexed runs per candidate in the controlling CSV count toward the decisions.
- Initial unscoped Etsy extraction included recommendation-module links after partially loaded results. This was caught before any decision. The controlling captures use the observed `data-results-grid-container`, exclude ads, and include the first ten organic grid cards after ordinary loading.
- The raw-discovery digital-download filter was omitted for controlling origin searches, so origin research could expose digital artwork too. No frozen raw sampling filter was changed.
- Open-web ordinals describe the search service's returned order, not a separately verified native search-engine SERP. Locale was not exposed and is recorded unavailable.
- The three supplementary JSON files preserve factual result identifiers and titles; the CSV is the controlling run/result/decision record.
- UTC crossed into September 26 during recovery; the raw observation date remains September 25 and the local Chicago date remained September 25. No historical time was reconstructed.

# Exact continuation

No completed raw scan should be repeated. Resume controlling origin work as follows:

1. Etsy badge queue rank 2: `TRACE-P002-OBS-ETSY-11-MR-08`, Three Raccoons. Continue in frozen order until six eligible families or exhaustion.
2. Etsy review-depth queue rank 1: `TRACE-P002-OBS-ETSY-06-TR-02`, Cat Guitarist. The lane has five candidates total and cannot borrow quota.
3. DTC store S01 queue rank 2: `TRACE-P002-OBS-DTC-S01-02`, Men's Someday We'll All Be Dead T-Shirt. Open its detail and collect attributable evidence before origin closure. Then continue within frozen raw ranks; proceed to S02 only after S01 selection/exhaustion is resolved. Later stores remain untouched by controlling origin research.
4. Apply the existing global dedup relations, final Gate 0, immutable IDs and source caps. Keep Amazon closed at zero. Never backfill a post-selection failure or move quota.
5. Create eligible SDCs in the frozen repeating lane order only after required eligibility closure. The five templates remain empty; do not treat them as five completed cards.
6. Conduct the prescribed independent five-card review before SDC 6 or clustering. No PASS, STOP-REVISE, or STOP-INSUFFICIENT-SAMPLE result is asserted by this partial recovery checkpoint.

# Publication restriction

An attempted push of the recovered commits to the existing calibration branch was rejected by automatic approval review: the reviewer requires explicit user authorization to publish/synchronize the TRACE artifacts to GitHub. The rejected action was `git push origin HEAD:docs/trace-v03-calibration`. It was not retried through another tool. No PR, merge, methodology amendment, commercial promotion, ad action or spend occurred.

Local research and commits are possible, but GitHub durability of the recovered/new records is pending that approval. This publication restriction does not establish a research failure or a five-card stop/go outcome.

# Validation

- Frozen methodology blob matches exactly.
- Both raw registers are byte-identical to recovered `c28da5e`.
- Controlling register: 12 runs + 120 results + 2 decisions; every run joins to ordinals 1–10.
- All controlling runs postdate the dedup barrier.
- No EF, selected-family, or SDC identity was assigned.
- Original prestage fragments and five-card templates are unchanged.
