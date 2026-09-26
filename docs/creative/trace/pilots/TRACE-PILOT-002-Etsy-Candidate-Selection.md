---
title: TRACE-PILOT-002 — Etsy Raw Scan and Pre-Origin Candidate Queue
owner: Creative Director
status: Raw frame complete — provenance closure pending
pilot_id: TRACE-PILOT-002
pool_id: TRACE-P002-POOL-ETSY
methodology_version: TRACE v0.3
methodology_frozen_commit: 0b74489e083d58d8037129247399d3cece866de6
preregistration_commit: f5f3291
observation_date: 2026-09-25
surface_capture_start_utc: 2026-09-25T18:01:24.473Z
surface_capture_end_utc: 2026-09-25T18:03:26.760Z
detail_capture_start_utc: 2026-09-25T18:06:25.464Z
detail_capture_end_utc: 2026-09-25T18:09:12.777Z
---

# TRACE-PILOT-002 — Etsy Raw Scan and Pre-Origin Candidate Queue

## Controlling status

The frozen Etsy raw frame is complete. This artifact stops before the mandatory cross-market origin searches and before final Gate 0.

- All 12 preregistered query/sort surfaces are `COMPLETE`.
- The CSV contains 156 rows after its header: 12 `SURFACE` rows and 144 `ORGANIC` rows.
- The organic observations resolve to 109 unique listing IDs and 35 repeated listing occurrences.
- No interleaved ad card rendered before organic ordinal 12 on any captured surface. This is a statement about these snapshots, not Etsy generally.
- Sixty-four unique listings survived the closed title/thumbnail screen as candidates. Their item pages were opened.
- Two additional conservative title cases were opened before closeout and then classified as fame/IP-dependent, so 66 listing pages were inspected in total.
- The pre-origin queue contains 22 families: 17 `RECENT-SALES-BADGE` candidates and 5 `ITEM-REVIEW-DEPTH` candidates.
- No origin query has been run, no family is finally `ELIGIBLE`, no expression-family ID has been assigned, and no Source Decode Card has been created.

The machine-readable controlling register is [TRACE-PILOT-002-Etsy-Scan-Register.csv](./TRACE-PILOT-002-Etsy-Scan-Register.csv).

## Session and execution controls

- Session: signed out.
- Country / ship-to country: United States.
- Language: English (US).
- Currency: USD.
- Access mode: live browser-rendered Etsy pages.
- Frozen filter: `instant_download=false`.
- Traversal: query-major; `Most relevant` then `Top reviews` for each of the six methodology queries.
- Organic ordinal: ads never occupy it.
- Captured observation ID: `TRACE-P002-OBS-ETSY-<captured-scan>-<organic-ordinal>`.
- Cohort credit: only a complete surface may supply first-occurrence or queue credit.

## Surface register

| Scan | Query order | Query | Sort | Status | Organic | Ads before organic 12 | Scroll/wait cycles | Closed at UTC |
|---|---:|---|---|---|---:|---:|---:|---|
| `01-MR` | 1 | `graphic t shirt` | Most relevant | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:01:24.473Z` |
| `02-TR` | 1 | `graphic t shirt` | Top reviews | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:03:14.359Z` |
| `03-MR` | 2 | `funny t shirt` | Most relevant | COMPLETE | 12 | 0 | 1 | `2026-09-25T18:03:26.760Z` |
| `04-TR` | 2 | `funny t shirt` | Top reviews | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:01:39.691Z` |
| `05-MR` | 3 | `novelty t shirt` | Most relevant | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:01:44.040Z` |
| `06-TR` | 3 | `novelty t shirt` | Top reviews | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:01:47.340Z` |
| `07-MR` | 4 | `text t shirt` | Most relevant | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:01:51.337Z` |
| `08-TR` | 4 | `text t shirt` | Top reviews | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:01:55.212Z` |
| `09-MR` | 5 | `illustrated t shirt` | Most relevant | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:01:59.800Z` |
| `10-TR` | 5 | `illustrated t shirt` | Top reviews | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:02:04.148Z` |
| `11-MR` | 6 | `retro graphic t shirt` | Most relevant | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:02:08.086Z` |
| `12-TR` | 6 | `retro graphic t shirt` | Top reviews | COMPLETE | 12 | 0 | 0 | `2026-09-25T18:02:11.520Z` |

`02-TR` and `03-MR` initially exposed a capture-instrumentation problem: the first counter treated duplicate DOM anchors as separate cards. No selection or queue credit was assigned from that intermediate state. Both surfaces were later authoritatively reclosed using unique listing IDs before any queue was constructed; the timestamps above preserve that reclosure after several later-numbered surfaces. `03-MR` required one of the three allowed five-second scroll/wait cycles, while `02-TR` returned a complete unique frame without a cycle. No queue tie depended on first occurrence, so the reclosure chronology changed no rank or candidate. The CSV preserves this friction in the surface notes.

## Immutable ID-format friction and crosswalk

At capture, observation IDs were immutably assigned with descriptive scan tokens such as `TRACE-P002-OBS-ETSY-01-MR-01`. The execution-schema clarification recorded after capture at 18:04 UTC standardized the scan aliases as `S01` through `S12`. Renumbering would violate the frozen immutability rule, so the captured IDs remain controlling. This is format friction only; it changes no surface, ordinal, eligibility, ordering, or selection decision.

| Captured scan token | Standard alias |
|---|---|
| `01-MR` | `S01` |
| `02-TR` | `S02` |
| `03-MR` | `S03` |
| `04-TR` | `S04` |
| `05-MR` | `S05` |
| `06-TR` | `S06` |
| `07-MR` | `S07` |
| `08-TR` | `S08` |
| `09-MR` | `S09` |
| `10-TR` | `S10` |
| `11-MR` | `S11` |
| `12-TR` | `S12` |

All expression-family and SDC joins must use the captured observation IDs in the CSV. The standard aliases are lookup aids only.

## Title/thumbnail and item-page closeout

### Unique-listing screen

| Pre-origin state | Unique listings | Treatment |
|---|---:|---|
| `ORIGIN-PENDING` | 48 | Fixed graphic candidate with attributable evidence state recorded; no final Gate 0 until origin search |
| `IP-EXCLUDED` | 26 | Named franchise, entertainment, celebrity/public-figure, artist, sports, viral-fame, or revealed character dependency |
| `PRODUCT-EXCLUDED` | 21 | Custom/personalized service, add-on, or non-fixed/non-shirt unit |
| `ATTRIBUTION-EXCLUDED` | 12 | Mixed or non-item-attributable review pool |
| `BRAND-EXCLUDED` | 1 | Reviews explicitly showed source-creator/brand support as the demand driver |
| `EVIDENCE-QUARANTINE` | 1 | No official badge or attributable item-review demand evidence |

The closed title/thumbnail screen contains 24 objective IP/fame exclusions and 21 objective product/service exclusions. Two additional IP cases were revealed only after opening a candidate page: Vox/Alastor character merchandise and an `Amaze / Space Mary` entertainment-property expression. The `HELLOW!` listing was excluded as brand-dependent because its own item reviews explicitly described supporting Shepherd Farms/Sarah and the “HELLOW Army.” These are contamination controls, not infringement findings.

For every opened candidate, the register records:

- whether Etsy displayed its own `Bestseller` badge;
- whether the page exposed a visible `Reviews for this item` section;
- the item-specific review count only when that scope was attributable;
- the latest displayed item-review date;
- `EXACT`, `SAME-PRINT-VARIANTS`, `MIXED`, or `UNCLEAR` attribution;
- the detail capture time and preliminary disposition.

A schema aggregate was not treated as item-specific when the page lacked a `Reviews for this item` section.

## Ranked provenance queue

This is a deterministic work queue, not a selected or cleared source set. Process each lane from rank 1 downward. For every candidate, run all three frozen origin searches on both the source-platform surface and the open web, review the first 10 organic results on each surface, then close final Gate 0. Continue down the badge queue until six families clear or the queue is exhausted. The review-depth lane has only five pre-origin qualifiers, so it cannot reach its target of six unless the frozen evidence facts change; do not borrow from the badge lane or another platform.

### RECENT-SALES-BADGE

Ordering: item-specific review count descending, latest displayed item-review date descending, cleaner attribution, then earlier first occurrence.

| Queue rank | Listing | Shop | Item reviews | Latest displayed item review | Attribution | Canonical observation | Origin searches |
|---:|---|---|---:|---|---|---|---|
| 1 | [Salty Girl Tee: Women's Vintage Cotton Blend T-Shirt](https://www.etsy.com/listing/4332571417/salty-girl-tee-womens-vintage-cotton) | Tokfun | 815 | 2026-09-25 | EXACT | `TRACE-P002-OBS-ETSY-01-MR-06` | `NOT-RUN` |
| 2 | [Three Raccoons Retro Graphic T-shirts, Vintage Comfort Colors® Raccoon Moon Tshirt, Raccoon Lovers, Funny Raccon Tee, Oversized Washed Tee](https://www.etsy.com/listing/1800339871/three-raccoons-retro-graphic-t-shirts) | OldSchoolCulture | 486 | 2026-09-14 | EXACT | `TRACE-P002-OBS-ETSY-11-MR-08` | `NOT-RUN` |
| 3 | [Mitochondria Vintage Science T-Shirt, Retro Biology Graphic Tee, 90s Academic Cell Diagram Shirt, Geek Lab Humor Top, STEM Learning Gift](https://www.etsy.com/listing/4414449167/mitochondria-vintage-science-t-shirt) | RetroFluent | 127 | 2026-09-21 | EXACT | `TRACE-P002-OBS-ETSY-03-MR-11` | `NOT-RUN` |
| 4 | [Comfort Colors Bigfoot Dandelion Shirt, Vintage Sasquatch Nature Tee, Woodland Cryptid Graphic T-Shirt, Outdoor Adventure Gift](https://www.etsy.com/listing/4520342710/comfort-colors-bigfoot-dandelion-shirt) | Monlesacx | 71 | 2026-09-24 | EXACT | `TRACE-P002-OBS-ETSY-01-MR-10` | `NOT-RUN` |
| 5 | [Artistic Cats Inspired by Famous Painters, Funny Cat Art, Minimalist Illustration, Gift for Artist or Art Teacher, Art Shirt, Aesthetic Tee](https://www.etsy.com/listing/4302187056/artistic-cats-inspired-by-famous) | AlanaDesings | 65 | 2026-08-28 | EXACT | `TRACE-P002-OBS-ETSY-09-MR-02` | `NOT-RUN` |
| 6 | [Retro Cat Shirt, Oversize, Womens, Mens, Unisex Comfort Colors T-shirt](https://www.etsy.com/listing/4531565663/retro-cat-shirt-oversize-womens-mens) | KickAshCo | 29 | 2026-09-21 | EXACT | `TRACE-P002-OBS-ETSY-11-MR-12` | `NOT-RUN` |
| 7 | [Comfort Colors® Ellas Fellas Club Shirt, Retro Western Cowboy T-Shirt, Country Concert Tee](https://www.etsy.com/listing/4507117950/comfort-colors-ellas-fellas-club-shirt) | HoneyTeesUS | 22 | 2026-09-19 | SAME-PRINT-VARIANTS | `TRACE-P002-OBS-ETSY-12-TR-12` | `NOT-RUN` |
| 8 | [Getting Meowied Shirt, Funny Cat Bride Tee, Cat Wedding Shirt, Bachelorette Cat Lover Gift, Bridal Shower Cat Graphic Tee](https://www.etsy.com/listing/4540503129/getting-meowied-shirt-funny-cat-bride) | CatDistributor | 17 | 2026-09-25 | EXACT | `TRACE-P002-OBS-ETSY-03-MR-09` | `NOT-RUN` |
| 9 | [JAWS at Walnut Beach Vintage Merch \| Adult & Youth T-Shirts \| Vinyl Beach Sticker \| Milford, Connecticut Souvenirs + Gifts](https://www.etsy.com/listing/4532612141/jaws-at-walnut-beach-vintage-merch-adult) | nefarmhousedesign | 15 | 2026-09-22 | SAME-PRINT-VARIANTS | `TRACE-P002-OBS-ETSY-06-TR-07` | `NOT-RUN` |
| 10 | [ART T Shirt \| Minimal Typography Tee \| Modern Graphic Shirt](https://www.etsy.com/listing/4443906535/art-t-shirt-minimal-typography-tee) | UnrushedGoods | 9 | 2026-09-23 | EXACT | `TRACE-P002-OBS-ETSY-07-MR-02` | `NOT-RUN` |
| 11 | [Lake Ontario Shirt, Great Lakes Sunset Graphic Tee, Retro Canada Vacation Gift, Cottage Country Outdoor Comfort Colors Shirt](https://www.etsy.com/listing/4563877335/lake-ontario-shirt-great-lakes-sunset) | TheMeroPixel | 9 | 2026-09-17 | EXACT | `TRACE-P002-OBS-ETSY-01-MR-05` | `NOT-RUN` |
| 12 | [Respect Your Mother  Rhinestone T-Shirt, Unisex Short Sleeve Statement Top for Casual Everyday Wear](https://www.etsy.com/listing/4567026619/respect-your-mother-rhinestone-t-shirt) | DailyCraftTexas | 7 | 2026-09-22 | EXACT | `TRACE-P002-OBS-ETSY-02-TR-08` | `NOT-RUN` |
| 13 | [Due To Not Wanting To I Will Not Thanks Shirt, Funny Cat Tee, Sarcastic Quote Shirt, Introvert Shirt, Mood Shirt, Cat Lover Gift](https://www.etsy.com/listing/4537001084/due-to-not-wanting-to-i-will-not-thanks) | IVANZLOCHEVSKYI | 7 | 2026-09-20 | EXACT | `TRACE-P002-OBS-ETSY-07-MR-12` | `NOT-RUN` |
| 14 | [Vintage Butterfly Botanical Chart Shirt Nature Moth Comfort Colors Tee](https://www.etsy.com/listing/4517356927/vintage-butterfly-botanical-chart-shirt) | BeeDesignCollection | 5 | 2026-09-23 | EXACT | `TRACE-P002-OBS-ETSY-01-MR-08` | `NOT-RUN` |
| 15 | [First of All, I'm a Delight T-Shirt \| Halloween Medusa Spooky Tee](https://www.etsy.com/listing/4565216251/first-of-all-im-a-delight-t-shirt) | SarcasticRebelShop | 4 | 2026-09-19 | EXACT | `TRACE-P002-OBS-ETSY-03-MR-08` | `NOT-RUN` |
| 16 | [Positive Encouragement Graphic Tee, Inspirational Teacher Motivation Shirt, Classroom Confidence Apparel, Comfort Colors® Gift Tee](https://www.etsy.com/listing/4539236796/positive-encouragement-graphic-tee) | ThreadPeakShop | 4 | 2026-09-15 | EXACT | `TRACE-P002-OBS-ETSY-07-MR-11` | `NOT-RUN` |
| 17 | [Retro Halloween Shirt, Y2K Comfort Colors Tee, Vintage Black Cat Ghost Skeleton T Shirt, Spooky Cute Pumpkin Witch Graphic Tee](https://www.etsy.com/listing/4572306570/retro-halloween-shirt-y2k-comfort-colors) | EverChangingJourney | 3 | 2026-09-24 | EXACT | `TRACE-P002-OBS-ETSY-01-MR-02` | `NOT-RUN` |

Queue-specific cautions:

- Seller authorship language is only a provenance input; it cannot override cross-seller recurrence.
- `Artistic Cats Inspired by Famous Painters` requires both public-domain-subject and modern-adaptation scrutiny.
- `Ellas Fellas Club` requires a fame/country-artist dependency check.
- `JAWS at Walnut Beach` includes adult/youth shirts and a sticker carrying the same print, so it is ranked as `SAME-PRINT-VARIANTS`; the origin screen must also test film/trade-dress dependence.
- Historical TRACE-PILOT-001 origin findings were not reused to clear, reject, or reorder any family.

### ITEM-REVIEW-DEPTH

Ordering: non-badged listings with at least 100 item-specific reviews and an item review displayed within the previous 180 days; review count descending, latest date descending, cleaner attribution, then earlier first occurrence. The fixed cutoff for this observation date is 2026-03-29.

| Queue rank | Listing | Shop | Item reviews | Latest displayed item review | Attribution | Canonical observation | Origin searches |
|---:|---|---|---:|---|---|---|---|
| 1 | [Cat Guitarist Men's Tee: Funny Feline Playing Music Graphic Novelty Shirt for Animal Lovers](https://www.etsy.com/listing/671213378/cat-guitarist-mens-tee-funny-feline) | missionthread | 1708 | 2026-04-24 | EXACT | `TRACE-P002-OBS-ETSY-06-TR-02` | `NOT-RUN` |
| 2 | [Jesus Riding Dinosaur T Shirt Funny T Shirts for Men Women UFO T Shirt Offensive Shirt Cool Graphic T Shirts Crazy Shirts T Rex Novelty Tee](https://www.etsy.com/listing/560142098/jesus-riding-dinosaur-t-shirt-funny-t) | Shirtmandude | 1024 | 2026-07-14 | EXACT | `TRACE-P002-OBS-ETSY-04-TR-08` | `NOT-RUN` |
| 3 | [Funny Dad Jokes T-Shirt, Father's Day Gift](https://www.etsy.com/listing/1012093892/funny-dad-jokes-t-shirt-fathers-day-gift) | CrazyDogTshirts | 857 | 2026-09-08 | EXACT | `TRACE-P002-OBS-ETSY-04-TR-07` | `NOT-RUN` |
| 4 | [Funny Possum Shirt T Shirt for Men Women Guys Possum T Shirt Cool Animal Graphic Tshirt Raccoon Live Weird Fake Your Death Silly Graphic Tee](https://www.etsy.com/listing/759163386/possum-shirt-funny-t-shirt-for-men-women) | Shirtmandude | 518 | 2026-07-31 | EXACT | `TRACE-P002-OBS-ETSY-05-MR-10` | `NOT-RUN` |
| 5 | [Breweries Are Calling T-Shirt, Hand Illustrated Beer Lover Tee](https://www.etsy.com/listing/549555574/breweries-are-calling-t-shirt-hand) | brewershirts | 395 | 2026-06-21 | EXACT | `TRACE-P002-OBS-ETSY-10-TR-11` | `NOT-RUN` |

A sixth non-badged family did not meet all frozen requirements. In particular, high search-card or schema counts without an item-specific review section were excluded, and `Master Baiter` had 182 item-specific reviews but its newest displayed item review was 2026-01-15, outside the 180-day window.

## Deterministic continuation

1. Preserve the observation IDs and queue ranks in the CSV.
2. Run provenance closure lane-by-lane; do not skip a difficult candidate or use analyst taste.
3. Record every required wording, cleaned-title, and subject/action/composition query, first-10 organic-result review, comparison, representative URL, and UTC time.
4. Apply the three-family commercial-source cap after expression-family deduplication.
5. Assign global `TRACE-P002-EF-###` IDs only after cross-platform family deduplication and final eligibility closeout.
6. Do not create an Etsy SDC until final Gate 0 is `ELIGIBLE`.
7. Do not backfill a post-selection failure.

## Friction and blockers

- **No blocked Etsy surface.** All 12 frames completed.
- **Bounded-load friction, resolved:** one surface needed one allowed scroll/wait cycle.
- **Instrumentation friction, recorded:** a duplicate-anchor counter briefly misclassified two surfaces before unique-ID closure; no downstream decision used that intermediate state.
- **ID-format friction, recorded:** post-capture `S01`–`S12` aliases are crosswalked without changing immutable IDs; no selection effect.
- **Dynamic advertising:** no ad was interleaved before organic ordinal 12 in this session, unlike some earlier snapshots. The protocol handled the zero-ad state without shifting ordinals.
- **Review-depth shortfall:** only five non-badged families met the 100-review and 180-day item-attribution floor before provenance review.
- **Provenance is the controlling open gate:** 22 queued families still require all mandatory origin searches. Nothing in this artifact is ready for decoding or downstream creative credit.

No methodology amendment is recommended from the raw Etsy stage alone. The provenance closeout and five-card checkpoint must determine whether this friction is merely operational or changes an eligibility, ordering, identity, lineage, or downstream-support decision.
