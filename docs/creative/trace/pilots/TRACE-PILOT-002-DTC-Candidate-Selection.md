---
title: TRACE-PILOT-002 — DTC Raw Scan and Pre-Origin Candidate Queue
owner: Creative Director
status: Raw DTC frame complete — provenance closure pending
pilot_id: TRACE-PILOT-002
pool_id: TRACE-P002-POOL-DTC
methodology_version: TRACE v0.3
methodology_frozen_commit: 0b74489e083d58d8037129247399d3cece866de6
preregistration_commit: f5f3291fc3de64673f8e66ed85e139f2ec9df535
panel_lock_commit: 143bf6a67fafa684e82860a6b2ab2368c456ea06
observation_date: 2026-09-25
raw_capture_start_utc: 2026-09-25T18:13:28.478Z
raw_capture_end_utc: 2026-09-25T18:28:03.414Z
---

# TRACE-PILOT-002 — DTC Raw Scan and Pre-Origin Candidate Queue

## Controlling status

The frozen DTC raw frame is complete. This artifact stops before every mandatory cross-market origin search and before final Gate 0.

- All 12 locked stores were processed once, in frozen `P002-DTC-S01` through `P002-DTC-S12` order; there are no failed or replacement slots.
- Every returned collection used the explicit `sort_by=best-selling` request and exposed a returned **Best selling** active/selected/current state.
- The register contains 12 `SURFACE` rows and 288 immutable `PRODUCT` observations: exactly 24 raw ranks per store. S06 and S11 exposed complete 24-product collections; the other stores contributed their first 24 ranks.
- The title/rendered-thumbnail pass records 36 exclusions and 4 duplicate-family occurrences. Twelve highest-ranked surviving families received candidate detail checks; 236 later canonical families remain ordered same-store continuation rows.
- Ten queue heads have independent nonzero-sales corroboration beyond rank (one is explicitly supported by an inference recorded in its evidence basis); S10 and S11 remain `UNVERIFIED` beyond native within-store rank.
- No origin query was run. No family is finally `ELIGIBLE`, no expression-family ID is assigned, and no Source Decode Card was created.

The machine-readable controlling register is [TRACE-PILOT-002-DTC-Scan-Register.csv](./TRACE-PILOT-002-DTC-Scan-Register.csv).

## Session and execution controls

- Access mode: live public browser-rendered storefront collection and product pages.
- Frozen traversal: store order first; raw product rank 1 through 24 within each store.
- Rank signal: merchant-native within-collection `best-selling`; treated as lifetime-weighted, single-snapshot, within-store order and never as cross-store-comparable magnitude.
- Observation ID: `TRACE-P002-OBS-DTC-S##-##`; IDs bind the frozen store slot and raw returned rank.
- Basic/title/thumbnail screen: every captured card was reviewed on its returned collection surface. The `thumbnail_alt` field preserves extracted alternative text where available; lack of extracted alt text does not mean the rendered thumbnail was uninspected.
- Product detail scope: the highest-ranked otherwise-eligible family in each store plus an excluded rank-1 family where detail was needed to resolve S06, S08, S09, or S11.
- Contamination labels are operational screening decisions, not infringement findings or legal conclusions.

## Surface closure

| Order | Store | Scope returned | Active-sort proof | Raw rows | Closed at UTC |
|---:|---|---|---|---:|---|
| 1 / `P002-DTC-S01` | Boredwalk | Mens TShirts | URL sort_by=best-selling; returned current link had aria-current=true and label Best selling | 24 | `2026-09-25T18:13:28.478Z` |
| 2 / `P002-DTC-S02` | Wicked Clothes | shirts | URL sort_by=best-selling; returned select value was best-selling and Best selling option was selected | 24 | `2026-09-25T18:14:38.575Z` |
| 3 / `P002-DTC-S03` | INTO THE AM | GRAPHIC TEES | URL sort_by=best-selling; returned collection controls displayed Best selling as the current control label | 24 | `2026-09-25T18:17:53.345Z` |
| 4 / `P002-DTC-S04` | Solid Threads | Men’s T-Shirts \| Funny Vintage Graphic Tees | URL sort_by=best-selling; returned select value was best-selling and Best selling option was selected | 24 | `2026-09-25T18:19:12.057Z` |
| 5 / `P002-DTC-S05` | Crazy Dog T-Shirts | CRAZY SHIRTS | URL sort_by=best-selling; returned select value was best-selling and Best selling option was selected | 24 | `2026-09-25T18:20:07.804Z` |
| 6 / `P002-DTC-S06` | AukCliff | T-shirts | URL sort_by=best-selling; returned select value was best-selling and Best selling option was selected | 24 | `2026-09-25T18:20:56.547Z` |
| 7 / `P002-DTC-S07` | SeaMonkey Apparel | TEE'S | URL sort_by=best-selling; returned active link class identified Best selling and matched the requested URL | 24 | `2026-09-25T18:21:55.837Z` |
| 8 / `P002-DTC-S08` | RAYGUN | T-SHIRTS | URL sort_by=best-selling; returned select value was best-selling and Best Selling option was selected | 24 | `2026-09-25T18:22:52.627Z` |
| 9 / `P002-DTC-S09` | Pyknic | Men's Tees | URL sort_by=best-selling; returned best-selling radio was checked and labeled Best selling | 24 | `2026-09-25T18:24:50.151Z` |
| 10 / `P002-DTC-S10` | Blackbird Supply Co. | COLLECTION: ALL | URL sort_by=best-selling; returned select value was best-selling and Best selling option was selected | 24 | `2026-09-25T18:25:52.916Z` |
| 11 / `P002-DTC-S11` | South Coast Outdoors Company | All T-Shirts | URL sort_by=best-selling; returned select value was best-selling and Best selling option was selected | 24 | `2026-09-25T18:26:56.206Z` |
| 12 / `P002-DTC-S12` | Sloth Hiking Club | SHOP ALL TEES | URL sort_by=best-selling; returned best-selling radio was checked and labeled Best selling | 24 | `2026-09-25T18:28:03.414Z` |

## Deterministic store-order candidate queue

This is a continuation queue, not a cleared source set. The table selects exactly one current head family per store. Every non-excluded, non-duplicate raw family in the CSV has a `store_queue_rank`; if a head fails the mandatory origin screen, continue to the next numerical `store_queue_rank` in that same store without reopening or reranking the raw collection. Open that fallback's detail page, capture its item-level evidence, then perform the full origin screen. Do not borrow a family from another store and do not create an SDC until final Gate 0 is `ELIGIBLE`.

| Store order | Queue head | Raw rank | Candidate | Review scope / item count | Nonzero-sales corroboration | Provenance candidate | Origin state |
|---:|---|---:|---|---|---|---|---|
| 1 / `P002-DTC-S01` | `TRACE-P002-OBS-DTC-S01-01` | 1 | [Men's Ban The Fascists Save The Books T-Shirt](https://www.boredwalk.com/collections/mens-tshirts/products/mens-ban-the-fascists-save-the-books-t-shirt) | ITEM-VISIBLE / 400 | `YES` — 400 visible item reviews; displayed reviews repeat the exact product title | `MEDIUM-CANDIDATE` — Store states its products are designed and hand-printed to order in its southern California studio; origin not independently tested. | `NOT-RUN` |
| 2 / `P002-DTC-S02` | `TRACE-P002-OBS-DTC-S02-01` | 1 | ['Feel Alive' Shirt](https://www.wickedclothes.com/products/feel-alive-shirt) | SHOP-WIDE | `YES` — Product page labels the CATSNEEZE design 200+ sold; 7,386-review score is shop-wide and not counted as item reviews | `MEDIUM-CANDIDATE` — Named artist CATSNEEZE and four-design artist grouping on the product page; origin not independently tested. | `NOT-RUN` |
| 3 / `P002-DTC-S03` | `TRACE-P002-OBS-DTC-S03-01` | 1 | [Lunar Canyon Tee](https://intotheam.com/collections/mens-graphic-t-shirts/products/lunar-canyon-tee?variant=44225029275705) | ITEM-STRUCTURED / 13700 | `YES` — Named-product JSON-LD reports 13,700 reviews; visible 14,903-review widget appears catalog-wide and is not used as item count | `MEDIUM-CANDIDATE` — Store describes original, hand-drawn artwork made by its illustrator team; origin not independently tested. | `NOT-RUN` |
| 4 / `P002-DTC-S04` | `TRACE-P002-OBS-DTC-S04-01` | 1 | [F Bombs Signature T-Shirt](https://solidthreads.com/collections/mens-t-shirts/products/f-bombs-t-shirt) | ITEM-VISIBLE / 13 | `YES` — Product review widget shows 13 reviews; a separate 83-review label conflicts, so the exact widget count is retained conservatively | `MEDIUM-CANDIDATE` — Store states it creates original designs; origin not independently tested. | `NOT-RUN` |
| 5 / `P002-DTC-S05` | `TRACE-P002-OBS-DTC-S05-01` | 1 | [Ask Me About My Ninja Disguise Flip Men's T Shirt](https://www.crazydogtshirts.com/products/ask-me-about-my-ninja-disguise-shirt) | ITEM-VISIBLE / 7 | `YES` — Seven visible product-specific reviews and named-product structured rating | `LOW-CANDIDATE` — No explicit candidate-level artist or authorship claim was found; origin not independently tested. | `NOT-RUN` |
| 6 / `P002-DTC-S06` | `TRACE-P002-OBS-DTC-S06-02` | 2 | [Coastal Waves](https://aukcliff.com/products/coastal-waves-t-shirt) | ITEM-STRUCTURED / 4 | `YES` — Named-product JSON-LD reports four reviews; 830-review display is explicitly across the shop and is not counted as item reviews | `HIGH-CANDIDATE` — Store says artist made and that designs are made by the store; origin not independently tested. | `NOT-RUN` |
| 7 / `P002-DTC-S07` | `TRACE-P002-OBS-DTC-S07-01` | 1 | [Puff Puff Pass Tee](https://www.seamonkeyapparel.com/collections/staple-tees/products/puff-puff-pass-tee) | ITEM-VISIBLE / 10 | `YES` — Ten visible product-specific reviews; page also labels the item Selling Fast | `HIGH-CANDIDATE` — Store describes original graphics and the item is presented as its own design; origin not independently tested. | `NOT-RUN` |
| 8 / `P002-DTC-S08` | `TRACE-P002-OBS-DTC-S08-02` | 2 | [My Job is Books](https://www.raygunsite.com/collections/t-shirts/products/my-job-is-books) | UNCLEAR | `YES` — Item page rendered a populated Customers who bought this also bought module; this is an inference, and no item review or sold count was exposed | `HIGH-CANDIDATE` — Product page states designed and printed by union labor at RAYGUN; origin not independently tested. | `NOT-RUN` |
| 9 / `P002-DTC-S09` | `TRACE-P002-OBS-DTC-S09-02` | 2 | [EXTRA SPICY TEE](https://pyknic.com/collections/mens-tees/products/extra-spicy-tee) | ITEM-VISIBLE / 22 | `YES` — Twenty-two visible verified-buyer reviews corroborated by named-product JSON-LD | `MEDIUM-CANDIDATE` — Family-owned brand language and seller-specific product page, but no explicit candidate-level artist credit; origin not independently tested. | `NOT-RUN` |
| 10 / `P002-DTC-S10` | `TRACE-P002-OBS-DTC-S10-01` | 1 | [Badlands National Park Women's Rolled Cuff Muscle Shirt Heather Olive](https://www.blackbirdsupply.com/products/badlands-rolled-cuff-shirt-for-women-heather-olive) | UNCLEAR | `UNVERIFIED` — No item review, sold count, or other independent nonzero-sales signal was exposed beyond within-store best-selling rank | `HIGH-CANDIDATE` — Product copy gives a design-specific inspiration account; store states small-batch hand printing in RVA; origin not independently tested. | `NOT-RUN` |
| 11 / `P002-DTC-S11` | `TRACE-P002-OBS-DTC-S11-02` | 2 | [Stay Wild Outdoor Adventure Graphic T-Shirt – Stay Wild SC3100](https://southcoastoutdoorscompany.com/products/stay-wild-sc3100) | ITEM-VISIBLE / 0 | `UNVERIFIED` — Item-specific widget says Be the first to write a review; no independent nonzero-sales signal was exposed beyond within-store best-selling rank | `HIGH-CANDIDATE` — Product page explicitly identifies the graphic as a South Coast Outdoors Co. design; origin not independently tested. | `NOT-RUN` |
| 12 / `P002-DTC-S12` | `TRACE-P002-OBS-DTC-S12-01` | 1 | [Out Of Breath T-shirt](https://slothhikingclub.com/products/out-of-breath-t-shirt) | ITEM-STRUCTURED / 396 | `YES` — Named-product JSON-LD reports 396 reviews; visible 4,613-review display appears shop-wide and is not used as item count | `MEDIUM-CANDIDATE` — Seller-specific product page and named-product structured evidence; no independent authorship/origin test was run. | `NOT-RUN` |

### Same-store continuation preview

The CSV is controlling and contains the full ordered continuation through raw rank 24. The first three canonical surface survivors are shown here as a quick cross-check; any listed fallback still requires its own detail and evidence closeout before origin screening.

| Store | Queue 1 | Queue 2 | Queue 3 |
|---|---|---|---|
| `P002-DTC-S01` | r1 — Men's Ban The Fascists Save The Books T-Shirt | r2 — Men's Someday We'll All Be Dead T-Shirt | r3 — Men's Have The Day You Deserve T-Shirt |
| `P002-DTC-S02` | r1 — 'Feel Alive' Shirt | r2 — 'Live Fast, Eat Trash' Shirt | r3 — 'Purely Spite' Shirt |
| `P002-DTC-S03` | r1 — Lunar Canyon Tee | r2 — Eternal Blossom Vintage Tee | r3 — Evergreen Vintage Tee |
| `P002-DTC-S04` | r1 — F Bombs Signature T-Shirt | r2 — Bad Ass Signature T-Shirt | r4 — Take It Slow Signature T-Shirt |
| `P002-DTC-S05` | r1 — Ask Me About My Ninja Disguise Flip Men's T Shirt | r2 — Can't Work Today My Arm Is In A Cast Men's T Shirt | r3 — That Sounds Like A Horrible Idea. What Time? Men's T Shirt |
| `P002-DTC-S06` | r2 — Coastal Waves | r3 — Captain Puffin Wildlife Photographer | r4 — Captain Puffin Hiker |
| `P002-DTC-S07` | r1 — Puff Puff Pass Tee | r2 — Hard Decisions Tee | r3 — Hula Gang Tee |
| `P002-DTC-S08` | r2 — My Job is Books | r3 — Abolish ICE Heavyweight | r4 — My Job Is Teach |
| `P002-DTC-S09` | r2 — EXTRA SPICY TEE | r3 — QUESADILLAS TEE | r4 — RAISE HELL EAT TACOS TEE |
| `P002-DTC-S10` | r1 — Badlands National Park Women's Rolled Cuff Muscle Shirt Heather Olive | r2 — Mens Gold LP Vinyl Record Music Lover Shirt in Solid Black | r3 — Big & Little Dipper Tshirt Set, Father and Child Gift For Dads Indigo Blue |
| `P002-DTC-S11` | r2 — Stay Wild Outdoor Adventure Graphic T-Shirt – Stay Wild SC3100 | r4 — Live Salty – Sunrises Tide Rises Good Times Coastal Tee SC3000 | r6 — Tarpon Saltwater Fishing Graphic T-Shirt – Tarpon SC2000 |
| `P002-DTC-S12` | r1 — Out Of Breath T-shirt | r2 — Go Outside  T-shirt | r3 — Meese T-shirt |

## Rank-1 outcomes and exceptions

| Store | Rank 1 observation | Rank-1 disposition | Selected raw rank | Basis when rank 1 did not advance |
|---|---|---|---:|---|
| `P002-DTC-S01` | `TRACE-P002-OBS-DTC-S01-01` — Men's Ban The Fascists Save The Books T-Shirt | `QUEUE-HEAD / ORIGIN-PENDING` | 1 | Highest-ranked canonical title/thumbnail survivor. |
| `P002-DTC-S02` | `TRACE-P002-OBS-DTC-S02-01` — 'Feel Alive' Shirt | `QUEUE-HEAD / ORIGIN-PENDING` | 1 | Highest-ranked canonical title/thumbnail survivor. |
| `P002-DTC-S03` | `TRACE-P002-OBS-DTC-S03-01` — Lunar Canyon Tee | `QUEUE-HEAD / ORIGIN-PENDING` | 1 | Highest-ranked canonical title/thumbnail survivor. |
| `P002-DTC-S04` | `TRACE-P002-OBS-DTC-S04-01` — F Bombs Signature T-Shirt | `QUEUE-HEAD / ORIGIN-PENDING` | 1 | Highest-ranked canonical title/thumbnail survivor. |
| `P002-DTC-S05` | `TRACE-P002-OBS-DTC-S05-01` — Ask Me About My Ninja Disguise Flip Men's T Shirt | `QUEUE-HEAD / ORIGIN-PENDING` | 1 | Highest-ranked canonical title/thumbnail survivor. |
| `P002-DTC-S06` | `TRACE-P002-OBS-DTC-S06-01` — Simple | `PRODUCT-EXCLUDED` | 2 | Basic house-mark tee; product page calls it Our own mark and the plainest thing we make |
| `P002-DTC-S07` | `TRACE-P002-OBS-DTC-S07-01` — Puff Puff Pass Tee | `QUEUE-HEAD / ORIGIN-PENDING` | 1 | Highest-ranked canonical title/thumbnail survivor. |
| `P002-DTC-S08` | `TRACE-P002-OBS-DTC-S08-01` — Iowa: We All Are Going to Die Heavyweight | `IP-EXCLUDED` | 2 | Thumbnail and product detail quote U.S. Senator Joni Ernst |
| `P002-DTC-S09` | `TRACE-P002-OBS-DTC-S09-01` — HOPE THEY SERVE TACOS IN HELL TEE | `IP-EXCLUDED` | 2 | Title-led echo of I Hope They Serve Beer in Hell |
| `P002-DTC-S10` | `TRACE-P002-OBS-DTC-S10-01` — Badlands National Park Women's Rolled Cuff Muscle Shirt Heather Olive | `QUEUE-HEAD / ORIGIN-PENDING` | 1 | Highest-ranked canonical title/thumbnail survivor. |
| `P002-DTC-S11` | `TRACE-P002-OBS-DTC-S11-01` — Blue Marlin – Offshore Saltwater Fishing Tee SC1600 | `BRAND-EXCLUDED` | 2 | Rendered thumbnail/product images make the South Coast logo and slogan integral |
| `P002-DTC-S12` | `TRACE-P002-OBS-DTC-S12-01` — Out Of Breath T-shirt | `QUEUE-HEAD / ORIGIN-PENDING` | 1 | Highest-ranked canonical title/thumbnail survivor. |

### Other recorded title/thumbnail exclusions and duplicate-family collapses

The register preserves every row-level disposition. In summary:

- `IP-EXCLUDED`: recognizable entertainment, quotation, public-figure, sports, or logo-parody dependency on the captured surface.
- `BRAND-EXCLUDED`: the principal design is house-logo/source-brand dependent.
- `PRODUCT-EXCLUDED`: basic/non-graphic or test product rather than a substantive fixed graphic-shirt candidate.
- `DUPLICATE-FAMILY`: another raw row carries the same design family; it receives no separate queue credit.

Duplicate collapses are S03 r8 → r1, S03 r19 → r12, S07 r5 → r1, and S11 r24 → r2. All exclusion bases, family-parent IDs, detail-open state, and continuation ranks are machine-readable in the CSV.

## Evidence interpretation

- A native `best-selling` position is the frozen ordering signal, not by itself an independently quantified nonzero-sales count.
- Visible or named-product structured reviews count as candidate-specific corroboration only when attributable. Shop-wide widgets are labeled `SHOP-WIDE` or excluded from the item count.
- S08's populated **Customers who bought this also bought** module is encoded with the normative `YES` value; its evidence basis explicitly preserves that this is an inference, not a numeric item-sales count.
- S10 and S11 remain in the deterministic candidate queue despite `UNVERIFIED` independent sales corroboration because their native within-store rank is valid; that uncertainty must remain visible in later selection decisions.
- Seller authorship language supports only a provisional provenance-candidate grade. It cannot substitute for the frozen wording, cleaned-title, and subject/action/composition origin searches.

## Integrity boundary and next action

Raw DTC capture closed at `2026-09-25T18:28:03.414Z`. No cross-market origin search was run during this stage, and no historical TRACE-PILOT-001 origin outcome was reused to clear, reject, or reorder a family.

Next, process the 12 queue heads in the frozen store order. For each one, run all mandatory origin searches, record first-page/first-10 evidence and representative URLs, then close final Gate 0. If it fails, use that store's next `store_queue_rank` from the CSV and repeat. Failed store slots remain empty if their within-rank-24 queue is exhausted. No SDC may be created before an `ELIGIBLE` closeout.

## Raw-stage friction

- No store failed broad-scope, native-sort, or 24-rank capture verification.
- S06 and S11 ended exactly at 24 products; this is documented as complete collection capture rather than truncation.
- S03 and S07 included variant/alternate-handle repeats; S11 repeated its selected family at rank 24. Family collapse preserves all raw ranks while preventing duplicate candidate credit.
- Review widgets sometimes mixed item and store scope. The conservative item-attribution treatment is preserved above and in the register.
- S10's returned H1 was `COLLECTION: ALL` even though the frozen broad apparel slug was used; the rendered grid remained apparel-only and the requested native sort was active.

No methodology amendment is recommended from DTC raw capture alone. The mandatory origin stage and cross-platform family deduplication remain the controlling tests.

## Controlling S01 final selection — 2026-09-26T17:50Z

S01 Boredwalk closes with its fourth queued candidate, `TRACE-P002-OBS-DTC-S01-04`, Support Your Local Library: `ELIGIBLE`, provenance `MEDIUM`, item-attributable nonzero sales `YES` (132 reviews, verified exact-product entries). The first three queued candidates remain quarantined. The Origin Search Register and D01Q04 supplement control the evidence and limitations.

The civic phrase alone is not treated as a distinctive quotation or copy-family signal. Reviewed alternatives use materially different layouts; Boredwalk claims in-house design authorship. No candidate-specific disputed artwork or protected-adaptation signal was observed in the bounded check. This is research eligibility, not ownership or legal clearance.

Under the frozen one-family-per-store limit, S01 ranks 5–22 are not reached. No EF ID or SDC is assigned before global selection closes. Continue S02 Wicked Clothes, queue rank 1, Feel Alive.

## Controlling S02 final selection — 2026-09-26T17:55Z

Wicked Clothes closes with queue rank 2, `TRACE-P002-OBS-DTC-S02-02`, Live Fast, Eat Trash: `ELIGIBLE`, provenance `MEDIUM`, nonzero sales `YES`. Exact candidate artwork was visually matched to Vincent Trinidad's Threadless design, and the linked artist catalog identifies the same illustrator credited by Wicked Clothes. Cross-seller recurrence is recorded but creator-traced; other outlets receive no independent-family credit. This is not a finding that all recurring sellers have permission.

Queue rank 1, Feel Alive, is `IP-QUARANTINE`; its CATSNEEZE credit alone did not resolve the specific recurring skeleton/plant composition. Its raw nonzero-sales YES is superseded by UNVERIFIED because the 200+ marker is adjacent to an artist group and the reviews are shop-wide. For selected rank 2, the separate item-specific 150+ bought in past month marker supplies corroboration; the 2K+ artist count and 7,386 shop reviews are not used.

Later S02 candidates are not reached. Continue S03 INTO THE AM at Lunar Canyon, retaining its original observation and raw rank. No EF/SDC assignment yet.

## Controlling S03 final selection — 2026-09-26T18:03Z

INTO THE AM closes with Lunar Canyon, `TRACE-P002-OBS-DTC-S03-01`: `ELIGIBLE`, provenance `MEDIUM`, nonzero sales `YES`. Four required no-text searches are complete. The source attributes designs to its illustrator team; the nearest visual comparator is materially distinct. Brand-identical mirror pages receive no independent credit or assumed affiliation.

The native 14,903-review widget mixes other products and is excluded from item counts, superseding reliance on the raw named-product aggregate. The exact Shop product review section supplies 24 ratings and dated customer entries; conflicting top-page placeholders are not used. Raw rank 8 remains a duplicate; later S03 candidates are not reached. Continue S04 Solid Threads, F Bombs Signature T-Shirt.
