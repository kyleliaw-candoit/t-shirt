---
title: MVV-001 Landing-Page Assortment Manifest
brand: Worth the Detour
experiment_id: mvv-r012-001
owner: Creative Director
status: Complete
last_updated: 2026-08-18
---

# MVV-001 — Landing-Page Assortment Manifest

## Purpose

Record the founder-approved Worth the Detour MVV #1 landing-page product assortment using stable product identifiers, exact locked creative source assets, and the primary R012 recognition mechanism each product contributes.

This is a **product-validation assortment**, not the future Meta acquisition-creative set. A shirt does not need to independently decode the entire R012 category when viewed on the landing page; category meaning is carried by the page framing and the assortment as a whole.

The executable MVV #1 landing-page assortment currently contains **10 products**. The implemented product order is the **accepted MVV #1 baseline** and should remain unchanged for Issue #56 unless a material regression or genuine blocker is discovered.

## Identifier rule

Use existing canonical Creative Director identifiers directly as `design_id` values wherever a locked product already has one. Do not create a parallel `D001` / `D002` style remapping.

Fashion-1D consists of two separate founder-approved products and therefore uses two explicit child identifiers:

- `Fashion-1D-GN` — gender-neutral execution
- `Fashion-1D-F` — female-leaning execution

These IDs replace the temporary manifest-only `Fashion-1D-A` / `Fashion-1D-B` placeholders.

## Current executable assortment

| Tentative order | `design_id` | Product / working name | Canonical locked source asset | Primary R012 recognition mechanism |
|---:|---|---|---|---|
| 1 | `B2` | No, Really. Five Minutes. | `docs/creative/assets/R012/R012-B2-LOCKED.png` | Hunt behavior / insider humor — the reflexive antique-stop detour and knowingly unrealistic “five minutes” promise. |
| 2 | `A1` | Good Antiques Don’t Shout | `docs/creative/assets/R012/R012-A1-LOCKED.png` | Hunter’s eye / antiques discernment — recognizing quiet quality that does not announce itself. |
| 3 | `A3` | The Good Ones Don’t Shout | `docs/creative/assets/R012/R012-A3-LOCKED.png` | Hunter’s eye / vintage-MCM discernment — explicitly broadens the assortment into vintage furniture and understated design quality. |
| 4 | `YIF-M` | Yeah, it’ll Fit — restrained execution | `docs/creative/assets/R012/R012-YIF-M-LOCKED.png` | Hunt behavior / insider humor — treasure-hunter optimism about fitting an absurdly oversized find into the car. |
| 5 | `YIF-F` | Yeah, it’ll Fit — softer / female-leaning execution | `docs/creative/assets/R012/R012-YIF-F-LOCKED.png` | Hunt behavior / insider humor — same authentic logistics joke expressed through a different gender/style treatment. |
| 6 | `C2` | Found Not New — Booth 42 | `docs/creative/assets/R012/R012-C2-LOCKED.png` | Story of the find / antique-mall artifact — found-object value plus specific booth-hunting context. |
| 7 | `C3B` | The Thrill Curve — Discount Dots + SOLD | `docs/creative/assets/R012/R012-C3B-LOCKED.png` | Hunt emotion / insider ritual — excitement from discount progression followed by the heartbreak of `SOLD`. |
| 8 | `Fashion-1D-F` | Treasure Hunter — Retro Script, Female-Leaning | `docs/creative/assets/R012/R012-Fashion-1D-F-LOCKED-SOURCE.png` | Direct treasure-hunter identity / fashion-first recognition through explicit `Treasure Hunter` language. |
| 9 | `Type-Led-3` | The Thrill of the Find — Utility Compressed | `docs/creative/assets/R012/R012-Type-Led-3-LOCKED-SOURCE.png` | Thrill of discovery / type-led identity, with explicit `ANTIQUES ARE WORTH THE DETOUR` category support. |
| 10 | `Type-Led-4` | Thrill of the Find — Free Handwritten | `docs/creative/assets/R012/R012-Type-Led-4-LOCKED-SOURCE.png` | Thrill of discovery / expressive type-led identity, with explicit `ANTIQUES ARE WORTH THE DETOUR` category support. |

## MVV #1 execution exclusion — `Fashion-1D-GN`

`Fashion-1D-GN` was originally included in the 11-product landing-page assortment, but it is **excluded from the executable MVV #1 landing page** because the current image-generation workflow could not produce a customer-facing LP product image that reliably passed the canonical LP Product Image Standard.

Multiple attempts encountered design-specific generation problems, including difficulty preserving the required customer-facing presentation and, in earlier attempts, reliable artwork / garment-material fidelity. The final automated attempt repeatedly produced review/specification-board content instead of a clean LP product image. Continuing to iterate would create disproportionate delay relative to the learning value of one additional product in this MVV.

This is an **execution/tooling exclusion, not a product or creative rejection**:

- the locked `Fashion-1D-GN` T-shirt design remains founder-approved and canonically archived;
- no negative inference about customer demand, product quality, or the underlying binocular concept should be drawn from its exclusion;
- the design may be revisited in a later test when a reliable LP merchandising image can be produced by a different workflow or tool;
- all AI roles should treat the MVV #1 landing-page assortment as **10 executable products**, not 11.

The locked source remains:

`docs/creative/assets/R012/R012-Fashion-1D-GN-LOCKED-SOURCE.png`

Decision recorded: **2026-08-18**.

## Fashion-1D archive state

`Fashion-1D-GN` and `Fashion-1D-F` are founder-approved, separately archived, byte-verified, and `LOCKED`. The MVV #1 execution exclusion above changes only whether `Fashion-1D-GN` appears on the current landing page; it does not change the locked design's archive status.

### Fashion-1D-GN

Canonical asset:

`docs/creative/assets/R012/R012-Fashion-1D-GN-LOCKED-SOURCE.png`

Verified SHA-256:

`ca31b1176694dd5407771b0cf544c15639736580a39b79de133f7413c42f376f`

Verified Git blob SHA-1:

`c529619cdc2469b0a68adc962e630fffa7556e51`

### Fashion-1D-F

Canonical asset:

`docs/creative/assets/R012/R012-Fashion-1D-F-LOCKED-SOURCE.png`

Verified SHA-256:

`0a9b9f2bdf977917328f66bb319095b0f7f212414af7f8b72fe8324b6a056024`

Verified Git blob SHA-1:

`90d0f24822a27e31003b7c70469ae4a647636865`

The historical Fashion-1D comparison/source board remains archived at:

`docs/creative/assets/R012/R012-Fashion-1D-LOCKED-SOURCE.png`

Do not overwrite or delete that board.

## Explicit MVV #1 holdouts

The following locked products are intentionally not in the first landing-page assortment:

- `B1` — overlaps substantially with B2; B2 is the selected detour-sign product for MVV #1.
- `C1` — C2 carries the same core idea with stronger antique-mall specificity.
- `Fashion-1C` — omitted in favor of the Fashion-1D direction.
- `Fashion-7A1` and `Fashion-7A2` — aesthetically useful but comparatively weak on brand message; lower priority before the brand itself passes MVV.

These are **holdouts, not rejected designs**. `Fashion-1D-GN` is documented separately above because its omission is an execution/tooling exception rather than an assortment-selection holdout.

## Presentation note

A3 should not be judged as a standalone category-decoding advertisement. On the landing page it appears beside multiple products and page-level cues that establish the antiques / vintage treasure-hunting world. Its specific job is to make vintage and especially vintage / mid-century-modern treasure hunters visibly part of the Worth the Detour audience.

## Handoff status

The Creative Director product-image subtask is complete for the executable MVV #1 assortment:

> Produce or approve one standardized primary LP product image for each included design.

Ten products have approved LP primary images. `Fashion-1D-GN` is explicitly excluded from MVV #1 under the execution exception above so it does not remain an unresolved dependency or blocker.

The detail / inspection asset subtask is complete. Issue #55 is closed, and this manifest is ready to serve as a canonical input to Issue #56 acquisition-candidate selection.
