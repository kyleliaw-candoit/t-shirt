---
title: MVV-001 Meta Carousel Production Requirements
brand: Worth the Detour
experiment_id: mvv-r012-001
owner: Strategy Advisor / Campaign Lead
status: Working
verified_on: 2026-08-29
platform: Meta Ads Manager
related_issue: 56
---

# MVV-001 Meta Carousel Production Requirements

## 1. Purpose

This document is the experiment-specific production and QA reference for Worth the Detour MVV #1 Meta carousel advertising.

It exists so the Creative Director, Campaign / MVV Operator, Brand Manager, and Technical Reviewer work from the same current platform constraints.

This is not a permanent company-wide Meta specification. Meta capabilities, placements, and requirements can change. The Campaign / MVV Operator must verify the live Ads Manager configuration before final asset export and again before launch.

## 2. Governing campaign model

The primary acquisition candidate is an automatically reorderable carousel containing all 10 executable MVV #1 landing-page products.

Meta's delivery and card-order optimization are intended parts of the commercial model. Equal card exposure is not required.

The intended analytical chain is:

> `creative_id → source card / source product → landing visit → downstream design exposure → design engagement → product-specific intent → lead`

The carousel-level `creative_id`, source-card / source-product identity, and downstream landing-page `design_id` must remain separate.

## 3. Confirmed Meta carousel capabilities and limits

Verified against official Meta documentation on 2026-08-29:

| Requirement / capability | Current confirmed rule |
|---|---|
| Carousel size | 2–10 cards |
| Card media | Images or videos |
| Card-specific fields | Each card can have its own headline, description, destination link, and call to action |
| Manual creation | A standard carousel can be assembled manually in Meta Ads Manager; Shopify or a product catalog is not required |
| Image maximum file size | 30 MB |
| Video maximum file size | 4 GB |
| Automatic card ordering | Meta supports showing predicted best-performing cards first |
| Facebook Feed traffic reference | 1:1; at least 1080 × 1080 pixels |
| Instagram Feed traffic reference | Meta's current placement guide reports 4:5 for image-only carousels; verify the selected objective and live placement preview before export |
| Stories / Reels | Requirements differ from Feed; do not produce 9:16 assets unless those placements are intentionally included |

These are platform constraints, not a final placement plan.

## 4. Official Meta sources

- [Design specifications for carousel ads](https://www.facebook.com/business/help/1114358518575630)
- [Create a carousel ad from Meta Ads Manager](https://www.facebook.com/business/help/1375829326076396)
- [Facebook Feed carousel specifications](https://www.facebook.com/business/ads-guide/update/carousel/facebook-feed/link-clicks)
- [Instagram Feed carousel specifications](https://www.facebook.com/business/ads-guide/update/carousel/instagram-feed/link-clicks)
- [Show predicted best-performing cards first](https://www.facebook.com/business/help/120435098301466)
- [View carousel-ad metrics](https://www.facebook.com/business/help/1609310829322538)

## 5. Campaign-specific decisions still required

The following are not resolved merely by Meta's general specifications:

- campaign objective;
- optimization event;
- included Facebook and Instagram placements;
- whether the campaign is image-only;
- final aspect-ratio and export matrix;
- shared primary text;
- card-level headline, description, and CTA conventions;
- initial supplied card order;
- whether Meta's best-performing-card-first control is available for the chosen setup;
- source-card / source-product URL-parameter convention;
- whether card-specific URLs survive Meta processing and canonical-host redirects;
- whether any complementary non-carousel executions are included;
- whether Stories or Reels versions are justified.

The Strategy Advisor / Campaign Lead owns the campaign decisions. The Creative Director owns creative execution within the approved constraints. The Campaign / MVV Operator owns live-platform verification.

## 6. Creative Director requirements

Before creating finished assets, the Creative Director must:

1. Read Issue #56, this document, the Brand Acquisition Brief, the Brand Review Checklist, and the canonical assortment manifest.
2. Design every carousel card for realistic mobile-feed comprehension.
3. Keep essential product meaning within the visible image area and avoid depending on interface text that may truncate.
4. Use the approved product assets and canonical `design_id` values.
5. Treat the 10 cards as one coherent acquisition execution while preserving each card's product identity.
6. Supply the initial card order, while assuming Meta may reorder cards.
7. Produce only the aspect ratios and placements approved in the final campaign plan.
8. Record card media, copy, destination, source-product identity, and status in the acquisition creative manifest.
9. Review actual Ads Manager previews before issuing the pre-launch Creative Director decision.

## 7. Campaign / MVV Operator live verification gate

Before final asset export or meaningful spend, the Campaign / MVV Operator must verify in the actual campaign builder:

- the selected objective supports the intended carousel and destination;
- the exact available placements;
- the exact accepted ratios, dimensions, media types, and file limits;
- the visible and truncated behavior of primary text, headline, description, and CTA;
- all 10 cards can be added;
- automatic best-performing-card ordering is available and enabled as intended;
- every card can retain its correct destination URL and source-card / source-product parameters after any reordering;
- the rendered Facebook and Instagram previews;
- Meta does not crop, pad, reorder, or transform assets in a way that changes essential meaning.

If the live interface conflicts with this document, stop and update the campaign-specific requirement before requesting creative rework.

## 8. Attribution QA gate

Before meaningful spend:

1. Configure stable carousel-level `creative_id`.
2. Configure stable card-specific source attribution using the smallest reliable mechanism supported by Meta, potentially a card-specific `utm_content` convention.
3. Perform controlled clicks from at least two different cards.
4. Verify correct source-card values through the canonical-host redirect, `landing_view`, downstream events, and D1 storage.
5. Verify that downstream `design_id` remains independent when the visitor engages with a product different from the source card.
6. Exclude controlled QA records from live analysis.
7. If reliable card attribution is unavailable, stop and choose the smallest technically reliable alternative before meaningful spend.

Do not silently change the MVV event schema. Any material semantic change must follow the schema's change-control process.

## 9. Pre-launch role checks

### Creative Director

Verify mobile comprehension, product fidelity, crop, legibility, coherent carousel presentation, and rendered-placement quality.

### Brand Manager

Verify that the complete execution attracts R012 treasure hunters, decodes antiques / vintage discovery, communicates apparel, and avoids generic vintage, thrift-fashion, farmhouse, reseller, appraisal, or travel drift.

### Technical Reviewer

Verify URL construction, source-card attribution, `creative_id` / source-product / downstream `design_id` separation, redirect persistence, D1 evidence, privacy, and unnecessary complexity.

### Founder

Approve the final creative package, campaign structure, and spending before launch.

## 10. Change control

Update this document when:

- the campaign objective or placements are approved;
- live Ads Manager behavior differs from the verified documentation;
- final export requirements are known;
- the source-card attribution method is verified;
- Meta materially changes carousel requirements before launch.

Record the verification date and cite the current official Meta source. Do not generalize MVV #1 platform behavior into permanent company methodology without repeated evidence.
