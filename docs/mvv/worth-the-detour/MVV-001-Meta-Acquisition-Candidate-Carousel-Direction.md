---
title: MVV-001 Meta Acquisition Candidate and Carousel Direction
brand: Worth the Detour
experiment_id: mvv-r012-001
owner: Creative Director
status: Proposed — Review Required
related_issue: 56
based_on_main: 2c5449f7fbee36d517ded32100b7fab00cab3dba
last_updated: 2026-09-03
---

# MVV-001 Meta Acquisition Candidate and Carousel Direction

## Decision

Advance one automatically reorderable, all-product Meta carousel containing the 10 executable MVV #1 landing-page products.

**Unifying idea: _Ten ways to know the hunt._**

The carousel should feel like a curated rack encountered inside the antiques/vintage-discovery world: one consistent apparel presentation, with each card revealing a different recognition signal—detour behavior, a trained eye, find logistics, booth culture, discount ritual, explicit treasure-hunter identity, or the thrill of discovery.

This is one coherent acquisition execution, not 10 independent product ads and not a product-winner ranking. It should receive one persistent carousel-level `creative_id`. Each card must also retain a stable source-card identity and source-product `design_id`. Downstream landing-page behavior continues to use the independently selected or viewed product's `design_id`.

```text
carousel creative_id
  → source card + source-product design_id
  → landing visit
  → downstream design_id exposure / engagement / intent
  → lead
```

A click from one product followed by intent for another is valid evidence. High card CTR is not automatically product preference; limited card delivery is uncertainty, not rejection.

## Shared framing

The complete execution should communicate, in combination:

- **Apparel:** make the garment unmistakable on every card; do not present isolated artwork as if it were a poster.
- **R012 world:** use restrained antique-mall / flea-market / estate-sale context plus specific card language. Avoid generic thrift-fashion, farmhouse décor, reseller, appraisal, travel, or nostalgia framing.
- **Brand meaning:** use shared primary text to connect varied products to **Worth the Detour** and “For people who see what others miss.”
- **Recognition:** let each card deliver one quick customer truth rather than forcing every print to explain the whole category.

Recommended shared primary-text direction for later copy development:

> You know the promising booth, the quiet good piece, and the “five-minute” stop that never is. Worth the Detour makes T-shirts for antique and vintage treasure hunters—for people who see what others miss.

This is framing direction, not final deployment copy. Final length, truncation behavior, headline convention, description, and CTA depend on objective and live placement previews.

Card headlines should carry short product/recognition cues when the print alone cannot decode rapidly. Do not place extra explanatory copy over locked artwork. Preserve a consistent visual system: warm ivory garment, front-facing inspection, softly defocused discovery context, comparable garment scale, and restrained brand sign-off outside the print area if the approved format permits it.

## Ten-card evaluation

Scroll-stop ratings are directional creative judgments for acquisition planning, not product-quality judgments.

| Initial order | `design_id` / product | Acquisition territory and recognition mechanism | Mobile scroll-stop | Category decoding / feed limitation | Recommended treatment, crop, context | Wrong-attention risk / card-specific production requirement |
|---:|---|---|---|---|---|---|
| 1 | `Type-Led-4` — The Thrill of the Find — Handwritten | Thrill of discovery; expressive fashion/type signal | **High** — large, gestural lettering | Main phrase reads fast; small “ANTIQUES ARE WORTH THE DETOUR” may disappear | Use approved LP product image as source presentation; tight garment crop with the full chest unit large; retain a slim band of antique-shop context | “Find” could read as generic shopping/inspiration. Pair with an antiques-explicit headline or shared framing; verify the angled script remains fully inside safe crop. |
| 2 | `B2` — No, Really. Five Minutes. | One More Booth / detour behavior; insider recognition of an implausibly short stop | **High–medium** — sign form and joke are quick | Without context, “five minutes” can be generic relationship humor | Tight garment crop while preserving the complete sign; visible but soft antique-mall environment; headline should name the antique-stop behavior | Generic humor clicks. Keep the sign/artwork unobstructed and make antiques context legible without adding props that compete. |
| 3 | `YIF-M` — Yeah, It’ll Fit — Classic | Find logistics; tiny car plus oversized chair joke | **High–medium** — comic proportion reads quickly | Small restrained print may lose the car/chair relationship | Crop closer than LP while keeping the entire illustration and phrase; minimal contextual support; garment still evident | Could attract moving/furniture humor rather than hunters. Headline should anchor “the antique find”; do not enlarge or alter locked print composition. |
| 4 | `Fashion-1D-F` — Treasure Hunter | Direct identity declaration; fashion-first retro script | **High–medium** — explicit audience label | “Treasure hunter” can imply gaming, beach detecting, or children without antiques context | Preserve female-leaning approved styling; large garment/chest read; antique-shop context and an antiques-explicit headline are required | Broad identity curiosity. Preserve the approved garment treatment and prevent decorative context from turning into generic vintage fashion. |
| 5 | `Type-Led-3` — The Thrill of the Find — Utility | Thrill of discovery; compressed utility type | **High–medium** — oversized “FIND” | Supporting antiques line will likely be too small; “FIND” alone is broad | Tight full-print crop on visible garment; allow shared copy/headline to perform category decoding | Generic discovery/shopping clicks. Verify small support line is not depended upon and compressed letters are not cropped. |
| 6 | `C3B` — The Thrill Curve | Hunt emotion / discount-dot-to-SOLD ritual | **Medium–high** — bright sequence and faces | Meaning needs a beat of inspection; can resemble generic retail-sale humor | Keep all dots, faces, and SOLD tag at useful size; tighter garment crop; antique-mall context plus a short “you know this feeling” headline | Bargain-shopping attention rather than antique hunters. Preserve exact sequence, colors, baseline, and SOLD relationship. |
| 7 | `YIF-F` — Yeah, It’ll Fit — Soft | Same find-logistics recognition in a softer/female-leaning execution | **Medium** — readable joke, softer contrast | Same car/chair scale issue as `YIF-M`; visually close sibling may feel repetitive | Preserve approved softer styling; tight full-unit crop; use consistent category headline family without presenting it as a color test | Generic furniture/moving humor; similarity may reduce novelty. Keep it as a distinct product card and do not imply equal delivery is required. |
| 8 | `A1` — Good Antiques Don’t Shout | Hunter’s Eye; quiet-quality discernment explicitly tied to antiques | **Medium** — strong phrase, restrained execution | Smaller chair/copy may be difficult in-feed, but “antiques” gives valuable category clarity | Tight chest crop while keeping garment silhouette; subdued antique-shop background; product-specific headline can reinforce “a good eye” | Lower curiosity risk; greater risk is being overlooked. Do not make the quiet design artificially loud or replace it with standalone art. |
| 9 | `C2` — Found Not New — Booth 42 | Story of the find / antique-mall artifact; dealer tag and booth ticket | **Medium–low** — authentic detail rewards inspection | Small hand-lettering and ticket detail are likely weak at feed scale | Use the closest crop that keeps the whole tag/ticket composition and apparel clear; headline should decode Booth 42 / antique-mall hunting | Could read as generic resale/sustainability. Preserve worn artifact character, exact overlap, and hierarchy; no added faux-grunge. |
| 10 | `A3` — The Good Ones Don’t Shout | Hunter’s Eye / MCM discernment; quiet-confidence furniture recognition | **Low–medium** — elegant but intentionally understated | Does not independently say antiques; small chair and restrained copy are vulnerable | Tight crop with full chest unit; retain enough discovery context to decode vintage/MCM; explicit antiques/vintage headline needed | Interior-design or MCM décor curiosity. Do not treat weak feed delivery as product failure or make the approved composition louder. |

## Initial order supplied to Meta

Supply the order shown above.

The opening five establish the acquisition story quickly: expressive discovery, insider detour humor, find logistics, explicit treasure-hunter identity, and strong type-led “FIND.” The middle introduces the discount/SOLD ritual and the softer logistics variant. The closing three reward closer recognition and broaden the world into discernment, booth artifacts, and MCM.

This order is a useful cold-start editorial sequence, not a constraint on delivery. Enable predicted-best-performing-card ordering if the selected live setup supports it. Meta may change the first card and sequence for different people. Therefore:

- every card must work without positional dependence;
- essential meaning cannot rely on a preceding card;
- shared framing must travel with the carousel;
- card-specific destinations must stay attached to the correct source card after reordering;
- unequal impressions are expected;
- analysis must retain both supplied order and observed delivery/order behavior where available.

## Complementary non-carousel concepts

Do **not** create extra concepts merely to increase test count.

One meaningfully different non-carousel direction could add material acquisition learning after the carousel direction is approved:

**Behavioral scene — “The five-minute stop.”** Show a recognizable antique-mall detour moment with a person/setting as the acquisition hero and the shirt as part of the scene, rather than making a product card the sole visual subject. This would test whether lived-situation recognition acquires relevant attention better than a product-led carousel.

A second non-carousel concept is not yet earned. Consider one only if the Campaign Lead identifies a specific learning gap, budget capacity, and format/placement plan that the behavioral scene and carousel do not cover.

## Decisions made now

- Use all 10 executable products in one primary automatically reorderable carousel.
- Treat the carousel as one creative execution with one persistent `creative_id`.
- Preserve stable source-card identity and source-product `design_id` separately.
- Use a coherent warm-ivory garment / subdued discovery-environment system derived from approved LP product presentations.
- Use card-level headlines selectively for fast recognition and category decoding.
- Supply the initial order above while designing every card to stand alone.
- Preserve restrained and under-delivered products for downstream landing-page evaluation.
- Develop at most one complementary behavioral-scene concept initially.

## Unresolved Campaign Lead / Founder decisions

The Strategy Advisor / Campaign Lead must confirm:

- campaign objective;
- optimization event;
- included Facebook and Instagram placements;
- whether the campaign is image-only;
- final aspect-ratio and export matrix;
- whether the live setup offers and will use predicted-best-performing-card ordering;
- primary-text, headline, description, and CTA constraints after preview;
- landing-page destination and reliable source-card parameter convention;
- whether the complementary behavioral-scene concept fits the test budget and learning design.

The Founder must approve the selected concept set and finished creative package before spend.

## Production deferred

Do not export deployment-ready files yet. After objective and placements are confirmed, Creative should:

1. verify the exact live Meta crop and text behavior with the Campaign Operator;
2. select only the required aspect ratios—currently 1:1 Facebook Feed and possibly 4:5 Instagram Feed are references, not an approved export matrix;
3. create carousel card crops from approved customer-facing product presentations while treating locked sources as artwork authority;
4. develop final shared primary text, card headlines, description/CTA conventions, and the single behavioral-scene concept if approved;
5. assign the persistent carousel `creative_id` and stable card identities in the acquisition creative manifest;
6. review realistic mobile placement previews before issuing a Creative Director readiness decision.

Do not assume Stories or Reels and do not create 9:16 versions unless those placements are explicitly included.

## Conflicts and risks

No blocking conflict was found among Issue #56, the assortment manifest, acquisition brief, event schema, or the dated Meta production requirements.

One status tension should be preserved explicitly: the production-requirements table provides 1:1 Facebook Feed and 4:5 Instagram Feed references, while Issue #56's later finished-assets checklist says “at minimum 1:1 and 4:5.” The production document and current assignment correctly defer the final export matrix until objective and placements are confirmed. Therefore this phase recommends no exports; the Campaign Lead should reconcile the checklist wording with the approved placement plan before finished-asset production.

The approved LP images are optimized for product evaluation, not necessarily feed acquisition. They are the correct customer-facing presentation source, but their final card crops require placement-aware creative judgment. Locked artwork must not be regenerated, reinterpreted, or redesigned to solve an ad-crop problem.

## Next handoff

After this decision document is reviewed and merged:

1. Campaign Lead confirms objective, optimization event, placements, live automatic-ordering availability, and whether the one behavioral-scene concept is in scope.
2. Creative Director develops the complete carousel execution and, if approved, the single complementary behavioral-scene concept—assigning persistent IDs but not proliferating near-duplicates.
3. Campaign Operator and Technical Reviewer verify card-specific destination attribution and downstream `design_id` independence.
4. Creative Director produces only the approved export matrix and copy package, then reviews live mobile previews.
5. Brand Manager, Technical Reviewer, and Founder complete their respective pre-launch reviews and approval.

Issue #56 acquisition-candidate-selection checkboxes remain open until this document is reviewed and merged.
