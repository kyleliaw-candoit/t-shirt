---
title: TRACE-PILOT-002 — DTC Panel Lock
owner: Creative Director
status: Locked — ranked-product inspection not begun
pilot_id: TRACE-PILOT-002
methodology_version: TRACE v0.3
methodology_frozen_commit: 0b74489e083d58d8037129247399d3cece866de6
preregistration_commit: f5f3291fc3de64673f8e66ed85e139f2ec9df535
locked_at: 2026-09-25T18:09:29Z
observation_date: 2026-09-25
---

# TRACE-PILOT-002 — DTC Panel Lock

## Lock attestation

This panel was locked before any TRACE-PILOT-002 DTC ranked-product inspection.

Only current public assortment, category scope, store positioning, and non-ranked sort controls were inspected. Collection pages were deliberately loaded in `title-ascending` order when a sort parameter was used. No `sort_by=best-selling` URL, merchant bestseller-ranked collection, or ranked-product result was opened or inspected while preparing this lock. Search-result snippets and historical TRACE-PILOT-001 records were not used to select or prequalify an individual product.

The 12 stores below are frozen in order. A store that later fails broad-scope, active native-sort, bounded-capture, assortment, or eligible-family requirements leaves an empty slot. It will not be replaced, and no other store may contribute a second family.

## Frozen panel

| Order | Store ID | Store | Store URL | Current eligibility basis observed before rank inspection | Intended broad collection | Expected native-sort verification at ranked capture |
|---:|---|---|---|---|---|---|
| 1 | `P002-DTC-S01` | Boredwalk | [boredwalk.com](https://www.boredwalk.com/) | Independent, T-shirt-led original humor and illustration assortment; the current men's tee collection is broad and the store states its items are designed and printed in its studio. It is not principally franchise, sports, celebrity, or logo merchandise. | [Men's T-shirts](https://www.boredwalk.com/collections/mens-tshirts) | Request the same broad collection with `sort_by=best-selling`; require returned UI/HTML to show **Best selling** active before capturing ranks 1–24. |
| 2 | `P002-DTC-S02` | Wicked Clothes | [wickedclothes.com](https://www.wickedclothes.com/) | Independent-artist graphic-shirt store with a large current shirts collection spanning original humor, animals, gothic, and illustrated themes; not principally third-party franchise, sports, celebrity, or logo merchandise. | [Shirts](https://www.wickedclothes.com/collections/t-shirts) | Current non-ranked collection exposed the native `best-selling` option. At capture, require the explicit request and rendered selected state before ranks 1–24. |
| 3 | `P002-DTC-S03` | INTO THE AM | [intotheam.com](https://intotheam.com/) | T-shirt-led current assortment of original, hand-drawn artist graphics; the broad men's graphic-tee collection contains a substantial active catalog and is not principally franchise, sports, celebrity, or logo merchandise. | [Men's graphic T-shirts](https://intotheam.com/collections/mens-graphic-t-shirts) | Current Shopify collection exposed native catalog sorting including `best-selling`. At capture, require `sort_by=best-selling` plus a returned interface/HTML active-state signal; otherwise `SORT-UNVERIFIED`. |
| 4 | `P002-DTC-S04` | Solid Threads | [solidthreads.com](https://solidthreads.com/) | Independent graphic-tee-led brand with a broad current men's collection of handcrafted or art-directed vintage-style designs; not principally licensed-franchise, sports, celebrity, or logo merchandise. | [Men's T-shirts](https://solidthreads.com/collections/mens-t-shirts) | Current non-ranked collection exposed the native `best-selling` option. Require the explicit request and rendered selected state before capture. |
| 5 | `P002-DTC-S05` | Crazy Dog T-Shirts | [crazydogtshirts.com](https://www.crazydogtshirts.com/) | Large graphic-T-shirt-led store with a broad current humor/saying collection. A separate licensed collection exists, but the intended collection is not principally licensed merchandise; every encountered ranked product still receives strict Gate 0 screening. | [Crazy Shirts](https://www.crazydogtshirts.com/collections/crazy-shirts) | Current non-ranked collection exposed the native `best-selling` option. Require the explicit request and rendered selected state before ranks 1–24. |
| 6 | `P002-DTC-S06` | AukCliff | [aukcliff.com](https://aukcliff.com/) | Independent outdoor graphic-apparel store with a large current T-shirt catalog organized around hiking, wildlife, coast, and adventure designs; not principally franchise, sports, celebrity, or third-party logo merchandise. | [Outdoor T-shirts](https://aukcliff.com/collections/explore-the-great-outdoors-with-t-shirts) | Current non-ranked collection exposed the native `best-selling` option. Require explicit request plus selected state before capture. |
| 7 | `P002-DTC-S07` | SeaMonkey Apparel | [seamonkeyapparel.com](https://www.seamonkeyapparel.com/) | Independent coastal graphic-apparel store with a current broad tee collection and original coastal/lifestyle positioning; not principally franchise, sports, celebrity, or third-party logo merchandise. | [Tee's](https://www.seamonkeyapparel.com/collections/staple-tees) | Current non-ranked page exposed a **Best selling** sort control for this collection. Require the explicit request and returned active state before capture. |
| 8 | `P002-DTC-S08` | RAYGUN | [raygunsite.com](https://www.raygunsite.com/) | Independent, T-shirt-led current assortment centered on original political, regional, community, and humor statements rather than licensed franchise merchandise. Named-person or organization-dependent products remain automatic Gate 0 exclusions. | [T-Shirts](https://www.raygunsite.com/collections/t-shirts) | Current non-ranked collection exposed the native `best-selling` option. Require explicit request plus selected state before capture. |
| 9 | `P002-DTC-S09` | Pyknic | [pyknic.com](https://pyknic.com/) | Independent food-themed graphic-apparel label with a substantial current men's tee collection of original food illustrations and puns; not principally franchise, sports, celebrity, or third-party logo merchandise. | [Men's tees](https://pyknic.com/collections/mens-tees) | Current non-ranked page exposed a native **Best selling** radio value (`best-selling`) while **Alphabetically, A-Z** was checked. At capture, require the best-selling value checked/active. |
| 10 | `P002-DTC-S10` | Blackbird Supply Co. | [blackbirdsupply.com](https://www.blackbirdsupply.com/) | Independent artist-led graphic-apparel store with a broad current men's/women's assortment centered on nature, astronomy, travel, and illustrative themes; not principally franchise, sports, celebrity, or logo merchandise. | [Men's and women's apparel](https://www.blackbirdsupply.com/collections/mens-womens-apparel) | Current non-ranked collection exposed the native `best-selling` option. Require explicit request plus rendered selected state before capture. |
| 11 | `P002-DTC-S11` | South Coast Outdoors Company | [southcoastoutdoorscompany.com](https://southcoastoutdoorscompany.com/) | Independent T-shirt-led current collection mixing fishing, coastal wildlife, lifestyle, southern-heritage, and some house-logo graphics. It is not principally third-party franchise, sports, or celebrity merchandise; house-brand-dependent products remain individually `BRAND-EXCLUDED`. | [All T-Shirts](https://southcoastoutdoorscompany.com/collections/all-t-shirts) | Current non-ranked page exposed the native `best-selling` option while **Alphabetically, A-Z** was selected. Require the explicit best-selling request and active state before capture. |
| 12 | `P002-DTC-S12` | Sloth Hiking Club | [slothhikingclub.com](https://slothhikingclub.com/) | Independent, T-shirt-led current assortment centered on nature art and trail humor, with a large broad tee catalog; not principally third-party franchise, sports, celebrity, or logo merchandise. House-brand designs remain subject to individual brand-dependency review. | [Shop all tees](https://slothhikingclub.com/collections/all) | Current non-ranked page exposed a native **Best selling** sort value. Require `sort_by=best-selling` and the returned control marked active/checked before capture. |

## Panel-level interpretation

- Panel membership establishes only store and collection eligibility. It does not establish that any particular product is eligible, original, attributable, provenance-cleared, or sales-corroborated.
- Franchise, character, sports, celebrity, organization, quotation, disputed-artwork, unresolved recurring-expression, and house-brand-dependent products remain excluded or quarantined under Gate 0.
- The intended ranked capture is limited to raw product ranks 1–24 in each locked broad collection, unless the complete collection is demonstrably shorter.
- A merchant-curated `Bestsellers` collection does not substitute for the required native sort verification.
- The expected verification in the table is not a claim that ranked order has already been viewed. The active `Best selling` state must be demonstrated anew when that store's frozen turn is executed.

## Candidates considered but not locked

| Candidate | Pre-rank decision |
|---|---|
| SnorgTees | Not locked: the current broad collection was accessible, but the rendered collection interface did not expose a sufficiently clear sort-state control for the later three-part native-sort proof. |
| 6DollarShirts | Not locked: the broad collection was accessible, but the rendered collection interface did not expose a sufficiently clear sort-state control for the later three-part native-sort proof. |
| Chummy Tees | Not locked: the current broad collection did not provide a sufficiently clear, verifiable native sort state during non-ranked inspection. |
| Animal Hearted | Not locked: current navigation repeatedly entered a storefront account callback before stabilizing, making later deterministic live capture uncertain. |
| The Home T | Not locked: the current broad apparel collection did not expose a sufficiently clear, verifiable native sort state during non-ranked inspection. |
| OpenTrail | Not reconsidered: TRACE-PILOT-001 ended with inaccessible broad native-ranked capture, and current eligibility was not independently restored before this lock. |
| Two-Cross | Not reconsidered: TRACE-PILOT-001 ended with no qualifying current tee pool, and current eligibility was not independently restored before this lock. |

## Lock closeout

- Locked at: `2026-09-25T18:09:29Z`
- Locked store count: `12`
- Ranked DTC collection URLs opened before lock: `0`
- DTC product pages opened before lock: `0`
- Individual DTC designs selected before lock: `0`
- Next authorized DTC action: wait until the preregistered Amazon and Etsy frame work is complete, then process `P002-DTC-S01` through `P002-DTC-S12` in this frozen order.
