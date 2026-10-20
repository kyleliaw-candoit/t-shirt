# Expanded design-language scan — plan and recovery checkpoint

Updated: 2026-10-20 (America/Chicago)
Status: Collection in progress. 93 front-design references documented; backs unverified. No family synthesis started.

## Approved scope

This supersedes the equal 20-per-source allocation in [the earlier decision](../2026-10-20-Expanded-Scan-Decision.md). The Founder accepted deeper marketplace sampling to improve visual-language discovery, then requested interruption-safe planning.

| Source | Target | Verified expanded records | Status / next action |
|---|---:|---:|---|
| Etsy | 40 | 0 | Establish reproducible discovery route and listing-level badge evidence |
| Redbubble | 40 | 5 | RB-men batch 001; next position 8 |
| Zazzle | 40 | 0 | Men's/Women's T-shirts → Popular; 20 eligible unique designs per route |
| Life is Good | 20 | 20 | Allocation collected; Best sellers sort; backs unverified |
| SnorgTees | 20 | 20 | Allocation collected; position 18 held outside count; backs unverified |
| HistoreeTees | 20 | 20 | Allocation collected; live pages 1–2 verified; backs unverified |
| The Bee & The Fox | 20 | 8 | Collection exhausted: 8 unique eligible references; shortfall 12 |
| Sloth Hiking Club | 20 | 20 | Allocation collected; default Featured order in Bestsellers collection; backs unverified |
| **Total source-level slots** | **220** | **93** | **Collection in progress; source shortfall recorded** |

The men/women split is an operational extension of the earlier balanced-route plan, not a claim about buyer demographics. Globally unique artwork totals must be reported separately after cross-source deduplication.

SimplyCuteTees' four examples remain supplementary. Boredwalk is deferred. Preserve all [28 initial discovery designs](../discovery-28/README.md); do not repeat their completed analysis. Reuse records when encountered in the ordered scan, preserving original evidence dates and recording current route membership separately. Initial curated designs outside the ordered scan remain supplementary.

## Execution plan

1. Reconcile existing records and establish each source's exact route, ordering, evidence type and collection cursor before collection. Consult [source strategy](../2026-10-19-Source-Strategy.md) and [screening/continuation](../discovery-28/Screening-and-Continuation.md).
2. Collect in batches of up to five accepted designs. Log inspected exclusions and pending candidates as well, so low-yield sources do not require repeated screening. Commit partial progress at a source change, access blocker or planned stop even if five are not accepted.
3. Save source images, evidence and concise visual/garment observations with stable record IDs. Use the actual images for analysis; descriptions are supporting records, not substitutes.
4. Compare within and across sources at the allocation checkpoint. Keep tentative overlapping groups, boundary examples and outliers; distinguish subject similarity from visual relationships.
5. Expand selectively in batches of ten if new relationships continue appearing or family boundaries remain uncertain. Record the reason; do not silently change quotas or replace an inaccessible source.
6. Develop annotated recipe cards and neutral reconstructions, then application tests using the same audience/material/concept. Separate observation, transfer hypothesis and Founder/customer evaluation.

## Eligibility and evidence

- Front-only graphics; exclude known back graphics and back logos. Missing back views mean uncertainty, not proof of a blank back; retain placement evidence and unresolved cases explicitly.
- Exclude customization-dependent templates, licensed characters and celebrities. An optional editing button does not disqualify a complete predefined design. Illustration-only designs are eligible.
- Follow displayed order rather than choosing only attractive examples. Preserve category, query, filters, sort, position, date and page/cursor.
- Etsy listing Bestseller badges, seller-designated brand collections, Redbubble Best Selling ordering and Zazzle Popular are distinct commercial proxies, not interchangeable audited sales rankings.
- Recolors/cuts do not create new distinct artwork counts. Retain relevant garment differences and duplicate links.
- Track creator concentration and recurrence within each source and across independent creators; unknown authorship stays unknown. Do not use pooled frequencies as an estimate of market prevalence or visual quality.
- Audience-fit judgments are contextual hypotheses. Commercially signaled examples alone cannot establish that visual treatment caused sales.

## Batch record and completion rule

For each batch, retain under this directory:

- `records/<stable-id>.md`: source, creator/brand, product URL, route and ordering, observed commercial evidence/date, eligibility and placement checks, image paths/hashes, garment facts versus unknowns, visual relationships, duplicate/carry-forward links, and status.
- `images/`: retained evidence images; reference existing repository images rather than duplicating identical files.
- `batches/<source>-<batch>.md`: inspected candidates and dispositions, accepted IDs, unresolved IDs, last fully inspected item/page/position, next candidate/page, access limitations and changes in ordering.

A batch is complete only when images and records exist remotely, hashes/references and counts have been checked, and the source cursor is saved. Update this checkpoint's progress table and append the batch path to the recovery log in the same commit as the batch where possible. Do not mark uploads, tool attempts or unverified local files as completed work.

Record the resulting commit SHA in the PR progress summary after verification. If interrupted before updating that summary, the remote commit plus verified batch manifest is authoritative. Do not trust a session checklist over repository evidence.

## Resume procedure — read first after interruption

1. Inspect the current remote branch `docs/design-language-expanded-collection`, its PR and latest commits. Check whether it has since merged; never overwrite newer work.
2. Read this checkpoint, the latest batch manifests and any pending records. Reconcile the table against remotely verified records/images, not conversational claims.
3. Verify the last batch's files and cursor. Repair only missing/partial records; preserve stable IDs and evidence dates. Never restart completed source scans automatically.
4. Resume at the first unresolved candidate, using both its URL and recorded position. Rankings may move: record a new snapshot and reconcile IDs rather than treating an old page number as immutable.
5. If source access fails, log the exact blocker and continue an independent accessible source; do not silently lower eligibility or fabricate completion.
6. Commit and verify each batch, then update progress. Keep the PR unmerged until Founder approval.

## Recovery log

- Baseline: PR #133 merged at `07cf652cc047de2c63bbddc0209d8ab69b44435d`; pilot and 28-design research are preserved on main.
- Initial checkpoint: this plan and zero-progress table only. No new product scans, image captures, or recipe families are claimed complete.
- Next concrete action: reconcile the existing 28 records with source registers, then establish the first source's current ordered discovery route. The current turn establishes the recovery plan; it does not claim background execution after the response ends.

## Founder execution instructions — 2026-10-20

- Continue collection on Astra Medium. **Pause before any comparison across collected designs or recipe-family development and remind the Founder to switch to Astra Extra High.** Do not start synthesis until that handoff occurs.
- Explicitly announce when execution stops, whether work is still active, the durable checkpoint and what remains. Never imply background work continues after a final response. Report blockers requiring Founder attention promptly; continue other authorized work when possible.

## Expanded execution checkpoint

- PR #135 merged at `951d8864a06b9e4ad992f9cbf4ae3b273b035afc`.
- [Snorg batch 001](batches/SNORG-001.md): five records, including two carried forward and three new. All five are front-design references with unverified backs; zero independently confirmed blank-back products. The table counts documented research records, not verified front-only merchandise.
- Source-level records: 5/220. Within-batch distinct artworks: 5. Cross-source unique total not established.
- Resume at Snorg position 7. No attention is required from the Founder at this checkpoint.

- [Snorg batch 002](batches/SNORG-002.md): cumulative 10/220 source records. Latest cursor supersedes earlier entries: resume position 13. All backs remain unverified.

- [Snorg batch 003](batches/SNORG-003.md): cumulative 15/220 source records. Latest cursor supersedes earlier entries: resume position 18. All backs remain unverified.

- [Snorg batch 004](batches/SNORG-004.md): cumulative 20/220 source records. Latest cursor supersedes earlier entries: resume position 24. All backs remain unverified.

- Snorg allocation reached: 20 front-design records (17 new, 3 carried forward), plus one held franchise-object boundary at position 18. Existing Oxford Comma at position 33 remains supplementary outside this ordered allocation. Next source: HistoreeTees, establish current ordered recent-best-sellers route and reconcile prior IDs. No need to expand Snorg past its allocation unless a collected reference is subsequently ineligible.

- [HistoreeTees batch 001](batches/HISTOREE-001.md): cumulative 25/220 source records; resume this source at position 6. Backs remain unverified.

- [HistoreeTees batch 002](batches/HISTOREE-002.md): cumulative 30/220 source records; resume this source at position 11. Backs remain unverified.

- [HistoreeTees batch 003](batches/HISTOREE-003.md): cumulative 35/220 source records; resume this source at position 16. Backs remain unverified.

- [HistoreeTees batch 004](batches/HISTOREE-004.md): cumulative 40/220 source records; resume this source at position 21. Backs remain unverified.

- HistoreeTees allocation reached: 20 references, 17 new and three carried forward. Current first 20 follow direct live HTML order; cached page discrepancy resolved and saved. History Is Importanter at position 23 remains supplementary. Next source: Sloth Hiking Club, reconcile the saved four IDs against current frontpage order.

- [Sloth Hiking Club batch 001](batches/SLOTH-001.md): cumulative 45/220 source records; resume this source at position 6. Backs remain unverified.

- [Sloth Hiking Club batch 002](batches/SLOTH-002.md): cumulative 50/220 source records; resume this source at position 11. Backs remain unverified.

- [Sloth Hiking Club batch 003](batches/SLOTH-003.md): cumulative 55/220 source records; resume this source at position 16. Backs remain unverified.

- [Sloth Hiking Club batch 004](batches/SLOTH-004.md): cumulative 60/220 source records; resume this source at position 21. Backs remain unverified.

- Sloth allocation reached: 20 front references, 17 new and three carried forward. Birds & Flowers at position 23 remains supplementary. Collection membership is the signal; its displayed default Featured order is not an asserted sales rank. Next source: The Bee & The Fox.

- [Bee batch 001](batches/BEE-001.md): cumulative 65/220 source records. Position 2 excluded: sweatshirt. Position 5 excluded: primary photo directly shows back copy. Positions 1,3,4,6,7 collected.

- [Bee batch 002](batches/BEE-002.md): cumulative 68/220 source records. Positions 8,10,11 collected. Position 9 is the same Feel Your Feelings artwork in green (not counted again). Position 12 socks and position 13 sweatshirt excluded. Collection exhausted at 13; eight unique adult front-design references total, shortfall 12 against target 20.

- Bee source exhausted at 8/20. Next source: Life is Good. Keep total target 220 until Founder decides how to address the 12-slot shortfall; do not silently reallocate.

- [Life is Good batch 001](batches/LIG-001.md): cumulative 73/220 source records. Accepted positions 1,5,8,10,11 (DLS-LIG-005–009). Positions 2,3,4,6 are solid shirts without a central design, excluded from graphic design scan. Position 7 excluded: design continues onto sleeve. Position 9 repeats Pumpkin Cats artwork from 8 on another cut/color. Next candidate 12, Solid Vee.

- [Life is Good batch 002](batches/LIG-002.md): cumulative 78/220 source records. Accepted positions 13,15,16,19,21 (DLS-LIG-010–014). Position 12 solid tee excluded; positions 14,17,18 have sleeve graphics, excluded; 20 sleep pants excluded. Position 16 is different artwork from position 11 despite sharing wording. Next position 22.

- [Life is Good batch 003](batches/LIG-003.md): cumulative 83/220 source records. Accepted positions 23–27 (DLS-LIG-015–019). Position 22 repeats cauldron artwork from 16. Position 23 depicts the seller’s own Jake-style brand mascot, not an identified third-party licensed character; brand familiarity remains an explicit appeal confound.

- [Life is Good batch 004](batches/LIG-004.md): cumulative 88/220 source records. Accepted 29,30,32,35,36 (DLS-LIG-020,021,022,001 carry-forward,023). Position 28 excluded: all-over pattern including sleeves. 31 repeats Daisy artwork; 33 and 34 pants excluded. First 20 eligible reached at displayed position 36.

- [RB-men batch 001](batches/RB-men-001.md): cumulative 93/220. Accepted positions 2,3,4,6,7 as DLS-RB-001–005. Position 1 held outside count: Dune franchise creature/setting imagery, boundary with licensed-character exclusion. Position 5 excluded: identifiable Muppet characters. Browser media saves succeeded for first twelve images; later downloads require recovery before counting.
