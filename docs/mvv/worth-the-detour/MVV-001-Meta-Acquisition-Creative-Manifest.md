---
title: MVV-001 Meta Acquisition Creative Manifest
brand: Worth the Detour
experiment_id: mvv-r012-001
owner: Creative Director
status: Working — representative-card verification pending
related_issue: 56
last_updated: 2026-09-03
---

# MVV-001 Meta Acquisition Creative Manifest

## Execution identity

| Field | Value |
|---|---|
| `creative_id` | `WTD-MVV001-CAR-01` |
| Concept | Ten ways to know the hunt |
| Format | Manually assembled, image-only 10-card carousel |
| Objective / destination | Traffic / Website |
| Performance goal | Maximize number of link clicks |
| Placements | Facebook Feed and Instagram Feed only |
| Primary text | `COPY-P01` |
| Optional description | `COPY-D01` |
| CTA | Learn More |
| Landing-page base | `https://worth-the-detour.com/` |
| Card ordering | Initial order below; predicted-best-performing-card ordering enabled if available |
| Attribution | Same carousel `creative_id` on every card; stable source-card and source-product identity per card; downstream landing-page `design_id` remains independent |

The Campaign Operator and Technical Reviewer own the exact URL-parameter encoding. Every final card URL must semantically carry `creative_id=WTD-MVV001-CAR-01`, its listed source card, and its listed source-product `design_id`. Do not use the source product to preselect or overwrite downstream product behavior.

## Card and asset matrix

Status `GATED` means the treatment and filenames are final, but bulk file export must wait for live verification of the representative `C01` pair.

| Order | Card | Source-product `design_id` | Territory | Headline | Facebook Feed 1:1 asset | Instagram Feed 4:5 asset | Status |
|---:|---|---|---|---|---|---|---|
| 1 | `C01` | `Type-Led-4` | Thrill of discovery / expressive type | For the Thrill of the Antique Find | `WTD-MVV001-CAR-01_C01_Type-Led-4_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C01_Type-Led-4_IG-Feed_4x5_1080x1350.jpg` | `PREVIEW-READY` |
| 2 | `C02` | `B2` | One More Booth / detour humor | The Five-Minute Antique Stop | `WTD-MVV001-CAR-01_C02_B2_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C02_B2_IG-Feed_4x5_1080x1350.jpg` | `GATED` |
| 3 | `C03` | `YIF-M` | Find logistics / insider humor | When the Antique Find Has to Fit | `WTD-MVV001-CAR-01_C03_YIF-M_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C03_YIF-M_IG-Feed_4x5_1080x1350.jpg` | `GATED` |
| 4 | `C04` | `Fashion-1D-F` | Direct treasure-hunter identity | Treasure Hunter, Recognized | `WTD-MVV001-CAR-01_C04_Fashion-1D-F_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C04_Fashion-1D-F_IG-Feed_4x5_1080x1350.jpg` | `GATED` |
| 5 | `C05` | `Type-Led-3` | Thrill of discovery / utility type | Antiques Are Worth the Detour | `WTD-MVV001-CAR-01_C05_Type-Led-3_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C05_Type-Led-3_IG-Feed_4x5_1080x1350.jpg` | `GATED` |
| 6 | `C06` | `C3B` | Discount/SOLD hunt ritual | Antique-Mall Hope, Then SOLD | `WTD-MVV001-CAR-01_C06_C3B_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C06_C3B_IG-Feed_4x5_1080x1350.jpg` | `GATED` |
| 7 | `C07` | `YIF-F` | Find logistics / softer expression | Yes, the Find Will Fit | `WTD-MVV001-CAR-01_C07_YIF-F_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C07_YIF-F_IG-Feed_4x5_1080x1350.jpg` | `GATED` |
| 8 | `C08` | `A1` | Hunter's Eye / antiques discernment | A Good Eye Knows | `WTD-MVV001-CAR-01_C08_A1_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C08_A1_IG-Feed_4x5_1080x1350.jpg` | `GATED` |
| 9 | `C09` | `C2` | Booth artifact / story of the find | Found in Booth 42 | `WTD-MVV001-CAR-01_C09_C2_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C09_C2_IG-Feed_4x5_1080x1350.jpg` | `GATED` |
| 10 | `C10` | `A3` | Hunter's Eye / MCM discernment | The Good Vintage Ones Don’t Shout | `WTD-MVV001-CAR-01_C10_A3_FB-Feed_1x1_1080.jpg` | `WTD-MVV001-CAR-01_C10_A3_IG-Feed_4x5_1080x1350.jpg` | `GATED` |

All final files belong under `docs/mvv/worth-the-detour/assets/meta/MVV-001/`.

## Representative asset verification

| File | Canvas | Format | Size | SHA-256 |
|---|---:|---|---:|---|
| `WTD-MVV001-CAR-01_C01_Type-Led-4_FB-Feed_1x1_1080.jpg` | 1080 × 1080 | JPEG | 309,551 bytes | `b13b3285659dd07fd6b9a434fa791d3ba01a789c57696a0a15a7ea4880b4c91e` |
| `WTD-MVV001-CAR-01_C01_Type-Led-4_IG-Feed_4x5_1080x1350.jpg` | 1080 × 1350 | JPEG | 397,594 bytes | `42435c5defaf3278bc25c33a401e8d03b121b423cc3aa8d9072c899cc1c3e7cc` |

The 4:5 asset is a compositionally faithful placement adaptation of the approved LP image. The 1:1 asset uses a vertical crop that preserves the garment, full print, category line, and supporting antique context. Neither modifies the locked artwork.

## Copy references

- `COPY-P01`: “The best finds rarely announce themselves. These are T-shirts for antique-mall detours, flea-market hunts, estate-sale mornings—and people who always check one more booth.”
- `COPY-D01`: “Worth the Detour — For people who see what others miss.”
- CTA: Learn More

## Complementary concept

No complementary non-carousel creative is approved for first-run production. The behavioral “five-minute antique stop” scene is held in reserve and would require a new persistent `creative_id`, separate manifest entries, Strategy Advisor approval, and the same two-ratio feed matrix.

## Gate state

Do not change the nine `GATED` cards to production-ready or export their files until the Campaign Operator records successful live verification of:

1. placement-specific media assignment;
2. crop/rendering behavior;
3. primary text, headline, description, and CTA rendering;
4. stable card-to-URL/source identity;
5. predicted-best-performing-card ordering behavior.

Any URL convention added after Technical Review must update this manifest without changing the established creative, card, or product identities.
