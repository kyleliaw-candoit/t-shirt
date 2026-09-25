---
title: TRACE-PILOT-001 — Etsy Scan, Final Audit, and Source Decodes
owner: Creative Director
status: Complete — frozen v0.2 execution
pilot_id: TRACE-PILOT-001
methodology_version: TRACE v0.2
methodology_frozen_commit: c383e2d90619e594b38b65dbd3508638d6e845d0
observation_date: 2026-09-25
---

# TRACE-PILOT-001 — Etsy Scan, Final Audit, and Source Decodes

## Execution basis

- Frozen methodology: `docs/company/TRACE-Bestseller-Creative-Intelligence-Methodology.md`
- Frozen commit: `c383e2d90619e594b38b65dbd3508638d6e845d0`
- Observation date: 2026-09-25
- Session: signed out; United States; English (US); USD; Etsy displayed ship-to Plano, Texas
- Traversal interpretation: query-major in the frozen query-bank order; `Most relevant` before `Top reviews` for each query
- Etsy appended `instant_download=false` to every resulting search URL.

The complete machine-readable register is [TRACE-PILOT-001-Etsy-Scan-Register.csv](./TRACE-PILOT-001-Etsy-Scan-Register.csv). It contains all 144 frozen organic observations, all 85 ads visible on the loaded result pages, exact listing IDs, first-occurrence/deduplication status, dispositions, listing-page evidence where inspected, and the selected-family ranks. Its `source_family_id` field is the stable pilot-scoped join key for the table and records below; it is populated only on each selected family's canonical first-occurrence row. For those 12 rows, `final_audit_disposition` is the controlling source-use status after the final Gate 0 audit; it does not rewrite the frozen execution selection.

## Scan completion

| Scan | Query | Sort | Organic captured | Ads recorded | Verified result URL |
|---:|---|---|---:|---:|---|
| 1 | graphic t shirt | Most relevant | 12 | 8 | `https://www.etsy.com/search?q=graphic+t+shirt&instant_download=false` |
| 2 | graphic t shirt | Top reviews | 12 | 12 | `https://www.etsy.com/search?q=graphic+t+shirt&order=highest_reviews&instant_download=false` |
| 3 | funny t shirt | Most relevant | 12 | 0 | `https://www.etsy.com/search?q=funny+t+shirt&instant_download=false` |
| 4 | funny t shirt | Top reviews | 12 | 12 | `https://www.etsy.com/search?q=funny+t+shirt&order=highest_reviews&instant_download=false` |
| 5 | novelty t shirt | Most relevant | 12 | 0 | `https://www.etsy.com/search?q=novelty+t+shirt&instant_download=false` |
| 6 | novelty t shirt | Top reviews | 12 | 12 | `https://www.etsy.com/search?q=novelty+t+shirt&order=highest_reviews&instant_download=false` |
| 7 | text t shirt | Most relevant | 12 | 1 | `https://www.etsy.com/search?q=text+t+shirt&instant_download=false` |
| 8 | text t shirt | Top reviews | 12 | 12 | `https://www.etsy.com/search?q=text+t+shirt&order=highest_reviews&instant_download=false` |
| 9 | illustrated t shirt | Most relevant | 12 | 4 | `https://www.etsy.com/search?q=illustrated+t+shirt&instant_download=false` |
| 10 | illustrated t shirt | Top reviews | 12 | 12 | `https://www.etsy.com/search?q=illustrated+t+shirt&order=highest_reviews&instant_download=false` |
| 11 | retro graphic t shirt | Most relevant | 12 | 0 | `https://www.etsy.com/search?q=retro+graphic+t+shirt&instant_download=false` |
| 12 | retro graphic t shirt | Top reviews | 12 | 12 | `https://www.etsy.com/search?q=retro+graphic+t+shirt&order=highest_reviews&instant_download=false` |

Totals: 144 organic slots, 121 unique listing IDs, 85 separately recorded ads. Fifty-nine candidate pages were opened for badge, item-review, recency, attribution, eligibility, or quarantine checks. Every one of the 51 title/thumbnail-eligible fixed-design candidates was opened.

## Execution-time first-occurrence family dispositions

| Disposition | First-occurrence listing records | Notes |
|---|---:|---|
| `ELIGIBLE` | 50 | Includes the 12 families selected at execution and 38 evidence-qualified but unselected families. The final audit below supersedes source-use status for the selected set. |
| `PRODUCT-EXCLUDED` | 36 | Custom/personalized printing, add-ons, or non-fixed design units. |
| `IP-EXCLUDED` | 25 | Named franchise, film, game, band, celebrity, sports identity, lyric, brand-led identity, or direct public-figure dependence. |
| `IP-QUARANTINE` | 8 | Origin, public-personality/cause dependence, quotation, or artwork provenance unresolved. |
| `DUPLICATE-FAMILY` | 1 | Second Pasta Pups dachshund/spaghetti expression; spread evidence only. |
| `ATTRIBUTION-EXCLUDED` | 1 | One listing mixed multiple quote/design outcomes. |

Subsequent occurrences of an already observed listing ID are marked `DUPLICATE-FAMILY` at row level in the CSV while preserving the first family disposition. These counts preserve the execution-time scan register; they are not the final source-use count.

## Execution-time selected Etsy families and final Gate 0 audit

All 12 sources selected at execution showed Etsy's official `Bestseller` badge. The badge popover stated that the item had high sales volume over the previous six months. All item counts below came from `Reviews for this item`, not the shop-wide counts shown on search cards.

The strict final Gate 0 cross-market provenance audit leaves one source `ELIGIBLE` for downstream decoding and quarantines 11 that had been selected at execution. The frozen ranks, IDs, and raw observations remain intact for reproducibility. No replacement family was backfilled.

This is conservative contamination control, not a finding that any seller or listing infringes intellectual-property rights. Cross-market recurrence establishes unresolved origin or clone-family risk; it does not establish ownership, copying direction, authorization, or infringement.

Shared evidence vector: `PLATFORM-BADGED | SAME-PRINT-VARIANTS | RECENT | SINGLE-SNAPSHOT`.

| Rank | Source-family ID | Listing / shop | First frozen occurrence | Item reviews; visible recent dates | Final audit | Execution note / final audit reason |
|---:|---|---|---|---|---|---|
| 1 | `TRACE-P001-ETSY-01` | [Salty Girl Tee](https://www.etsy.com/listing/4332571417/salty-girl-tee-womens-vintage-cotton) — Tokfun | Scan 5, `novelty t shirt`, Most relevant, organic #10 | 814; Sep 23, Sep 21, Sep 20, 2026 | `IP-QUARANTINE` | Exact phrase/reveal and raincoat/umbrella expression recur across unrelated listings and markets; origin is unresolved. |
| 2 | `TRACE-P001-ETSY-02` | [Three Raccoons](https://www.etsy.com/listing/1800339871/three-raccoons-retro-graphic-t-shirts) — OldSchoolCulture | Scan 12, `retro graphic t shirt`, Top reviews, organic #6 | 486; Sep 14, Sep 8, Sep 5, Aug 31, 2026 | `IP-QUARANTINE` | The three-raccoons/full-moon expression recurs across unrelated Etsy and Walmart offers; origin is unresolved. |
| 3 | `TRACE-P001-ETSY-03` | [Huzzah Frog with Sword](https://www.etsy.com/listing/4350974897/huzzah-frog-with-sword-tee-embroidered) — PineSpiceBooks | Scan 5, `novelty t shirt`, Most relevant, organic #4 | 269; Sep 19, Sep 13, Sep 8, Sep 1, 2026 | `IP-QUARANTINE` | The Huzzah/frog/sword expression recurs across unrelated offers; origin is unresolved. |
| 4 | `TRACE-P001-ETSY-04` | [Mitochondria](https://www.etsy.com/listing/4414449167/mitochondria-vintage-science-t-shirt) — RetroFluent | Scan 5, `novelty t shirt`, Most relevant, organic #5 | 127; Sep 21, Sep 19, Sep 18, Sep 15, 2026 | `IP-QUARANTINE` | The exact Mitochondria/Powering Life Since Forever expression recurs across unrelated Etsy and SHEIN offers; origin is unresolved. |
| 5 | `TRACE-P001-ETSY-05` | [Gangster Cats](https://www.etsy.com/listing/4479852711/funny-gangster-cat-shirt-meme-cats) — CatDistributor | Scan 1, `graphic t shirt`, Most relevant, organic #7 | 102; Sep 24, Sep 22, Sep 21, 2026 | `IP-QUARANTINE` | Selected at execution, then conservatively quarantined because the original analysis recorded unknown artwork provenance; seller-side design/AI-assistance disclosure did not resolve underlying source-asset origin. |
| 6 | `TRACE-P001-ETSY-06` | [Rock Star Cat](https://www.etsy.com/listing/4472721533/rock-star-cat-shirt-vintage-kitten-y2k) — CitrusTeeShop | Scan 1, `graphic t shirt`, Most relevant, organic #3 | 79; Sep 25, Sep 24, Sep 23, 2026 | `IP-QUARANTINE` | The exact Rock Star Cat/guitar title and expression recur on Walmart; origin is unresolved. |
| 7 | `TRACE-P001-ETSY-07` | [Fighting Leopards](https://www.etsy.com/listing/4496061696/vintage-leopard-fighting-graphic-tee) — ThreadPeakShop | Scan 1, `graphic t shirt`, Most relevant, organic #8 | 36; Sep 22, Sep 21, Sep 18, 2026 | `IP-QUARANTINE` | The exact Vintage Leopard Fighting title/expression recurs on TeePublic and SHEIN; origin is unresolved. |
| 8 | `TRACE-P001-ETSY-08` | [Poker Cats](https://www.etsy.com/listing/4444727416/poker-cats-vintage-graphic-t-shirt-retro) — OldSchoolCulture | Scan 5, `novelty t shirt`, Most relevant, organic #9 | 20; Sep 16, Sep 7, Sep 6, 2026 | `IP-QUARANTINE` | Selected at execution, then quarantined because its cross-seller template/copy relationship with `TRACE-P001-ETSY-05` and the photographic-source origin remain unresolved. |
| 9 | `TRACE-P001-ETSY-09` | [Everything Is Temporary](https://www.etsy.com/listing/4538546086/everything-is-temporary-design-acid-wash) — Printtostitch | Scan 1, `graphic t shirt`, Most relevant, organic #12 | 14; Sep 24, Sep 19, Sep 15, Sep 14, 2026 | `IP-QUARANTINE` | The exact phrase, acid-wash front/back format, title, and expression recur on SHEIN; origin is unresolved. |
| 10 | `TRACE-P001-ETSY-10` | [I Never Question My Wife's Choices](https://www.etsy.com/listing/4490363105/funny-husband-shirt-i-never-question-my) — BlazingBrite | Scan 3, `funny t shirt`, Most relevant, organic #12 | 10; Sep 22, Sep 11, Sep 6, Sep 4, 2026 | `IP-QUARANTINE` | The exact Wife's Choices phrase recurs across unrelated Etsy and independent-store offers; origin is unresolved. |
| 11 | `TRACE-P001-ETSY-11` | [Boho Sun](https://www.etsy.com/listing/4521474627/boho-sun-t-shirt-retro-celestial-sky-tee) — RetroFluent | Scan 1, `graphic t shirt`, Most relevant, organic #6 | 10; Sep 20, Sep 18, Sep 7, Aug 25, 2026 | `IP-QUARANTINE` | The Boho Sun composition/title recurs across unrelated sellers; origin is unresolved. |
| 12 | `TRACE-P001-ETSY-12` | [ART](https://www.etsy.com/listing/4443906535/art-t-shirt-minimal-typography-tee) — UnrushedGoods | Scan 9, `illustrated t shirt`, Most relevant, organic #2 | 9; Sep 23, Sep 18, Sep 8, 2026 | `ELIGIBLE` | Generic identity word rendered as a fixed typographic composition. |

The seller cap passes for the 12 execution selections. The one final-qualifying source comes from one shop.

The first family below the execution cutoff was Lake Ontario sunset, also badged with nine item reviews, but its most recent displayed item review was Sep 17. `ART` had a Sep 23 item review and also appeared earlier in the interpreted frozen traversal. The exact definition of the recency tiebreak remains a methodology ambiguity. The 11 final quarantines were not backfilled, so the controlling Etsy source set contains one family.

## Final-qualifying Source Decode Card

### TRACE-P001-ETSY-12 — ART

- **Observed expression:** The lower-case word `art` is broken into oversized red letters, rotated/stacked vertically on an off-white shirt.
- **Source context:** Artists/design-oriented wearers. No insider truth beyond identity and comfort with formal experimentation.
- **Public signal / payoff:** Minimal identity declaration with visual sophistication.
- **Candidate mechanism:** Turn the identity word itself into a demonstration of the named practice.
- **Apparel grammar:** One word; oversized lower-case letters; rotation and stacking; one ink color; strong negative space.
- **Alternative explanations/confounders:** Minimalism, gallery/store aesthetic, fashion styling, and broad low-risk identity signal.
- **Prohibited transfer:** `art`, the exact letter rotations/stack, red/off-white treatment, and scale.
- **Confidence:** Strong demand evidence; medium apparel-grammar confidence and low-to-medium concept-recipe confidence.

## Selected-then-quarantined post-selection audit records

These 11 records preserve what was observed and why each family entered the frozen execution selection. They are audit-only records, not source-decode cards (SDCs). Their final `IP-QUARANTINE` status means they supply no SDC, mechanism, apparel-grammar, recipe, recurrence, corroboration, or transfer evidence. Cross-market recurrence is used only as conservative contamination control; it is not an infringement finding and does not establish ownership, copying direction, or authorization.

### TRACE-P001-ETSY-01 — Salty Girl

- **Execution record:** Selected at rank 1 with an official `Bestseller` badge and 814 item reviews.
- **Observed expression:** Setup text resolves into oversized distressed `SALTY`; a person in a yellow raincoat stands under an umbrella in rain.
- **Contamination evidence:** The exact phrase plus raincoat/umbrella expression appears in listings on both [TeePublic](https://www.teepublic.com/t-shirt/98027519-all-these-flavors-and-you-choose-to-be-salty-cute-) and [Etsy](https://www.etsy.com/listing/4487469041/salty-girl-tee-womens-vintage-cotton). Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-02 — Three Raccoons

- **Execution record:** Selected at rank 2 with an official `Bestseller` badge and 486 item reviews.
- **Observed expression:** Three photoreal raccoons form a large chest collage before a full moon and atmospheric night sky.
- **Contamination evidence:** The three-raccoons/full-moon expression recurs across unrelated Etsy and Walmart offers, including [Walmart](https://www.walmart.com/ip/20621519954) and a [separate Etsy listing](https://www.etsy.com/listing/1716481453/raccoon-moon-shirt-three-raccoons). Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-03 — Huzzah Frog with Sword

- **Execution record:** Selected at rank 3 with an official `Bestseller` badge and 269 item reviews.
- **Observed expression:** A small embroidered green frog in a red cape raises a sword; `HUZZAH` sits below.
- **Contamination evidence:** The Huzzah/frog/sword expression recurs across unrelated sellers, including [Shawncraft](https://www.shawncraft.com/products/huzzah-frog-with-sword-embroidered-t-shirt) and a [separate Etsy listing](https://www.etsy.com/listing/4376475806/huzzah-frog-with-sword-shirt-funny). Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-04 — Mitochondria

- **Execution record:** Selected at rank 4 with an official `Bestseller` badge and 127 item reviews.
- **Observed expression:** Large `Mitochondria`, scientific/cellular diagrams, and `Powering life Since Forever!` form a distressed academic/industrial label.
- **Contamination evidence:** The exact Mitochondria/Powering Life Since Forever expression appears in offers on both [SHEIN](https://us.shein.com/T-Shirt-Printed-With-%22Mitochondria%2C-Powering-Life-Since-Forever%21%22-p-449215019.html) and [Redbubble](https://www.redbubble.com/i/t-shirt/Mitochondria-Powering-Life-Since-Forever-Retro-Science-by-BrownHorse90s/179010893/lrcw). Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-05 — Gangster Cats

- **Execution record:** Selected at rank 5 with an official `Bestseller` badge, 102 item reviews, and visible item reviews through Sep 24, 2026.
- **Observed expression:** No slogan. A monochrome group of cats appears as an edgy human ensemble; one central cat smokes while the cats hold varied tough/judgmental expressions.
- **Recorded provenance:** The original analysis explicitly recorded unknown artwork provenance. The seller-side `Designed by`/AI-assistance disclosure describes a stated production role, but it does not establish the origin or license status of the underlying photographic/source assets.
- **Final Gate 0 decision:** `IP-QUARANTINE`. Frozen v0.2 requires unresolved origin to be quarantined, so the conservative final audit overrides the execution-time `ELIGIBLE` disposition for source use.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-06 — Rock Star Cat

- **Execution record:** Selected at rank 6 with an official `Bestseller` badge and 79 item reviews.
- **Observed expression:** A stylized wide-eyed cat plays an electric guitar inside a rough rectangular frame; no slogan appears.
- **Contamination evidence:** The exact Rock Star Cat/guitar title and expression recur on [Walmart](https://www.walmart.com/ip/20738101229). Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-07 — Fighting Leopards

- **Execution record:** Selected at rank 7 with an official `Bestseller` badge and 36 item reviews.
- **Observed expression:** Two red leopards occupy a dynamic opposing/entwined pose on an ivory shirt; no slogan appears.
- **Contamination evidence:** The exact Vintage Leopard Fighting title/expression recurs on [TeePublic](https://www.teepublic.com/t-shirt/97895802-vintage-leopard-fighting-graphic) and SHEIN. Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-08 — Poker Cats

- **Execution record:** Selected at rank 8 with an official `Bestseller` badge, 20 item reviews, and visible item reviews through Sep 16, 2026.
- **Observed expression:** No slogan. A group of cats surrounds a poker table with cards and chips; a central cat smokes. The image uses a dark, vintage photographic treatment.
- **Recorded provenance:** The photographic-source origin is unresolved. Its close cat-ensemble/smoking-center relationship to `TRACE-P001-ETSY-05` appears across different sellers, and the available evidence cannot distinguish independent creation from a shared template, copied family, or common source assets.
- **Final Gate 0 decision:** `IP-QUARANTINE`. The unresolved cross-seller/template/copy relationship and source-image origin fail conservative final clearance.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-09 — Everything Is Temporary

- **Execution record:** Selected at rank 9 with an official `Bestseller` badge and 14 item reviews.
- **Observed expression:** A front/back acid-wash streetwear graphic combines repeated `EVERYTHING`, vertical `TEMPORARY`, marbled abstraction, checker geometry, stars, and QR-like forms.
- **Contamination evidence:** The exact phrase, front/back format, title, and expression recur on [SHEIN](https://us.shein.com/Everything-Is-Temporary-Design-%2C-Acid-Wash-Tee%2C-Oversized-Unisex-Graphic-Shirt%2C-Front-And-Back-Print%2C-Vintage-Streetwear-Gift-p-568174589.html). Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-10 — I Never Question My Wife's Choices

- **Execution record:** Selected at rank 10 with an official `Bestseller` badge and 10 item reviews.
- **Observed expression:** Typography-only statement: `I never question my wife's choices, I'm one of them`.
- **Contamination evidence:** The exact phrase recurs across unrelated Etsy and independent-store offers, including [Soul & Peace](https://soulandpeace.com/products/never-question-wifes-choices-half-sleeve-t-shirt) and a [separate Etsy listing](https://www.etsy.com/listing/1273928368/i-never-question-my-wifes-choices). Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

### TRACE-P001-ETSY-11 — Boho Sun

- **Execution record:** Selected at rank 11 with an official `Bestseller` badge and 10 item reviews.
- **Observed expression:** A distressed orange sun disc sits inside fine white radiating lines on charcoal gray; no slogan appears.
- **Contamination evidence:** The Boho Sun composition and exact title recur across unrelated sellers and markets, including [SHEIN](https://us.shein.com/1pc-Boho-Sun-T-Shirt%2C-Retro-Celestial-Sky-Tee%2C-Vintage-Hippie-Festival-Top%2C-Groovy-Minimalist-Summer-Nature-Lover-Gift-Shirt-p-562846432.html). Origin and authorization are unresolved.
- **Final Gate 0 decision:** `IP-QUARANTINE`.
- **Downstream control:** Audit only—no SDC, mechanism, grammar, recipe, recurrence/corroboration, or transfer use. No backfill.

## Important unselected evidence

The badge-first rule excluded several title/thumbnail-eligible fixed designs with much larger item-specific review histories than low-count badged sources. These unselected records did not receive the final cross-market origin audit and must not be described as cleared sources:

| Listing | Badge | Item reviews | Latest visible review |
|---|---:|---:|---|
| Cat Guitarist (`671213378`) | No | 1.7k | Apr 24, 2026 |
| Jesus Riding Dinosaur (`560142098`) | No | 1k | Jul 14, 2026 |
| Funny Dad Jokes (`1012093892`) | No | 857 | Sep 8, 2026 |
| Possum / Live Weird Fake Your Death (`759163386`) | No | 518 | Jul 31, 2026 |
| Breweries Are Calling (`549555574`) | No | 395 | Jun 21, 2026 |
| Bookworm Embroidered (`1891921335`) | No | 279 | Sep 18, 2026 |

Conversely, the execution-time cutoff included a badged family with nine item reviews. This follows v0.2 exactly, but it is a material calibration result. The final audit changes source-use eligibility, not the historical cutoff or ranks.

## Exclusion examples

- **Product/custom contamination:** custom photo, custom text/logo, personalized bootleg, backside upgrade, and company-logo listings dominated `text t shirt` and several `Top reviews` surfaces.
- **Clear IP/public-fame exclusions:** Westlife, Descendants/Zombies/Camp Rock, Roblox/Sprunki, Dolly Parton, Radiohead, named sports/basketball identities, movie shirts, bands, musicians, celebrity puns, lyric-based `Hey Sista`, and direct anti-Trump/FDT identity goods.
- **Execution-stage quarantines:** Jimothy the viral Seattle raccoon; artistic cats based on famous painters; Yayoi Kusama-derived merchandise; `Every Child Matters`; Lake Ontario political-event satire; a red-balloon skeleton of unclear reference origin; art-history/public-domain-image provenance; and a Great Wave adaptation.
- **Selected-then-quarantined:** Eleven execution selections (`TRACE-P001-ETSY-01` through `-11`) failed strict final provenance clearance because exact or materially matching expressions recurred across unrelated sellers/markets or underlying source origin remained unresolved. They contribute no downstream evidence and were not backfilled. This is contamination control, not an infringement finding.
- **Family dedupe:** two Pasta Pups dachshund/spaghetti listings were treated as one repeated expression, not two mechanism confirmations.

Exact IDs, titles, rows, execution dispositions, and controlling final-audit dispositions are in the CSV.

## Etsy-specific methodology findings

1. **Freeze traversal order explicitly.** v0.2 freezes query order and two sorts but does not state whether traversal is query-major or sort-major. Because `earlier first occurrence` is a tiebreak, this can change selection. This run used query-major, `Most relevant` then `Top reviews`.
2. **Specify lazy-load recovery.** One surface initially exposed only 11 organic cards plus one ad. Waiting/scrolling caused the remaining cards to load. v0.3 should define a maximum wait/scroll procedure and an incomplete-surface rule.
3. **State whether `instant_download=false` is intentional.** Etsy appended it automatically in this signed-out US session. The pilot benefited because digital files were suppressed, but the protocol should freeze this filter rather than inherit browser/session state accidentally.
4. **Define recency operationally.** `Recency` might mean latest review date, number of reviews in a window, or review cadence. The current rule does not say which.
5. **Reconsider hard badge precedence.** Treating the official Bestseller badge as an absolute first tier produced a fully badged execution sample but discarded much deeper exact-design review histories. A v0.3 vector or minimum-strength rule should preserve the badge's recent-sales value without making nine reviews lexicographically superior to 1.7k item reviews in every case.
6. **Explicitly label search-card counts as shop-level.** `Top reviews` heavily promoted custom printers whose visible counts belonged to the shop, not the displayed design. The listing page was mandatory for item attribution.
7. **Clarify cause/public-figure eligibility.** Cause affiliation is currently a confounder, while public-personality dependence is an exclusion/quarantine. Political and movement slogans exposed a repeatable boundary problem.
8. **Require cross-market provenance closure before synthesis.** The strict final audit quarantined 11 of 12 execution selections because expression recurrence or underlying artwork/source origin remained unresolved. A design can lack a recognizable franchise and still fail contamination control. v0.3 should record provenance confidence separately from concept eligibility and demand evidence, run clone/origin checks before decoding, and require an explicit controlling final disposition before any SDC, recipe, grammar, recurrence, corroboration, or transfer use.

## Etsy-stratum recommendation

**Revise and retain TRACE.** The frozen procedure produced an auditable 12-family execution selection, and the strict final Gate 0 audit reduced it to one source cleared for downstream use. The audit prevented 11 clone/origin-conflicted families from contributing evidence, but that attrition shows cross-market provenance screening must occur before decoding. The run also exposed fixable operational ambiguities and one important selection distortion: absolute badge precedence. Do not rewrite the frozen ranks or backfill after the fact; carry the controls into the post-pilot v0.3 proposal.
