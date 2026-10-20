# Cross-source duplicate and template reconciliation

October 20, 2026 · Scope: the 220 retained source-level records merged in PR136.

**Result: retain 220 reference records.** All 220 retained image files have different SHA-256 hashes. Visual comparison found no confirmed cross-source instance of the same complete artwork that should be collapsed in this pass. This does **not** certify 220 independently created artworks: different crops, mockups or undetected reused elements can evade this review, and creator provenance is incomplete on some marketplace records.

No source record was deleted or rewritten. Collection-stage exclusions/recolors remain in the source batch logs. This audit adds a global comparison layer without changing historical collection claims.

## Distinctions preserved

| References | What repeats | Decision |
|---|---|---|
| RB-005 / SNORG-010 | Attempted-murder crow-count premise | Different artwork and layout: open two-bird vignette versus a sequence of framed bird panels. Retain both; do not call two distinct concepts. |
| RB-022 / ZZ-007 | Left-unsupervised wording | Different typography, alignment and scale. Retain as visual treatments; not independent evidence that the wording or family causes sales. |
| RB-007 / RB-018 / RB-022 | Compact, left-aligned bold white copy on dark blanks | Treat as a repeated visual template cohort when judging support. Three captions do not equal three independent discoveries. |
| ZZ-015 / ZZ-022 | Hubby/wifey flowing-script treatment | Copy/garment variants of a closely related signature treatment; retain source records, discount independent-support claims. |
| ZZ-034 / ZZ-044 | California/Hawaii script on similarly styled white shirts | Near-template pair, not a different design-language discovery. Retain both, count the relationship once conceptually. |
| ZZ-021 / ZZ-028 | Good/bad witch decorative lettering | Closely related type composition with changed wording and reversed light/dark treatment. Retain as variants, not independent recipe validation. |
| LIG-009 / LIG-012 | Women-have-hobbies subject and wording | Framed monochrome versus open colored treatment; retain as a useful visual boundary comparison. |
| ETSY-032 / ETSY-047 | Armored rider on a large cat | Different scene rendering, lettering and framing; retain. Similar subject does not by itself establish duplicate artwork. |
| HISTOREE-003 / SNORG-019 | Pompeii / lava humor | Different visual systems and wording: retro sunset/event stack versus illustrated event treatment. Retain. |

Abbreviations above expand to `DLS-` record IDs, linked in the [review log](Review-Log.md). These are review examples, not an exhaustive list of shared phrases or supplier relationships.

## Counting rule for further work

Keep three separate questions: how many source records were collected; whether complete artwork is repeated; and whether multiple records provide independent evidence for a visual relationship. A repeated seller template may be useful to show a flexible dimension, but cannot be treated as multiple independent confirmations. Do not calculate marketplace prevalence or confidence intervals from this purposive sample.

If a later comparison confirms the same complete artwork, assign a shared artwork-group ID and retain both provenance records. Mark one as the visual representative; do not erase the other source or retrospectively claim that the original quota was globally unique.
