---
title: TRACE-PILOT-001 Execution Log and Debrief
owner: Creative Director
maintainer: Knowledge Librarian
status: Pilot Complete — Revise and Retest
pilot_id: TRACE-PILOT-001
methodology_version: TRACE v0.2
methodology_frozen_commit: c383e2d90619e594b38b65dbd3508638d6e845d0
started_at: 2026-09-25
completed_at: 2026-09-25
last_updated: 2026-09-25
final_recommendation: REVISE-AND-RETEST
---

# TRACE-PILOT-001 — Execution Log and Debrief

## Decision summary

**Final recommendation: `REVISE-AND-RETEST`.**

TRACE v0.2 successfully produced an auditable Etsy sample, a partial auditable Shopify/DTC sample, and a useful record of Amazon access failure. Its IP, custom-product, review-attribution, and no-backfill safeguards materially improved source quality.

The pilot did not complete the preregistered 36-family sample. It made 22 execution-time selections, then a strict frozen-v0.2 final Gate 0 provenance and brand-dependency audit removed 17 of them from source use:

- Amazon: 0 of 12.
- Etsy: 12 selected at execution; 1 final qualifying.
- Shopify/DTC: 10 selected at execution; 4 final qualifying.
- Total: **22 execution-time selections and 5 final qualifying families out of 36**.

The 5 final eligible Source Decode Cards produced no `CORROBORATED` or `PROVISIONALLY-CORROBORATED` recipe. Concrete Semantic Resolution remains a `CANDIDATE` on one eligible DTC family, `TRACE-P001-DTC-07`; three associated source-distance tests and three source-by-seed originality comparisons remain active noncommercial diagnostics. Six other transfer tests are retained only as invalidated audit records because their recipe inputs failed Gate 0. These labels describe limited pattern support or diagnostic development in the incomplete accessible sample; they are not causal validation, internal behavioral testing, production clearance, or legal clearance.

See [Recipe Synthesis and Transfer Test](./TRACE-PILOT-001-Recipe-Synthesis-and-Transfer-Test.md) for the family ledger, maturity calculations, source prohibitions, and diagnostic transfer matrices.

## Frozen execution manifest

| Field | Frozen or executed value |
|---|---|
| Methodology | `docs/company/TRACE-Bestseller-Creative-Intelligence-Methodology.md` |
| Frozen commit | `c383e2d90619e594b38b65dbd3508638d6e845d0` |
| Market/locale | United States |
| Amazon pools | Men’s Novelty T-Shirts Top 100; Women’s Novelty T-Shirts Top 100 |
| Etsy queries | `graphic t shirt`; `funny t shirt`; `novelty t shirt`; `text t shirt`; `illustrated t shirt`; `retro graphic t shirt` |
| Etsy execution order | Query-major; `Most relevant` then `Top reviews` |
| Etsy session | Signed out; English (US); USD; ship-to Plano, Texas |
| Etsy automatic filter | `instant_download=false` |
| Shopify panel | 12 preselected stores; panel-lock timestamp was not preserved |
| Family target | 12 Amazon + 12 Etsy + 12 Shopify/DTC |
| Cross-platform backfill | Prohibited; none performed |

The Amazon execution window is preserved at approximately 15:38–15:54 UTC. Etsy and Shopify/DTC preserve the observation date but not exact UTC timestamps.

## Pool execution

| Pool | Precommitted depth | Actual ranked/organic observations | Diagnostic records | Selected at execution | Final qualifying | Status | Evidence |
|---|---:|---:|---:|---:|---:|---|---|
| Amazon Men’s Top 100 | 100 | 0 | Access responses only | 0 | 0 | `BLOCKED` | Direct retrieval returned 503; ordinary browser returned “We do not support your session or client.” |
| Amazon Women’s Top 100 | 100 | 0 | Access responses only | 0 | 0 | `BLOCKED` | Same execution blocker. |
| Etsy: 12 query/sort pools | 144 organic | 144 | 85 ads | 12 | 1 | `COMPLETE-WITH-AUDIT-REMOVALS` | [Etsy scan register](./TRACE-PILOT-001-Etsy-Scan-Register.csv) |
| Shopify/DTC: 10 successful stores | 240 raw cards | 240 | 0 | 10 | 4 | `PARTIAL-WITH-AUDIT-REMOVALS` | Embedded CSV in [Shopify/DTC scan](./TRACE-PILOT-001-Shopify-DTC-Scan-and-Decodes.md) |
| Shopify/DTC: OpenTrail | 24 intended | 0 | 1 store-failure record | 0 | 0 | `BLOCKED` | Broad ranked pool inaccessible; indexed curated collection not substituted. |
| Shopify/DTC: Two-Cross | 24 intended | 0 | 1 store-failure record | 0 | 0 | `FAILED-ELIGIBILITY` | Current store no longer exposed a qualifying tee pool; broad collection returned 502. |
| **Total** | **632 possible slots** | **384 observations** | **87 diagnostics** | **22** | **5** | **PARTIAL** | Platform depths are not comparable market shares. |

Search snippets exposed apparent Amazon exclusions such as Spider-Man, Star Wars, Dolly Parton, custom-upload products, plain basics, and mixed-design listings. They are non-sample diagnostics only: they receive no observation, family, or Source Decode Card IDs.

## Sample reconciliation

| Platform | Target qualifying families | Selected at execution | Final eligible SDCs | Audit removals | Completion |
|---|---:|---:|---:|---:|---|
| Amazon | 12 | 0 | 0 | 0 | Blocked |
| Etsy | 12 | 12 | 1 | 11 quarantined | Partial after audit |
| Shopify/DTC | 12 | 10 | 4 | 4 quarantined; 2 brand-excluded | Partial after audit |
| **Total** | **36** | **22** | **5** | **17** | **13.9% of target** |

No selected Etsy shop contributed more than two families. Shopify/DTC selected one family from each successful store at execution; six of those ten were removed by final provenance or brand-dependency audit.

## Etsy reconciliation

The Etsy register contains:

- 229 rows: 144 organic observations and 85 ads.
- 121 unique organic listing IDs.
- 23 repeated occurrences of an already observed listing ID.
- 120 deduplicated commercial expression families after collapsing one separate Pasta Pups listing into an earlier family.
- 50 execution-time eligible first-listing records: 12 selected and 38 unselected.
- 59 listing pages opened; every one of the 51 title/thumbnail-eligible fixed-design candidates was inspected.

### Execution-time first-listing disposition

| Disposition | Records | Interpretation |
|---|---:|---|
| `ELIGIBLE` | 50 | Twelve selected; 38 qualified but unselected. |
| `PRODUCT-EXCLUDED` | 36 | Custom/personalized services, add-ons, or non-fixed units. |
| `IP-EXCLUDED` | 25 | Named entertainment, music, celebrity, sports, brand, lyric, or public-fame dependence. |
| `IP-QUARANTINE` | 8 | Cause, quotation, reference origin, or artwork provenance unresolved. |
| `ATTRIBUTION-EXCLUDED` | 1 | Mixed multiple designs/outcomes. |
| Duplicate expression listing | 1 | Separate listing ID collapsed into an existing family. |

All 12 execution-time selections displayed Etsy’s official `Bestseller` badge and had item-specific review evidence. Item-review counts ranged from 9 to 814, with visible recent reviews. The final audit found materially similar phrases, subjects, or compositions across unrelated sellers for 11 selections without a traceable origin; frozen v0.2 therefore required `IP-QUARANTINE`. Only the seller-made single-word `ART` composition remained qualifying, and no post-synthesis backfill was attempted. The execution selection also excluded non-badged designs with substantially larger item histories, including counts of approximately 1.7k, 1k, 857, 518, 395, and 279.

This followed v0.2, but demonstrates that absolute badge precedence selects a recent-badge panel rather than a balanced view of recent and persistent probable winners.

## Shopify/DTC reconciliation

The embedded Shopify/DTC register contains 242 rows:

- 240 ranked product cards from 10 successful stores.
- 2 store-failure records.
- 10 execution-time selections, of which 4 remain final qualifying families.
- 4 selected-then-quarantined copy/origin records.
- 2 selected-then-excluded brand-dependent records.
- 223 cards captured but not screened after the store’s source was selected.
- 3 Jeep-related `IP-QUARANTINE` rows.
- 1 house-brand-dependent exclusion during execution, plus 2 selected-then-brand-excluded records at final audit.
- 1 basic/non-graphic exclusion.
- 2 recognized duplicate-family rows.

Eight execution-time selections occurred at raw rank 1. After audit, three of the four final qualifying families occurred at raw rank 1, and AukCliff’s source occurred at rank 2 after excluding a plain basic. The selected Wicked Clothes, Crazy Dog, Sloth Hiking Club, and Solid Threads expressions were quarantined after exact or materially matching expressions were found across unrelated sellers without a resolved origin; the Solid Threads decision followed discovery of an exact or materially matching F-Bombs bomber expression. Raiz’d Up’s rank-5 source was removed because the dominant house brand made its retention inconsistent with the rank-4 brand exclusion.

All four final qualifying DTC sources had positive item- or product-scoped review evidence. The no-review South Coast and uncorroborated Raiz’d Up records were separately removed for brand dependence.

Shopify’s order is a lifetime within-store ordinal. It is not recent velocity and is not comparable across stores. A collection with no sales can fall back to newest-first, so native sort alone does not prove that every selected product has a nonzero order count.

## IP and contamination result

The exclusion requirement ultimately prevented contaminated sources from supporting final claims, but its execution-time implementation failed and required a strict final audit:

- Etsy excluded 25 IP/public-fame-dependent first-listing records and quarantined 8 during execution; final audit quarantined 11 additional execution selections for unresolved expression-origin or artwork-provenance conflicts.
- Shopify/DTC quarantined three Jeep-dependent ranks during execution.
- Final audit quarantined four selected DTC expressions with unresolved cross-market origin and removed the South Coast and Raiz’d Up selections for house-brand dependence; all six receive no recipe or apparel-grammar support.
- Ads, custom printing services, shop-wide reviews, and mixed-design outcomes were not credited as design-level demand.

No known licensed franchise, celebrity, sports identity, named entertainment property, unresolved repeated expression, or brand-dependent source entered the 5 eligible SDC inputs. Seventeen execution-time selections remain visible as excluded/quarantined audit records rather than being erased.

This is a methodological screen, not a legal finding. Artwork provenance remained uncertain for some generic marketplace imagery and should be tracked separately from identifiable franchise contamination.

## Claim boundaries

This pilot can support the following claims:

- TRACE can produce an auditable Etsy candidate scan under a documented execution interpretation when organic positions, ads, listing IDs, badges, and item-review scope are preserved. Frozen v0.2 was not deterministic enough to claim independent reproduction.
- Gate 0 materially reduces licensed-IP, public-fame, customization, mixed-design, and brand-led contamination.
- Native Shopify `Best selling` can provide a useful within-store lifetime order when collection scope and active sort state are verified.
- Platform access failure is a legitimate methodology result.
- The accessible sample produced 5 eligible Source Decode Cards, zero `CORROBORATED` and zero `PROVISIONALLY-CORROBORATED` recipes, five one-family candidates in total—including the Form Enacts Proposition candidate—and limited apparel-grammar observations.
- Candidate Concrete Semantic Resolution received three active three-niche source-erasure diagnostics against independently researched R010, R021, and R027 truths, yielding three active source-by-seed originality comparisons against its sole eligible support, `TRACE-P001-DTC-07`. Six earlier diagnostics are invalidated audit records because the recipes that generated them lost all eligible source support. The truth-panel sequencing is procedurally supported but not independently timestamp-audited.

It cannot support these claims:

- That a comprehensive 36-family or cross-platform bestseller scan was completed.
- That Amazon prevalence or mechanisms were measured.
- That Etsy badges, review totals, and Shopify ranks are comparable on one scale.
- That any observed semantic or visual mechanism caused sales.
- That the 223 unscreened Shopify/DTC cards were eligible.
- That a no-review Shopify rank necessarily represents nonzero sales.
- That search snippets are Amazon sample observations.
- That external recurrence proves a recipe caused sales.
- That the diagnostic transfer seeds are internally tested, replicated, product recommendations, production-cleared, or legally cleared.

## Friction and deviation register

| ID | Evidence | Type | Impact | Minimum correction |
|---|---|---|---|---|
| `FRI-001` | Amazon returned 503 and unsupported-client responses; 0/200 rows retrieved. | `PLATFORM-BLOCKER` | Amazon quota impossible without inventing a pool. | Add a complete-frame access prerequisite and deterministic stop rule. |
| `FRI-002` | Men’s and Women’s ranks are separate ordinals; v0.2 requested one combined top 12. | `RULE-AMBIGUOUS` | Selection could vary by analyst. | Freeze six families per pool; never compare category ordinals. |
| `FRI-003` | Amazon seller, displayed brand, artist/source, parent ASIN, and child ASIN can differ. | `RULE-AMBIGUOUS` | Seller cap and attribution may be wrong. | Separate commercial source, seller of record, list ID, detail ID, parent, and variant IDs. |
| `FRI-004` | Etsy’s first-occurrence tiebreak depended on an unstated query-major versus sort-major order. | `RULE-AMBIGUOUS` | Cutoff source can change. | Freeze query-major traversal, `Most relevant` before `Top reviews`. |
| `FRI-005` | One Etsy surface initially showed 11 organic cards until further wait/scroll. | `WORKFLOW-COST` | Result depth can vary with lazy loading. | Add a bounded lazy-load recovery procedure and partial-pool rule. |
| `FRI-006` | Etsy automatically appended `instant_download=false`. | `FIELD-UNAVAILABLE` | Session behavior silently changed the candidate pool. | Freeze the filter explicitly and record the final URL. |
| `FRI-007` | A badged source with 9 item reviews outranked non-badged sources with 279–1.7k reviews. | `RULE-AMBIGUOUS` | Absolute badge precedence distorted the evidence mix. | Separate badge-led and item-history-led Etsy subpanels. |
| `FRI-008` | “Recency” did not specify newest review, cadence, or count within a window. | `RULE-AMBIGUOUS` | The final Etsy cutoff was not fully deterministic. | Define recency as newest visible item-specific review date; unknown sorts last. |
| `FRI-009` | Etsy search-card counts were normally shop-level; listing pages supplied item counts. | `EDGE-CASE` | Shop popularity could be assigned to one design. | Require explicit review-scope values and listing-page verification. |
| `FRI-010` | Cause/public-figure and generic-art provenance boundaries recurred. | `EDGE-CASE` | Similar sources may be excluded inconsistently. | Clarify cause eligibility and add artwork-provenance confidence. |
| `FRI-011` | Shopify panel-lock time was not preserved. | `DEVIATION` | Preselection-before-result-inspection cannot be audited independently. | Require a timestamped panel manifest before ranked inspection. |
| `FRI-012` | Frozen v0.2 required 24 distinct families; the run captured 24 raw cards and stopped despite recognized duplicates in two stores. | `DEVIATION` | Crazy Dog and SeaMonkey did not demonstrably reach 24 distinct families. Selection was unaffected because both chosen sources ranked first. | v0.3 should deliberately define 24 raw cards, preserve ranks, and deduplicate separately. |
| `FRI-013` | Optional second-family backfill after store processing was not deterministic; two failed stores were left empty. | `RULE-AMBIGUOUS` | DTC quota could vary. | Use one family per locked store; failed slots remain empty. |
| `FRI-014` | Native `Best selling` can be newest-first when the collection has zero sales. | `EDGE-CASE` | Within-store rank may overstate demand. | Record nonzero-sales corroboration and cap unsupported sources at candidate confidence. |
| `FRI-015` | Visible, structured, family-level, and shop-wide review counts differed. | `RULE-AMBIGUOUS` | Review evidence can be misattributed. | Preserve each scope separately; never merge conflicting counts. |
| `FRI-016` | OpenTrail access changed; Two-Cross’s assortment changed between cached discovery and execution. | `PLATFORM-BLOCKER` | Preselected stores may fail at execution. | Record access mode, source freshness, and fixed failure codes; do not replace after result inspection. |
| `FRI-017` | Family relation and design attribution were used inconsistently in DTC records. | `RULE-AMBIGUOUS` | Variants can look like mixed or non-independent support. | Separate observation attribution, expression family, template cluster, and duplicate relation. |
| `FRI-018` | Several winners were principally visual/aesthetic and had no defensible semantic proposition. | `EDGE-CASE` | v0.2 encourages forced recipes. | Add `RECIPE-CANDIDATE`, `GRAMMAR-ONLY`, and `NO-TRANSFERABLE-MECHANISM`. |
| `FRI-019` | `REPEATED-EXPRESSION` is listed as maturity despite being saturation evidence. | `RULE-AMBIGUOUS` | Copies could appear to advance confidence. | Separate corroboration maturity from derivative saturation. |
| `FRI-020` | Independent R010, R021, and R027 truth banks were prepared without marketplace designs, but v0.2 did not require a timestamped one-truth-per-identity panel or provenance fields. | `RULE-AMBIGUOUS` | Transfer inputs could otherwise be chosen post hoc. | Freeze the exact canonical panel and provenance before recipe clustering. |
| `FRI-021` | No contemporaneous five-card calibration checkpoint or exact Etsy/DTC timestamps were preserved. | `DEVIATION` | The required stop-and-check step and changing surfaces cannot be audited precisely. | Make the checkpoint and UTC start/end times required execution-manifest gates. |
| `FRI-022` | Final Gate 0 audit found 15 unresolved expression-origin or artwork-provenance conflicts and 2 DTC brand-dependency conflicts among execution-time selections. | `GATE-FAILURE` | Seventeen sources reached synthesis before the controlling Gate 0 decision was closed. | Require exact-phrase, distinctive-title, and distinctive subject/composition searches plus a signed eligibility/provenance closeout before SDC creation or clustering; preserve later audit removals without post-hoc backfill. |
| `FRI-023` | The Earned Archetype Recasting recipe added a two-correspondence/native-evidence constraint that its animal source cluster did not demonstrate. | `ABSTRACTION-DRIFT` | Transfer refinement was mistaken for external corroboration. | Audit every required recipe ingredient against each credited source; downgrade unsupported refinements to candidate hypotheses. |

## Field-usefulness audit

| Field or record | Availability | Usefulness | Pilot ambiguity | v0.3 action |
|---|---|---|---|---|
| Platform, pool, query, sort, raw position | High on Etsy/DTC; unavailable on Amazon | Essential | DTC raw rank versus family rank | Retain; add family-first rank and duplicate ranks. |
| Exact observation time | Amazon only | High for changing surfaces | Etsy/DTC preserved date only | Require UTC start/end timestamps. |
| Result type / ad status | Complete on Etsy | Essential | None material | Retain. |
| Listing/product identifier | Strong on Etsy; URLs on DTC | Essential | Parent/variant relationships absent | Add surface, detail, parent, and variant identifiers. |
| Eligibility disposition | High | Essential | Missing brand- and evidence-quarantine states | Add `BRAND-EXCLUDED` and `EVIDENCE-QUARANTINE`. |
| Demand signal | High | Essential | Shopify zero-sale fallback | Retain; add nonzero-sales corroboration. |
| Design attribution | Useful | High | Conflated with family variants in DTC | Keep separate from family relation. |
| Currency | High | High | Etsy badge is recent; reviews can be lifetime | Preserve evidence-specific windows. |
| Persistence | Always single snapshot | Low in this run | No repeat scans | Retain for future repetition. |
| Official badge | High on inspected Etsy listings | High but not sufficient | Absolute precedence distorted sample | Use a separate badge-led lane. |
| Item review count | High on inspected Etsy; mixed on DTC | High | Visible versus structured versus shop-wide | Expand review-scope enum and retain conflicting counts. |
| Latest item review date | Available on selected Etsy sources | Moderate | “Recency” undefined | Define as newest visible item-specific review date. |
| Native-sort verification | High for 10 DTC stores | Essential | Page name alone is inadequate | Require broad scope, URL parameter, and active state. |
| Commercial source/seller | Clear on Etsy/DTC; unresolved on Amazon | Essential | Platform service versus design source | Separate commercial source and seller of record. |
| Artwork provenance confidence | Not registered | High for marketplace art | Eligibility and provenance were conflated; 15 selected expressions were quarantined only after the final provenance audit | Add `HIGH`, `MEDIUM`, `LOW`, `UNRESOLVED`, with `UNRESOLVED` controlling as `IP-QUARANTINE`, a recorded rationale required for eligible `LOW`, and mandatory phrase/title/composition recurrence searches. |
| Access mode/source freshness | Not normalized | High | Live HTML, index, cache, and blocked states differed | Add explicit fields. |
| Confounders | Present in source inputs | High | Not causal evidence | Retain as hypotheses. |
| Decode outcome | Not registered | High | Visual-only designs were forced toward recipes | Add three-outcome classification. |

## Pilot success criteria

| Frozen question | Answer | Evidence |
|---|---|---|
| Could another reviewer reproduce why each source was included or excluded? | `PARTIAL` | Etsy is auditable under the recorded traversal/recency interpretation, but frozen v0.2 leaves those rules ambiguous; DTC panel time, raw/distinct-family handling, and some field semantics are incomplete; Amazon was blocked. |
| Did any IP-dependent or brand-driven source contaminate recipe support? | `FOUND AND REMOVED` | Seventeen execution selections failed final Gate 0 audit. They are preserved as audit records but removed from SDC, recipe, grammar, and maturity support; no known excluded source supports any surviving candidate finding. |
| Were copies prevented from masquerading as independent confirmations? | `ONLY AFTER FINAL AUDIT` | Raw duplicate-family handling worked, but cross-seller phrase and composition recurrence was missed during execution. The final audit quarantined every unresolved recurrence before final claims were committed. |
| Did Source Decode Cards preserve niche truths without binding them to recipes? | `YES, AFTER AUDIT` | Source-specific contexts and transfer prohibitions remain on 5 eligible SDCs; 17 removed selections retain audit records only. |
| Could recipes be instantiated across unrelated truths? | `YES — DIAGNOSTIC ONLY` | Candidate Concrete Semantic Resolution was instantiated against the R010, R021, and R027 panel without source nouns, wording, or compositions. Panel timing was not independently audited. |
| Could the method reject derivative or unwearable concepts? | `PARTIAL — DIAGNOSTIC ONLY` | Candidate Concrete Semantic Resolution includes rejection probes, source prohibitions, T-shirt-fit checks, and an originality matrix. Six tests attached to withdrawn recipes are audit-only, and no behavioral or production test was run. |
| Which fields were useful, unused, ambiguous, or unavailable? | `YES` | See the field-usefulness audit. |
| What should change in v0.3? | `YES` | See the change map below. |

## Minimal TRACE v0.3 change map

| Change | Friction | Minimum normative correction | Existing evidence reclassified? |
|---|---|---|---|
| `V03-01 — Access and claim gate` | `FRI-001` | A ranked stratum starts only when its complete precommitted frame is retrievable and timestampable. After one failed direct retrieval and one failed ordinary browser retrieval, permit at most one ordinary reload before declaring deterministic failure. Snippets and fragments cannot reconstruct a pool. Blocked quotas remain empty. | No Amazon rows exist. |
| `V03-02 — Amazon sampling` | `FRI-002`, `FRI-003` | Select six unique families from Men’s and six from Women’s; never compare category ordinals or move quota. Preserve every traversed rank. Separate commercial source, seller of record, list/detail/parent/variant IDs, and quarantine identifier mismatches. | Retest required when access exists. |
| `V03-03 — Frozen execution manifest` | `FRI-004`–`FRI-006`, `FRI-011`, `FRI-016`, `FRI-021` | Freeze Etsy query-major order, final URL/filter, bounded lazy-load handling, UTC times, Shopify panel-lock time, access mode, source freshness, and five-card calibration outcome before synthesis. | Add missing metadata; do not invent timestamps. |
| `V03-04 — Etsy evidence lanes` | `FRI-007`–`FRI-010` | Use two independent six-family lanes: six badge-led sources and six item-history-led sources. Within each lane rank by item-specific review count, then newest visible item-specific review date, then attribution, then first occurrence. The history lane requires a visible item review within 180 days. Inspect every first-occurrence fixed-design candidate surviving title/thumbnail Gate 0 screening. | Do not retrofit v0.2 selection; retest under v0.3. |
| `V03-05 — Shopify/DTC execution` | `FRI-012`–`FRI-016` | Lock 12 stores before ranked inspection; permit assortment-level prequalification only. Verify broad scope, `sort_by=best-selling`, and active sort state. Capture 24 raw cards, preserve raw ranks, deduplicate separately, and take at most one family per locked store. Failed slots remain empty. Record nonzero-sales corroboration, review scope, access mode, and failure code. | Existing 10 selections remain v0.2 evidence; unsupported sales corroboration must be visible. |
| `V03-06 — Identity, provenance, and record model` | `FRI-017`, `FRI-022` | Use `POOL → observation → expression family → SDC → optional template cluster → mechanism cluster → recipe → transfer`. Selection fields appear only on canonical observations. Give observations, expression families, and SDCs stable IDs. Add explicit `BRAND-EXCLUDED`, `EVIDENCE-QUARANTINE`, provenance confidence, family-first rank, duplicate ranks, and a controlling final-audit disposition. Before eligibility, record exact-phrase, distinctive-title, and distinctive subject/composition searches across the open web or another marketplace; unresolved cross-seller recurrence is `IP-QUARANTINE`, not proof of infringement. | The committed registers preserve execution selection and final audit separately; no post-synthesis backfill was used. |
| `V03-07 — Decode and maturity outcomes` | `FRI-018`, `FRI-019`, `FRI-023` | Assign exactly one primary outcome: `RECIPE-CANDIDATE`, `GRAMMAR-ONLY`, or `NO-TRANSFERABLE-MECHANISM`. Remove `REPEATED-EXPRESSION` from maturity and record derivative saturation separately. Only independent eligible SDCs advance corroboration. Every credited source must demonstrate every required recipe ingredient; transfer-stage refinements cannot retroactively raise external maturity. | No recipe remains corroborated or provisionally corroborated; Concrete Semantic Resolution is a candidate on one eligible family, and unsupported recipes are retained only as retracted audit records. |
| `V03-08 — Transfer and handoff` | `FRI-020`, `FRI-021` | Freeze the exact R010, R021, and R027 truth panel before clustering, including canonical path, heading, blob/commit, and independence. Pilot concept seeds are noncommercial diagnostics and must pass the normal Brand Handoff Integrity Check before advancement. | Existing diagnostics are preserved and explicitly noncommercial. |

## Retest requirements

A v0.3 retest should:

1. Obtain a complete, timestamped Amazon frame before scanning that stratum.
2. Re-run Etsy under the two-lane evidence rule.
3. Lock and timestamp a fresh 12-store DTC panel.
4. Capture 24 raw DTC cards per store and normalize family relationships afterward.
5. Complete and record the five-card calibration checkpoint.
6. Assign each SDC a primary outcome before clustering.
7. Run and record exact-phrase, distinctive-title, and distinctive subject/composition recurrence searches, then close and sign the eligibility/provenance audit before creating SDCs or clustering; do not backfill after synthesis.
8. Verify that every credited source demonstrates every required ingredient of its proposed recipe.
9. Promote no more than three recipes; zero is valid.
10. Test each promoted recipe against the frozen R010, R021, and R027 panel.
11. Preserve v0.2 execution evidence unchanged and record any final-audit or v0.3 reclassification in a migration ledger.

## Final recommendation

`REVISE-AND-RETEST`

TRACE should be retained. The pilot validated its central separation of platform evidence, IP screening, source-specific truths, candidate mechanisms, and transfer prohibitions. The required revisions are operational and schema-level rather than a rejection of the core model.

## Normalization and known deviations at commit

1. The committed Etsy CSV clears `selection_rank` from duplicate observations, so exactly 12 canonical rows carry selection ranks.
2. Etsy reconciles to 121 unique listing IDs and 120 deduplicated expression families because one separate Pasta Pups listing belongs to an earlier family.
3. The DTC embedded CSV's attribution field remains mixed: most rows use `EXACT`, while recognized same-print variant relationships use `SAME-PRINT-VARIANTS`. The decode records family collapse separately where verified or pending. v0.3 formalizes the separation.
4. DTC captured 24 raw cards rather than 24 demonstrably distinct families. At least Crazy Dog and SeaMonkey contain duplicates and were not extended to rank 25; this did not change either rank-1 selection.
5. The DTC panel lock time, the five-card calibration checkpoint, and exact Etsy/DTC UTC times were not preserved. No timestamps were invented after the fact.
6. INTO THE AM's raw card text is `+ Quick Add`; its normalized detail-page title is `Lunar Canyon Tee`. Both are preserved.
7. Etsy uses a standalone register while DTC embeds its raw pool in a platform report. The schema divergence remains visible rather than rewriting the v0.2 evidence into a falsely uniform record.
8. The recipe artifact completes the cluster ledger, eligibility-driven withdrawal, apparel-grammar separation, and transfer/originality diagnostics. None of those diagnostics is labeled as behavioral validation or production clearance.
9. Twelve Etsy and ten DTC families were selected at execution. Final Gate 0 audit left only `TRACE-P001-ETSY-12`, `TRACE-P001-DTC-01`, `TRACE-P001-DTC-03`, `TRACE-P001-DTC-06`, and `TRACE-P001-DTC-07` eligible. Eleven Etsy and four DTC selections became `IP-QUARANTINE`; two DTC selections became frozen-v0.2 brand-dependent `IP-EXCLUDED` records (v0.3 `BRAND-EXCLUDED`). Removed records receive no downstream support and were not backfilled.
10. No recipe meets the frozen `CORROBORATED` or `PROVISIONALLY-CORROBORATED` threshold. Concrete Semantic Resolution remains a `CANDIDATE` on one eligible DTC family, `TRACE-P001-DTC-07`. Owned-Friction Reversal and Earned Archetype Recasting are withdrawn as active recipes because every supporting source failed Gate 0.
