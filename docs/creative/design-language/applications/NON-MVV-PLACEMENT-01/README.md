# Five non-MVV designs — lowered placement

October 23, 2026 · Founder authorized checking all five and lowering artwork where needed before resuming samples. Placement-only derivatives completed; revised provider previews and physical samples remain pending. Original approved masters and frozen assessments are unchanged.

## Decision and review

All five retain the older 1.5-inch top anchor. After inspecting the approved shirt views and controlled before/after comparisons, the Creative Director selects a **0.5-inch downward translation**, to top 2.0 inches from the print-canvas origin, for each. This follows the approved MVV correction without changing footprint, artwork, internal spacing, color or garment.

These are print-area coordinates, **not measured collar distances**. Reused local geometry is provisional (17.8 px/in, center x303, print origin y97 on the 602px blank; photographed size unknown). Estimated image-space collar clearance increases from about 54 to 63 pixels. Actual collar clearance and fulfillment scaling require provider/sample verification.

| Design | Color | Width × height, inches | New bottom, inches | Comparison |
|---|---|---|---|---|
| T-E-A / playful delivery | Pepper | 8 × 7.8358 | 9.8358 | [Before/after](assets/T-E-A-comparison.jpg) |
| T-E-B / type-led ornate sofa | Pepper | 8.5 × 6.3447 | 8.3447 | [Before/after](assets/T-E-B-comparison.jpg) |
| N-A / $2 and SALE bowl | Ivory | 8 × 9.9783 | 11.9783 | [Before/after](assets/N-A-comparison.jpg) |
| N-D-A / Grandma's bowl, heritage | Ivory | 8.75 × 8.3794 | 10.3794 | [Before/after](assets/N-D-A-comparison.jpg) |
| N-D-B / Grandma's bowl, framed | Pepper | 8.25 × 10.401 | 12.401 | [Before/after](assets/N-D-B-comparison.jpg) |

## Pre-feedback assessment — preserved October 23

The original placements are not severely collar-crowded in these local views, but are slightly higher than the Founder's subsequently established preference. The modest shift improves breathing room without requiring a new size comparison.

- **T-E-A:** clustered playful lettering and cabinet/car remain a single compact chest composition; the lowered headline is less neck-adjacent. No change to comic timing or internal spacing.
- **T-E-B:** the top-heavy serif headline benefits most clearly from the shift. The small ornate sofa stays subordinate and connected; no reason to alter the approved typography or scale.
- **N-A:** the rectangular top border and price line gain separation from the collar. The tall label still ends comfortably above the lower torso in the provisional view.
- **N-D-A:** the arch gains breathing room, while the bowl and payoff retain their approved relationship. The pre-existing interpretation concern about people inside the bowl is not reopened.
- **N-D-B:** the top cartouche is less collar-adjacent. The longest composition still has adequate lower-shirt space; a larger downward shift would risk unnecessary torso drift.

Tradeoff: these are subtle changes; all compositions sit slightly lower. Inspected all five saved before/after boards. The exact translation preserves artwork-scale relationships and native detail; it cannot improve existing resolution or alpha quality.

## Files and verification

[Reproducible build script](build_review.py) · [Specifications, hashes and current upload paths](layout-specs.json).

Each 1800 × 2400, 150-PPI transparent canvas translates the original RGBA pixels down exactly 75 pixels. Automated checks verify saved pixels match the original at that translation, no clipping occurs, and canvas size is unchanged. No artwork generation, repainting, resampling of print pixels, new text or branding was used. Preview resizing is for display only. Re-run with Pillow from the repository.

Original T-E-A is approximately 152 native PPI, T-E-B 165, N-A 127, N-D-A 132 and N-D-B 113 at approved widths. Prior native-detail/transparency work remains open, particularly for N-A and both N-D designs. These exports are placement candidates, not newly certified production masters. Recheck the selected third sample in Printful and resolve its relevant print-file issues before purchase.

## Sample handoff

The latest Founder selection from the ten MVV designs is **A3 and C3B only**. Type-Led-3 and Type-Led-4 are excluded. Founder intends to add a third design after this five-design review; its identity is not yet chosen. The prior live checkout contained different items and must be reconciled before any purchase. No checkout, purchase, publication or merge is performed by this placement revision.

Next: choose the third sample, use this revision's upload path for its placement, complete its production preflight/provider preview, and obtain the current checkout quote. Do not assume the time-limited welcome discount is still active.

## Subsequent Founder feedback — N-D-A internal spacing

Founder approved the lowered placements but identified unbalanced illustration-to-copy spacing in N-D-A. The earlier assessment remains above as recorded. [N-D-A spacing revision](NDA-spacing-02/README.md) now supplies the current candidate and replaces only its lowered-only upload path; the other four remain unchanged.
