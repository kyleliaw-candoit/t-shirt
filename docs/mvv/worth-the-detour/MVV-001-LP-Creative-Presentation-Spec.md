---
title: MVV-001 Landing-Page Creative Presentation Specification
brand: Worth the Detour
experiment_id: mvv-r012-001
owner: Creative Director
status: Proposed
last_updated: 2026-08-18
related_issue: 55
---

# MVV-001 — Landing-Page Creative Presentation Specification

## Purpose

Define the minimum customer-facing visual and presentation requirements for the Worth the Detour MVV #1 landing page so the MVV Landing-Page Developer / Codex can implement the experience without inventing material creative decisions.

This specification governs **creative presentation**, not front-end architecture, analytics, deployment, lead storage, or campaign mechanics.

The landing page has one primary creative job:

> **Quickly confirm the Worth the Detour antiques / vintage treasure-hunting world, then let visitors inspect and compare the actual T-shirt products fairly enough to reveal product-specific interest.**

The page must preserve the experiment distinction documented in `MVV-001-Acquisition-vs-Product-Validation.md`: acquisition creative earns relevant attention; the landing page evaluates products after visitors can inspect them properly.

---

## 1. Governing creative principles

### 1.1 Confirm the world, then get out of the products' way

The top of the page should establish three things quickly:

1. this is an apparel brand;
2. the initial world is antiques / vintage treasure hunting / flea markets / estate sales / overlooked finds;
3. the deeper identity is **For people who see what others miss.**

Do not use a long brand manifesto. Product evaluation should become the dominant experience quickly.

### 1.2 Product truth over merchandising theatrics

Use only the approved canonical primary LP images. Do not redesign the garments, artwork, print scale, print placement, crop treatment, or visual effects in implementation.

The product-image standard remains authoritative for garment fidelity, artwork fidelity, focal hierarchy, audience-aligned merchandising, and assortment fairness.

### 1.3 Fair comparison over editorial favoritism

The LP is not a lookbook ranking products by Creative Director preference. Unless a later experiment explicitly changes this, every included product should receive broadly comparable visual opportunity.

Do not create a hero product card, featured winner, larger first card, richer explanation, special badge, or materially stronger treatment for one product without explicit Creative Director / Founder approval.

### 1.4 Mobile is a primary review surface

Meta traffic will often arrive on phones. The mobile experience must make the brand legible, the assortment easy to scan, and every product inspectable without forcing desktop-style interaction patterns.

---

## 2. Page-level hierarchy

Use this hierarchy unless implementation constraints require a materially equivalent treatment:

1. **Compact brand / category orientation**
2. **Product collection introduction**
3. **10-product comparison section**
4. **Product-specific interest action(s)**
5. **Email-interest capture / follow-through**
6. **Minimal footer / trust context as needed**

The page should feel like a focused product-validation landing page, not a full ecommerce storefront.

Do not add navigation, collection taxonomy, shopping-cart chrome, merchandising filters, lifestyle editorial sections, or other storefront conventions unless they become necessary for the MVV.

---

## 3. Hero / above-the-fold intent

The first viewport should orient the visitor without delaying access to products.

### Required content intent

Include:

- **Worth the Detour** as the brand;
- **For people who see what others miss.** as the identity line;
- one concise category-decoding cue connecting the brand to antiques / vintage treasure hunting;
- a clear transition into the products.

A suitable category-decoding direction is plain, compact language such as antiques, vintage finds, flea markets, estate sales, or treasure hunting. Exact final copy belongs in the minimum creative copy package; the visual requirement here is that category meaning is explicit enough that a cold visitor should not interpret Worth the Detour as generic travel or lifestyle content.

### Above-the-fold restraint

Do not:

- lead with a large decorative lifestyle photograph that pushes products far below the fold;
- make the identity line visually compete with the brand name and product imagery;
- add a long paragraph explaining the philosophy;
- create a pseudo-luxury editorial composition that makes the brand feel precious or connoisseur-driven;
- imply that products are available to buy now.

The desired feeling is **warm, observant, credible, lightly knowing, and product-forward**.

---

## 4. Product section presentation

### 4.1 Canonical assortment

Use the 10 executable products from `MVV-001-LP-Assortment-Manifest.md`.

Default order for MVV #1:

1. `B2`
2. `A1`
3. `A3`
4. `YIF-M`
5. `YIF-F`
6. `C2`
7. `C3B`
8. `Fashion-1D-F`
9. `Type-Led-3`
10. `Type-Led-4`

This is the implementation default, not a permanent brand-wide merchandising rule. Do not change the order materially without Creative Director approval.

`Fashion-1D-GN` is excluded from MVV #1 execution and must not appear on the page.

### 4.2 Canonical product images

Use the approved primary LP assets in:

`docs/mvv/worth-the-detour/assets/lp-products/`

Expected assets:

- `R012-B2-LP-PRIMARY.png`
- `R012-A1-LP-PRIMARY.png`
- `R012-A3-LP-PRIMARY.png`
- `R012-YIF-M-LP-PRIMARY.png`
- `R012-YIF-F-LP-PRIMARY.png`
- `R012-C2-LP-PRIMARY.png`
- `R012-C3B-LP-PRIMARY.png`
- `R012-Fashion-1D-F-LP-PRIMARY.png`
- `R012-Type-Led-3-LP-PRIMARY.png`
- `R012-Type-Led-4-LP-PRIMARY.png`

Do not substitute locked-source boards, generated alternates, thumbnails, screenshots, or newly processed derivatives when the approved primary image can be used directly.

### 4.3 Product-card composition

Each product card should contain, in a consistent order:

1. primary product image;
2. obvious but restrained enlargement affordance;
3. product display name;
4. product-specific interest action;
5. only necessary supporting microcopy.

Keep cards visually quiet enough that the image and shirt idea remain the dominant read.

Do not add ratings, prices, color swatches, fake inventory, size selectors, sale badges, scarcity cues, shipping promises, or purchase controls.

---

## 5. Required tap/click-to-enlarge behavior

### Decision

**No bespoke secondary detail / inspection images are required for MVV #1.**

Instead, all 10 products must receive the same inspection behavior:

> **Tap/click the existing approved high-resolution primary product image to enlarge it.**

### Creative requirements

The enlargement behavior must:

- be available for every product, not only slower-read designs;
- use the same approved primary image at larger size;
- preserve the original image treatment and crop intent;
- avoid new filters, sharpening, color treatment, reframing, or generated detail crops;
- be visually simple and easy to dismiss;
- work naturally on touch devices;
- not introduce purchase or checkout implications;
- not create a materially richer inspection experience for one product than another.

The developer may choose modal, dialog, lightbox, or another accessible implementation mechanism. The interaction mechanics are developer discretion so long as the creative behavior above is preserved.

### Affordance

The card should make image enlargement discoverable without clutter. A small text cue, icon, cursor treatment, or equivalent is acceptable. The affordance should not visually overpower the product name or interest action.

---

## 6. Slower-read products

The following products deserve particular review for in-card comprehension:

- `C2`
- `C3B`
- `Type-Led-3`
- `Type-Led-4`

These designs must still communicate enough in the normal card state for a visitor to understand the core idea. Enlargement is for closer inspection, not for rescuing an unreadable default card.

Do not solve slower reading by enlarging only these cards, moving them into featured positions, adding extra explanatory paragraphs, or changing their artwork. Instead, ensure the general card image area is sufficiently generous and consistent across the assortment.

---

## 7. Mobile-first presentation requirements

### Mobile layout intent

Use a **single-column product flow** by default so each shirt receives meaningful width and the visitor can inspect one product at a time without cramped comparisons.

The product image should occupy the strongest visual area of each card. Product name and interest action should follow closely enough that the card reads as one unit.

Maintain comfortable spacing between cards so the user can distinguish one product from the next without creating excessive scroll dead space.

### Mobile behavior

- Product imagery must remain large enough to judge the shirt, not merely recognize that a shirt exists.
- No hover-only information or hover-only affordances.
- Enlargement must be obvious enough to discover on touch.
- Close/dismiss control for enlarged images must be easy to find and operate.
- Avoid tiny secondary text that creates a fake ecommerce density.
- Avoid sticky elements that cover meaningful product area unless explicitly approved.

The rendered mobile page is the primary Creative Director review artifact.

---

## 8. Desktop expansion behavior

Desktop may use a multi-column product grid to reduce unnecessary scrolling while preserving fair comparison.

Preferred creative direction:

- two columns is the safest default;
- three columns is acceptable only if product imagery remains comfortably inspectable and the slower-read designs still pass comprehension review;
- avoid four or more columns for the main product grid in MVV #1.

Desktop should feel like an expanded version of the same experience, not a separate editorial layout.

Do not use masonry, alternating oversized cards, asymmetrical magazine layouts, or hover-dependent product reveals.

---

## 9. Visual tone

The page should feel:

- warm;
- timeless rather than trend-chasing;
- restrained;
- slightly vintage in sensibility without becoming themed décor;
- observant and curious;
- credible and human;
- quietly confident rather than polished-to-luxury.

Prefer neutral, warm, low-noise page surfaces that let the approved product imagery carry most of the atmosphere.

Avoid:

- faux parchment;
- distressed texture overlays;
- wood-grain UI chrome;
- antique-store sign clichés;
- Victorian ornament;
- generic farmhouse styling;
- scrapbook collage treatment;
- fake stamps / labels everywhere;
- aggressive retro filters;
- glossy fashion-editorial minimalism that conflicts with the product world.

The page should suggest the Worth the Detour world through restraint and product imagery, not through decorative theming.

---

## 10. Prohibited image / creative transformations

Implementation must not:

- recolor approved product images;
- change contrast, saturation, temperature, or brightness selectively by product;
- crop products differently in ways that materially change apparent garment or print scale;
- mask garments into new shapes;
- add drop shadows, frames, borders, overlays, labels, badges, or decorative treatments selectively by product;
- generate alternate backgrounds;
- create secondary detail images;
- redraw or modify locked artwork;
- alter print size or placement;
- add artificial fabric texture;
- add review/spec boards, annotations, charts, labels, or inspection graphics inside product imagery.

Normal responsive sizing and non-destructive containment needed to place the same approved image into the page are allowed.

---

## 11. CTA presentation intent

The CTA system should detect **product-specific interest**, not imitate checkout.

### Product-card CTA intent

Each product should have a clearly associated interest action using consistent visual prominence and wording across the assortment.

The action should feel like:

> **I want this / I’m interested / tell me about this one**

rather than:

> **Buy now / Add to cart / Only X left / Preorder ships soon**

Exact wording belongs in the minimum creative copy package and must remain consistent with Brand Manager requirements.

### Email-interest capture

Email capture should appear as the natural follow-through after a visitor expresses interest, not as an unrelated newsletter signup that interrupts product browsing.

If the implementation uses an inline form, modal, drawer, or another pattern, keep the visual transition simple and clearly associated with the selected product when product-specific intent is being captured.

The Creative Director does not prescribe lead-storage mechanics or analytics behavior.

---

## 12. Developer discretion

The MVV Landing-Page Developer / Codex may decide ordinary implementation details including:

- exact CSS values;
- font sizing within the approved hierarchy;
- spacing values;
- breakpoint mechanics;
- semantic HTML structure;
- accessible modal/dialog/lightbox mechanics;
- focus states and keyboard behavior;
- image-loading implementation;
- ordinary responsive adjustments;
- whether the desktop grid uses two or three columns, provided inspection/fairness requirements remain satisfied;
- minor visual polish that does not alter brand meaning, hierarchy, product fairness, or experiment interpretation.

Use the simplest robust solution.

---

## 13. Decisions that must come back to another role

### Return to Creative Director

- strategic product-order changes;
- unequal card prominence;
- replacing approved product imagery;
- removing or materially changing enlargement behavior;
- changing product-image crop treatment in a way that affects product reading;
- introducing a hero lifestyle image or major new visual section;
- changing the hierarchy enough that product evaluation becomes secondary;
- adding explanatory content specifically to rescue one product;
- material tone / styling changes.

### Return to Brand Manager

- changes to brand positioning;
- category-decoding meaning;
- identity-line changes;
- claims about product availability, scarcity, launch timing, expertise, sustainability, or other brand promises;
- material CTA wording that changes what the visitor believes they are committing to.

### Return to Founder

- changing the executable assortment;
- reintroducing `Fashion-1D-GN`;
- changing the experiment scope;
- adding purchase / checkout capability;
- material scope expansion that would delay MVV launch for polish or infrastructure.

Technical architecture, analytics implementation, deployment, privacy implementation, and code-risk questions belong to the MVV Landing-Page Developer / Technical Reviewer, not this specification.

---

## 14. Lightweight mobile wireframe

This wireframe communicates hierarchy only. It is not pixel-perfect UI.

```text
┌──────────────────────────────┐
│ WORTH THE DETOUR             │
│ For people who see what      │
│ others miss.                 │
│                              │
│ Antiques / vintage treasure  │
│ hunting category cue         │
│                              │
│ ↓ See the shirts             │
├──────────────────────────────┤
│ THE COLLECTION               │
│ concise product-section line │
├──────────────────────────────┤
│                              │
│ [ B2 PRIMARY IMAGE        ]  │
│ [ tap image to enlarge    ]  │
│                              │
│ No, Really. Five Minutes.    │
│ [ product interest action ]  │
│                              │
├──────────────────────────────┤
│                              │
│ [ A1 PRIMARY IMAGE        ]  │
│ [ tap image to enlarge    ]  │
│                              │
│ Good Antiques Don’t Shout    │
│ [ product interest action ]  │
│                              │
├──────────────────────────────┤
│ ...same card structure...    │
├──────────────────────────────┤
│ [ Type-Led-4 PRIMARY      ]  │
│ [ tap image to enlarge    ]  │
│                              │
│ Thrill of the Find ...       │
│ [ product interest action ]  │
├──────────────────────────────┤
│ Email-interest follow-through│
│ only as needed by CTA flow   │
├──────────────────────────────┤
│ minimal footer               │
└──────────────────────────────┘
```

### Enlarged mobile state

```text
┌──────────────────────────────┐
│                         [×]  │
│                              │
│                              │
│   [ SAME APPROVED PRIMARY ]  │
│   [ IMAGE, DISPLAYED LARGE ] │
│                              │
│                              │
│      easy tap-to-close       │
└──────────────────────────────┘
```

---

## 15. Lightweight desktop wireframe

```text
┌────────────────────────────────────────────────────────────┐
│ WORTH THE DETOUR                                           │
│ For people who see what others miss.                       │
│ concise antiques / vintage treasure-hunting category cue   │
├────────────────────────────────────────────────────────────┤
│ THE COLLECTION                                             │
│ concise product-section line                               │
├───────────────────────────┬────────────────────────────────┤
│ [ B2 PRIMARY IMAGE      ] │ [ A1 PRIMARY IMAGE          ] │
│ [ enlarge affordance    ] │ [ enlarge affordance        ] │
│ No, Really. Five Minutes. │ Good Antiques Don’t Shout      │
│ [ interest action       ] │ [ interest action           ] │
├───────────────────────────┼────────────────────────────────┤
│ [ A3 PRIMARY IMAGE      ] │ [ YIF-M PRIMARY IMAGE       ] │
│ [ enlarge affordance    ] │ [ enlarge affordance        ] │
│ product name              │ product name                   │
│ [ interest action       ] │ [ interest action           ] │
├───────────────────────────┼────────────────────────────────┤
│ ...continue same system through all 10 products...         │
├────────────────────────────────────────────────────────────┤
│ Email-interest follow-through / minimal footer              │
└────────────────────────────────────────────────────────────┘
```

A three-column desktop grid is acceptable only if the actual rendered cards remain large enough for fair comprehension.

---

## 16. Rendered-page Creative Director review criteria

The rendered implementation is the real review artifact. The wireframes above are only handoff references.

Before issuing a Creative Director decision, review the actual deployed / preview page, especially on mobile, and confirm:

### Orientation

- Can a cold visitor quickly tell this is apparel?
- Is the antiques / vintage treasure-hunting world clear without a long explanation?
- Is **For people who see what others miss.** present with appropriate prominence?

### Product hierarchy

- Do products become the dominant experience quickly?
- Does any decorative or brand element compete with product evaluation?
- Does the page avoid feeling like a full store or a lifestyle editorial?

### Fairness

- Are all 10 products shown with broadly comparable image area and card treatment?
- Is any product receiving an accidental visual advantage?
- Is the default order preserved unless an approved change was made?

### Inspectability

- Can each shirt be understood in-card?
- Do `C2`, `C3B`, `Type-Led-3`, and `Type-Led-4` receive a genuine opportunity to be understood?
- Does every product enlarge consistently using the same approved primary image?
- Is enlargement easy to discover and easy to close, especially on mobile?

### Fidelity

- Are only the approved canonical LP primary images being used?
- Are image treatments consistent and non-transformative?
- Are artwork, garment proportions, print scale, and image presentation free from implementation-induced distortion?

### CTA presentation

- Is product-specific interest obvious without implying purchase?
- Are CTAs equally prominent across products?
- Does email capture feel like a continuation of expressed interest rather than unrelated newsletter capture?

### Tone

- Does the page feel warm, restrained, observant, credible, and lightly vintage without falling into themed décor or cliché?
- Is there enough breathing room to inspect products without making the page feel precious or overdesigned?

### Creative Director decision

Issue exactly one:

- `Creative ready`
- `Ready with minor observations`
- `Creative revisions required`

Request revisions only for material issues affecting comprehension, hierarchy, brand presentation, product fairness, or experiment validity. Do not delay MVV for cosmetic perfection.

---

## 17. Handoff status

This specification closes two Creative Director presentation decisions for MVV #1:

1. **Detail / inspection assets:** no bespoke secondary assets are required.
2. **Inspection behavior:** every product must use consistent tap/click-to-enlarge behavior with its existing approved high-resolution primary image.

Remaining Creative Director handoff item after this document:

> **Produce the minimum-sufficient LP creative copy package** — brand treatment, identity line, category-decoding support, collection/product-section language, product display names, CTA wording, and only necessary microcopy.

After the creative copy package is approved, the PM / MVV Landing-Page Developer should be able to create the Phase A implementation brief for Codex without inventing material creative decisions.
