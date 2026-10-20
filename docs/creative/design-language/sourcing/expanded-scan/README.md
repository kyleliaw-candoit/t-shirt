# Expanded design-language scan — plan and recovery checkpoint

Updated: 2026-10-20 (America/Chicago)
Status: Collection in progress under approved reallocation. 220/220 references documented; backs unverified. No family synthesis.

## Approved scope

This supersedes the equal 20-per-source allocation in [the earlier decision](../2026-10-20-Expanded-Scan-Decision.md). The Founder accepted deeper marketplace sampling to improve visual-language discovery, then requested interruption-safe planning.

| Source | Target | Verified expanded records | Status / next action |
|---|---:|---:|---|
| Etsy | 44 | 44 | Batch009; next card141; individual badges verified |
| Redbubble | 44 | 44 | Approved extension complete; backs unverified |
| Zazzle | 44 | 44 | Approved extension complete; backs unverified |
| Life is Good | 20 | 20 | Allocation collected; Best sellers sort; backs unverified |
| SnorgTees | 20 | 20 | Allocation collected; position 18 held outside count; backs unverified |
| HistoreeTees | 20 | 20 | Allocation collected; live pages 1–2 verified; backs unverified |
| The Bee & The Fox | 8 | 8 | Collection exhausted: 8 unique eligible references; shortfall 12 |
| Sloth Hiking Club | 20 | 20 | Allocation collected; default Featured order in Bestsellers collection; backs unverified |
| **Total source-level slots** | **220** | **220** | **Approved reallocation in progress** |

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

- [RB-men batch 002](batches/RB-men-002.md): cumulative 98/220. Accepted positions 8–12 as DLS-RB-006–010. Position 8 is a predefined named support-campaign design, not a blank personalization template; campaign solidarity may dominate purchase intent. No exclusions in this batch. Image-export recovery successful; count only verified files.

- [RB-men batch 003](batches/RB-men-003.md): cumulative 103/220. Accepted positions 13–17 as DLS-RB-011–015. No exclusions in this batch; decorative Japanese characters not independently translated. Designs retained as visual references, not permission to reuse artwork.

- [RB-men batch 004](batches/RB-men-004.md): cumulative 108/220. Accepted positions 18,19,20,23,24 as DLS-RB-016–020. Position 21 held: Star Wars franchise vehicles/setting boundary; position 22 excluded: Kenny G celebrity depiction. Men's route reached 20 distinct accepted artworks at position 24.

- [RB-women batch 001](batches/RB-women-001.md): cumulative 113/220. Women's route positions 2,3,4,6–18,20,21 repeat artwork already collected in men's route; stable IDs retained via matching artwork IDs in route roster, no extra count for cuts. Positions 1 and 19 inherit franchise-object holds; 5 Muppet excluded. Position 22 Cathulhu held for fictional-character/parody eligibility boundary. Accepted 23–27 as DLS-RB-021–025, first five additional distinct artworks from women’s route. Gender category is not evidence of buyer gender or a distinct visual market.

- [RB-women batch 002](batches/RB-women-002.md): cumulative 118/220. Accepted 28,29,30,31,33 as DLS-RB-026–030. Position 32 held: film-character-associated name/moth design; ambiguous boundary rather than a silent broadened exclusion. Position 33 is retained despite an explicit rectangular collage composition; collection does not filter by current taste.

- [RB-women batch 003](batches/RB-women-003.md): cumulative 123/220. Accepted 35,36,37,38,40 as DLS-RB-031–035. Position 34 excluded: identifiable Monty Python film-character scene; 39 excluded: Roger Rabbit characters/actor imagery. Position 38 has franchise-logo-style lettering but no depicted character; cultural/logo recognition recorded as confound rather than silently extending character exclusion.

- [RB-women batch 004](batches/RB-women-004.md): cumulative 128/220. Accepted 41,43,45,47,48 as DLS-RB-036–040. Position 42 duplicates DLS-RB-014; 44 excluded Muppet characters; 46 excluded recognizable viral public-figure depiction. Women's route reaches 20 additional artworks at position 48. Creator concentration and recurring artwork remain observable in saved rosters.

- [ZZ-men batch 001](batches/ZZ-men-001.md): cumulative 133/220. Accepted positions 1–5. Popular is a marketplace ranking proxy; no sales counts verified. All are complete predefined front designs.

- [ZZ-men batch 002](batches/ZZ-men-002.md): cumulative 138/220. Accepted 8,10,12,16,21. Excluded 6 custom text,7 name/photo,9 custom pet photo,11 team name,13 year placeholder,14 visible back print,15 visible your-text-here placeholder,17 custom photos,18 custom family text,19 visible custom-text placeholders,20 custom name/year. Positions 15 and 19 inspected visually rather than excluding from title alone.

- [ZZ-men batch 003](batches/ZZ-men-003.md): cumulative 143/220. Accepted 23,25,26,27,29. Excluded 22 visible back print,24 licensed Grinch design,28 artwork recolor of25 (same antler/phrase composition). Back status of accepted references remains unverified.

- [ZZ-men batch 004](batches/ZZ-men-004.md): cumulative 148/220. Accepted30,31,32,34,39. Excluded33 visible custom-text placeholder,35 custom-message placeholder,36 and37 visible back graphics,38 custom family reunion. Generic catchphrase/allusion designs retained; no licensed character depicted. Men's quota complete at39.

- [ZZ-women batch 001](batches/ZZ-women-001.md): cumulative 153/220. Women's Popular route: excluded1 licensed Grinch. Accepted2–6. Same phrase-family or typography resemblance alone is not exact-artwork duplication; copy variants remain flagged for later reconciliation, not clustered now.

- [ZZ-women batch 002](batches/ZZ-women-002.md): cumulative 158/220. Accepted7,8,9,11,13. Excluded10 licensed Peanuts;12 visible farm-name personalization. Bad Witch9 shares typography/flourish template with Good Witch2 but changes wording; retained as explicit copy variant, not evidence of independent family breadth.

- [ZZ-women batch 003](batches/ZZ-women-003.md): cumulative 163/220. Accepted14,16–19. Excluded15 licensed Sesame Street character. Complete predefined text designs retained; no demographic inference from women's merchandising route.

- [ZZ-women batch 004](batches/ZZ-women-004.md): cumulative 168/220. Accepted21–25. Excluded20 custom photo collage. Women's quota complete at25; later positions unneeded. Zazzle40 complete; global exact-artwork reconciliation pending.

- [Etsy batch 001](batches/ETSY-001.md): cumulative 173/220. Skipped sponsored positions1–4. Accepted5,6,7,9,10 with live Bestseller badges. Position8 lacks badge and is outside count. Position9 primary gallery shows sweatshirt; selected explicit Adult T-Shirt thumbnail2 and retained that tee image. Collection title alone is not ranking evidence.

- [Etsy batch 002](batches/ETSY-002.md): cumulative 178/220. Accepted12–16 with individual Bestseller badges. Excluded11 personalized teacher name. Generic frog/raccoon images retained; recurring folded-mockup styling noted separately from printed design.

- [Etsy batch 003](batches/ETSY-003.md): cumulative 183/220. Accepted18,19,20,31,32. No badge observed17,21,22,24,29,30; excluded23 Winnie-the-Pooh character. Sponsored25–28 skipped even where badge exists;31 is organic appearance of27, counted once. No global family comparison performed.

- [Etsy batch 004](batches/ETSY-004.md): cumulative 188/220. Accepted34,35,41,46,47. No badge33,42,44,45;36 excluded Wishbone television character. Sponsored37–40 skipped.43 held outside count: named Middle-earth inspiration plus distinctive fantasy doorway/figures; franchise-boundary review needed.47 repeats sponsored28, accepted once at organic appearance.

- [Etsy batch 005](batches/ETSY-005.md): cumulative 193/220. Accepted53,57,59,60 and page2/card7(cumulative67). No badge48,54–56,58,65,66. Sponsored49–52 and61–64 skipped. Page1 exhausted; page2 roster retained. Generic quote allusion60 retained without licensed character imagery.

- [Etsy batch 006](batches/ETSY-006.md): cumulative 198/220. Accepted69,71,72,78,81.69 adult-tee gallery image2 selected instead of sweatshirt primary. No badge68,77,79,80;70 excluded licensed Super Grover; sponsored73–76 skipped.78 seller-labeled embroidery retained as design-language reference, with process-transfer limitation rather than treating embroidery as DTG-ready.

- [Etsy batch 007](batches/ETSY-007.md): cumulative 203/220. Accepted89,90,92,102,103. No badge82–84,91,93,95,96,101. Sponsored85–88,97–100 skipped.94 held outside count: seller explicitly frames current named-public-figure death-related political message; boundary with celebrity/public-figure exclusion requires review, not silently treated as generic crow art.

- [Etsy batch 008](batches/ETSY-008.md): cumulative 208/220. Accepted107,108,114,117 and page3/card7(cumulative127). No badge104,106,115,116,118–120,125,126;105 excluded named Elephant and Piggie characters. Sponsored109–112,121–124 skipped.113 held outside count: named fictional Hobbit identity, franchise boundary.126 also displays National Geographic logo.128 inspected lookahead lacks badge, not needed. Etsy40 quota complete; retained 3-page roster, source is relevance discovery plus individual badges, not top40 sales rank.

## Current handoff

See [collection checkpoint and decision](Collection-Checkpoint-208.md). Historical checkpoint: Founder subsequently approved the12-slot reallocation; collection resumed. Do not start comparisons or recipe-family development until the Founder has been reminded to switch Astra Medium to Astra Extra High.

- [Etsy batch 009](batches/ETSY-009.md): cumulative 212/220. Founder approved reallocation2026-10-20: Etsy44, Redbubble44, Zazzle44, Bee8; total220 unchanged. Accepted131,132,137,140 with listing-level Bestseller badges.129,130,138 no badge; sponsored133–136 skipped;139 excluded visible Snoopy character. Etsy expanded allocation complete at page3/card20(cumulative140).

Founder approved 2026-10-20: replace unavailable12 Bee slots with4 additional each Etsy/Redbubble/Zazzle. New targets44/44/44/8; other source targets unchanged, total220.

- [Redbubble extension](batches/RB-extension.md): 216/220.

- [Zazzle extension](batches/ZZ-extension.md): 220/220.
