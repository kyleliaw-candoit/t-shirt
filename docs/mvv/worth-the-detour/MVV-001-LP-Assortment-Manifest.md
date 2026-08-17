---
title: MVV-001 Landing-Page Assortment Manifest
brand: Worth the Detour
experiment_id: mvv-r012-001
owner: Creative Director
status: Proposed
last_updated: 2026-08-17
---

# MVV-001 — Landing-Page Assortment Manifest

## Purpose

Record the founder-approved Worth the Detour MVV #1 landing-page product assortment using stable product identifiers, exact locked creative source assets, and the primary R012 recognition mechanism each product contributes.

This is a **product-validation assortment**, not the future Meta acquisition-creative set. A shirt does not need to independently decode the entire R012 category when viewed on the landing page; category meaning is carried by the page framing and the assortment as a whole.

The assortment currently contains **11 products**. The current product order is **tentative and not locked**.

## Identifier rule

Use existing canonical Creative Director identifiers directly as `design_id` values wherever a locked product already has one. Do not create a parallel `D001` / `D002` style remapping.

One exception is required for the founder-approved decision to treat the two shirts bundled in the locked Fashion-1D source presentation as two separate landing-page products. The existing family identifier is preserved and extended with child IDs:

- `Fashion-1D-A`
- `Fashion-1D-B`

These are not replacement IDs for another canonical identifier; they distinguish two LP products that were previously bundled under one `Fashion-1D` lock record.

## Current assortment

| Tentative order | `design_id` | Product / working name | Exact locked source asset | Primary R012 recognition mechanism |
|---:|---|---|---|---|
| 1 | `B2` | No, Really. Five Minutes. | `docs/creative/assets/R012/R012-B2-LOCKED.png` | Hunt behavior / insider humor — the reflexive antique-stop detour and knowingly unrealistic “five minutes” promise. |
| 2 | `A1` | Good Antiques Don’t Shout | `docs/creative/assets/R012/R012-A1-LOCKED.png` | Hunter’s eye / antiques discernment — recognizing quiet quality that does not announce itself. |
| 3 | `A3` | The Good Ones Don’t Shout | `docs/creative/assets/R012/R012-A3-LOCKED.png` | Hunter’s eye / vintage-MCM discernment — explicitly broadens the assortment into vintage furniture and understated design quality. |
| 4 | `YIF-M` | Yeah, it’ll Fit — restrained execution | `docs/creative/assets/R012/R012-YIF-M-LOCKED.png` | Hunt behavior / insider humor — treasure-hunter optimism about fitting an absurdly oversized find into the car. |
| 5 | `YIF-F` | Yeah, it’ll Fit — softer / female-leaning execution | `docs/creative/assets/R012/R012-YIF-F-LOCKED.png` | Hunt behavior / insider humor — same authentic logistics joke expressed through a different gender/style treatment. |
| 6 | `C2` | Found Not New — Booth 42 | `docs/creative/assets/R012/R012-C2-LOCKED.png` | Story of the find / antique-mall artifact — found-object value plus specific booth-hunting context. |
| 7 | `C3B` | The Thrill Curve — Discount Dots + SOLD | `docs/creative/assets/R012/R012-C3B-LOCKED.png` | Hunt emotion / insider ritual — excitement from discount progression followed by the heartbreak of `SOLD`. |
| 8 | `Fashion-1D-A` | Treasure Hunter — Retro Script, Product A | `docs/creative/assets/R012/R012-Fashion-1D-LOCKED-SOURCE.png` | Direct treasure-hunter identity / fashion-first recognition. |
| 9 | `Fashion-1D-B` | Treasure Hunter — Retro Script, Product B | `docs/creative/assets/R012/R012-Fashion-1D-LOCKED-SOURCE.png` | Direct treasure-hunter identity / fashion-first recognition. |
| 10 | `Type-Led-3` | The Thrill of the Find — Utility Compressed | `docs/creative/assets/R012/R012-Type-Led-3-LOCKED-SOURCE.png` | Thrill of discovery / type-led identity, with explicit `ANTIQUES ARE WORTH THE DETOUR` category support. |
| 11 | `Type-Led-4` | Thrill of the Find — Free Handwritten | `docs/creative/assets/R012/R012-Type-Led-4-LOCKED-SOURCE.png` | Thrill of discovery / expressive type-led identity, with explicit `ANTIQUES ARE WORTH THE DETOUR` category support. |

## Fashion-1D source-board handling

The current canonical lock record for Fashion-1D points to one byte-verified source PNG:

`docs/creative/assets/R012/R012-Fashion-1D-LOCKED-SOURCE.png`

That source remains authoritative for both `Fashion-1D-A` and `Fashion-1D-B` at this stage. Do **not** alter or regenerate the locked board merely to create separate product identities.

During the next Creative Director subtask — standardized primary LP product images — create or approve separate product presentation assets for `Fashion-1D-A` and `Fashion-1D-B`. Those LP presentation assets may crop/isolate the two approved shirts, but they must preserve the exact approved shirt executions rather than redesigning them.

## Explicit MVV #1 holdouts

The following locked products are intentionally not in the first landing-page assortment:

- `B1` — overlaps substantially with B2; B2 is the selected detour-sign product for MVV #1.
- `C1` — C2 carries the same core idea with stronger antique-mall specificity.
- `Fashion-1C` — omitted in favor of the two Fashion-1D products.
- `Fashion-7A1` and `Fashion-7A2` — aesthetically useful but comparatively weak on brand message; lower priority before the brand itself passes MVV.

These are **holdouts, not rejected designs**.

## Presentation note

A3 should not be judged as a standalone category-decoding advertisement. On the landing page it appears beside multiple products and page-level cues that establish the antiques / vintage treasure-hunting world. Its specific job is to make vintage and especially vintage / mid-century-modern treasure hunters visibly part of the Worth the Detour audience.

## Handoff status

This manifest completes the Creative Director subtask:

> Record each included `design_id`, exact locked source asset, and primary R012 recognition mechanism.

Next Creative Director subtask:

> Produce or approve one standardized primary LP product image for each included design.
